import pyperclip


# todo /fix  when I write 'bbbbXRTH' and then remove 'XRTH' the app should add only 'bbbb'. rewrite like this

from pynput import keyboard
from pynput.keyboard import Key

EMPTY_STR = ""
V_CHAR = 'v'
LAST_CHAR_INDEX = -1

current_word = EMPTY_STR
win_pressed = False
backspace_pressed = False


def on_press(key):
    global current_word, win_pressed
    try:
        if key == keyboard.Key.cmd:
            win_pressed = True
            return
        if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
            return
        if isinstance(key, keyboard.KeyCode) and key.char is not None:
            current_word += key.char
        elif key in [Key.space, Key.enter, Key.shift_r]:
            pyperclip.copy(current_word)
            current_word = EMPTY_STR
        elif key == Key.backspace:
            current_word = current_word[:LAST_CHAR_INDEX]
            pyperclip.copy(current_word)
    except AttributeError:
        pass


def on_release(key):
    global win_pressed
    if key == keyboard.Key.cmd:
        win_pressed = False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
