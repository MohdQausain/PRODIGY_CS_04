# PRODIGY_CS_04
Prodigy Cyber Security Internship - Task 4 - Simple Keylogger
---

# Simple Buffered Keylogger (Educational Tool)

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

This is a **simple, educational Python script** that implements a basic keyboard logger using the `pynput` library. It captures keystrokes (printable characters and special keys), buffers them in memory, and flushes the buffer to a log file every 60 seconds (1-minute intervals). It also supports fallback flushing every N keys and graceful shutdown.

**This tool is intended for legitimate, personal, and educational purposes only**, such as:
- Debugging your own input patterns in apps.
- Building simple productivity trackers (e.g., typing speed analysis).
- Learning about input event handling in Python.

It is **not** for surveillance, data theft, or any unauthorized monitoring. See the [Ethical and Legal Warnings](#ethical-and-legal-warnings) section below.

## Features

- **Buffered Logging**: Collects keystrokes in memory to reduce file I/O; flushes to file every 60 seconds.
- **Special Key Support**: Logs printable chars (e.g., 'a') and special keys (e.g., `[ENTER]`, `[SPACE]`, `[ESC]`).
- **Timestamps**: Optional per-keystroke timestamps for context.
- **Real-Time Console Output**: Prints keys as they are typed (configurable).
- **Fallback Flushing**: Automatically flushes every 10 keys to prevent data loss.
- **Graceful Shutdown**: Stop with Ctrl+C or Esc key; final buffer flush on exit.
- **Error Handling**: Basic resilience for file permissions and I/O issues (e.g., fallback to temp file).
- **Cross-Platform**: Works on Windows, macOS, and Linux (with permissions).

## Requirements

- Python 3.6 or higher.
- `pynput` library: For keyboard event listening.

No other external dependencies.

## Installation

1. Clone or download this repository (or just save the script as `fixed_simple_keylogger.py`).
2. Install the required library:
3. 3. Grant necessary permissions (see [Troubleshooting](#troubleshooting)):
- Windows: Run as Administrator if needed.
- macOS: Enable Accessibility in System Preferences > Security & Privacy > Privacy > Accessibility.
- Linux: May require `sudo` for global key capture.

## Usage

1. **Run the Script**:
2. - Console output: "Fixed simple keylogger started. Log file: ~/simple_keylog.txt"
- It begins listening for keystrokes immediately.

2. **Typing and Logging**:
- Type any keys: They appear in the console in real-time (e.g., `2023-10-05 14:30:22 h`).
- Special keys are formatted (e.g., `[ENTER]` for Enter).
- Every 10 keys: Automatic flush ("Flushed 10 entries...").
- Every 60 seconds: Interval flush to the log file.

3. **Check Logs**:
- Open the log file (default: `~/simple_keylog.txt` or your configured path).
- Example content:
  ```
  2023-10-05 14:30:22 h
  2023-10-05 14:30:23 e
  2023-10-05 14:30:23 l
  2023-10-05 14:30:24 l
  2023-10-05 14:30:24 o
  2023-10-05 14:30:25 [ENTER]

  2023-10-05 14:31:10 w
  2023-10-05 14:31:11 o
  2023-10-05 14:31:11 r
  2023-10-05 14:31:12 l
  2023-10-05 14:31:12 d
  2023-10-05 14:31:13 [ENTER]
  ```
  (Batches separated by blank lines.)

4. **Stopping the Script**:
- Press **Ctrl+C**: Triggers shutdown and final flush.
- Or press **Esc**: Immediately stops the listener and flushes.
- Console: "Keylogger stopped." All data is saved.

## Configuration

Edit the variables at the top of `fixed_simple_keylogger.py`:

- `LOG_FILE`: Path to the log file (default: `~/simple_keylog.txt` for user home dir). Example: `"C:\\temp\\simple_keylog.txt"` (Windows) or `"/tmp/simple_keylog.txt"` (Linux/Mac).
- `FLUSH_INTERVAL`: Seconds between automatic flushes (default: 60 for 1 minute).
- `FLUSH_ON_KEYS`: Flush every N keys (default: 10; set to 0 to disable).
- `ENABLE_TIMESTAMPS`: Add timestamps to entries (default: True).
- `DEBUG_PRINTS`: Show console debug info (e.g., flush confirmations; default: True).

Example: To disable timestamps and flush every 30 seconds:
```python
FLUSH_INTERVAL = 30
ENABLE_TIMESTAMPS = False

## 📸 Screenshots

### 1. CLI 
<img width="983" height="607" alt="Screenshot 2025-10-05 003303" src="https://github.com/user-attachments/assets/e4d8ae91-4d66-489f-abc5-f36cb4732f76" />

### 2. LOG TEXT FILE (AUTO SAVE)
<img width="776" height="48" alt="Screenshot 2025-10-05 003411" src="https://github.com/user-attachments/assets/203e5625-93a9-4ee6-8351-6983f78ddf45" />

### 3. INSIDE LOG FILE
<img width="478" height="647" alt="Screenshot 2025-10-05 003426" src="https://github.com/user-attachments/assets/e6ea8239-33ef-45c9-b13b-edf74c1ae859" />

---
`---EDUCATION PURPOSE ONLY--`
