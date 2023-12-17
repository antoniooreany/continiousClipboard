# # import string
# # import pyperclip
# # from pynput import keyboard
# # from pynput.keyboard import Key
# #
# # # Initialize an empty string current_word outside the on_press function
# # current_word = ""
#
# # def on_press(key):
# #     global current_word
# #     try:
# #         # Check if the pressed key is alphanumeric
# #         if key.char.isalnum():
# #             current_word += key.char
# #         elif key == Key.space or key.char in string.punctuation:
# #             # Copy current_word to the clipboard and reset it
# #             pyperclip.copy(current_word)
# #             current_word = ""
# #     except AttributeError:
# #         pass  # special key pressed
# #
# #
#
#
# # def on_press(key):
# #     global current_word
# #     try:
# #         # Check if the pressed key is alphanumeric
# #         if key.char.isalnum():
# #             current_word += key.char
# #         # Check if the pressed key is a space or a punctuation mark
# #         elif key == Key.space or (hasattr(key, 'char') and key.char in string.punctuation):
# #             # Copy current_word to the clipboard and reset it
# #             pyperclip.copy(current_word)
# #             current_word = ""
# #     except AttributeError:
# #         pass  # special key pressed
# #
# #
#
#
# import string
# import pyperclip
# from pynput import keyboard
# from pynput.keyboard import Key
#
# EMPTY_STR = ""
#
# V_CHAR = 'v'
#
# LAST_CHAR_INDEX = -1
#
# V = 'v'
#
# # Initialize an empty string current_word outside the on_press function
# # This variable will be used to store the characters of a word as they are typed
# current_word = ""
#
# # def on_press(key):
# #     """
# #     This function is called whenever a key is pressed. It checks if the pressed key is alphanumeric, a space, or a punctuation mark.
# #     If the key is alphanumeric, it is added to the current_word string.
# #     If the key is a space or a punctuation mark, the current_word is copied to the clipboard and then reset to an empty string.
# #     If the key is a special key (like Shift, Ctrl, etc.), an AttributeError is raised and caught, and the function does nothing.
# #
# #     Args:
# #         key (Key): The key that was pressed.
# #     """
# #     global current_word
# #     try:
# #         # Check if the pressed key is alphanumeric
# #         #
# #         # if key.char.isalnum():  # TODO no attribute 'char' error
# #         if hasattr(key, 'char') and key.char.isalnum():
# #             # TODO: what if the key is a space or a punctuation mark?
# #             # Add the pressed key to the current_word string
# #             current_word += key.char  # TODO no attribute 'char' error
# #         # Check if the pressed key is a space or a punctuation mark
# #         elif key == Key.space or (
# #                 hasattr(key, 'char') and key.char in string.punctuation):  # TODO no attribute 'char' error
# #             # Copy current_word to the clipboard and reset it
# #             pyperclip.copy(current_word)
# #             current_word = ""
# #     except AttributeError:
# #         raise AttributeError  # special key pressed
#
#
# import string
# import pyperclip
# from pynput import keyboard
# from pynput.keyboard import Key
#
# current_word = ""
#
# # TODO the start and the finish of the sentence is not in the clipboard. Fix it.
# # TODO the deleted characters should not be in the clipboard. Fix it.
# # def on_press(key):
# #     global current_word
# #     try:
# #         if isinstance(key, keyboard.KeyCode) and key.char.isalnum():
# #             current_word += key.char
# #         elif key == Key.space or (isinstance(key, keyboard.KeyCode) and key.char in string.punctuation):
# #             pyperclip.copy(current_word)
# #             current_word = ""
# #     except AttributeError:
# #         pass
# # todo write the program which save every typed word in the clipboard automatically
# # def on_press(key):
# #     global current_word
# #     try:
# #         if isinstance(key, keyboard.KeyCode) and key.char.isalnum():
# #             current_word += key.char
# #         elif key in [Key.space, Key.enter, Key.shift_r] or (isinstance(key, keyboard.KeyCode) and key.char in string.punctuation):
# #             pyperclip.copy(current_word)
# #             current_word = ""
# #     except AttributeError:
# #         pass
#
# # todo find the way on how to copy the last word in the clipboard
# # TODO the deleted characters should not be in the clipboard. Fix it.
# # def on_press(key):
# #     global current_word
# #     try:
# #         if isinstance(key, keyboard.KeyCode) and key.char.isalnum():
# #             current_word += key.char
# #         elif key in [Key.space, Key.enter, Key.shift_r] or (
# #                 isinstance(key, keyboard.KeyCode) and key.char in string.punctuation):
# #             pyperclip.copy(current_word)
# #             current_word = ""
# #         elif key == Key.backspace:
# #             current_word = current_word[:-1]
# #     except AttributeError:
# #         pass
#
# # def on_press(key):
# #     global current_word
# #     try:
# #         if isinstance(key, keyboard.KeyCode) and key.char.isalnum():
# #             current_word += key.char
# #         elif key in [Key.space, Key.enter, Key.shift_r] or (
# #                 isinstance(key, keyboard.KeyCode) and key.char in string.punctuation):
# #             pyperclip.copy(current_word)
# #             current_word = ""
# #         elif key == Key.backspace:
# #             current_word = current_word[:-1]  # Remove the last character from current_word
# #             pyperclip.copy(current_word)  # Update the clipboard with the updated current_word
# #     except AttributeError:
# #         pass
#
#
# # def on_press(key):
# #     global current_word
# #     try:
# #         # Check if win-v is pressed
# #         if key == keyboard.Key.cmd and keyboard.KeyCode.from_char(V):
# #             return  # todo not sure about return, maybe continue
# #         if isinstance(key, keyboard.KeyCode) and key.char.isalnum():
# #             current_word += key.char
# #         elif key in [Key.space, Key.enter, Key.shift_r] or (
# #                 isinstance(key, keyboard.KeyCode) and key.char in string.punctuation):
# #             pyperclip.copy(current_word)
# #             current_word = ""
# #         elif key == Key.backspace:
# #             current_word = current_word[:LAST_CHAR_INDEX]  # Remove the last character from current_word
# #             pyperclip.copy(current_word)  # Update the clipboard with the updated current_word
# #     except AttributeError:
# #         pass
# #
# #
# # # Start the keylogger
# # with keyboard.Listener(on_press=on_press) as listener:
# #     listener.join()
#
# ####################################################################################################
# # Start the keylogger
# # with keyboard.Listener(on_press=on_press) as listener:
# #     listener.join()
#
# # Start the keylogger
# # The Listener object listens for key presses and calls the on_press function whenever a key is pressed
# # with keyboard.Listener(on_press=on_press) as listener:
# #     listener.join()
# ####################################################################################################
#
# # from pynput import keyboard
# # from pynput.keyboard import Key
# #
# # current_word = ""
# # win_pressed = False
# #
# #
# # def on_press(key):
# #     global current_word, win_pressed
# #     try:
# #         if key == keyboard.Key.cmd:
# #             win_pressed = True
# #             return
# #         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
# #             return
# #         if isinstance(key, keyboard.KeyCode) and key.char.isalnum():
# #             current_word += key.char
# #         elif key in [Key.space, Key.enter, Key.shift_r] or (
# #                 isinstance(key, keyboard.KeyCode) and key.char in string.punctuation):
# #             pyperclip.copy(current_word)
# #             current_word = EMPTY_STR
# #         elif key == Key.backspace:
# #             current_word = current_word[:LAST_CHAR_INDEX]
# #             pyperclip.copy(current_word)
# #     except AttributeError:
# #         pass
# #
# #
# # def on_release(key):
# #     global win_pressed
# #     if key == keyboard.Key.cmd:
# #         win_pressed = False
# #
# #
# # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
# #     listener.join()
import string

import pyperclip
# import pyperclip
# from pynput import keyboard
# from pynput.keyboard import Key
#
# EMPTY_STR = ""
# V_CHAR = 'v'
# LAST_CHAR_INDEX = -1
#
# current_word = EMPTY_STR
# win_pressed = False
#

#
#
# def on_press(key):
#     global current_word, win_pressed
#     try:
#         if key == keyboard.Key.cmd:
#             win_pressed = True
#             return
#         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
#             return
#         if isinstance(key, keyboard.KeyCode) and key.char.isalnum():
#             current_word += key.char
#         elif key in [Key.space, Key.enter, Key.shift_r] or (
#                 isinstance(key, keyboard.KeyCode) and key.char in string.punctuation):
#             pyperclip.copy(current_word)
#             current_word = EMPTY_STR
#         elif key == Key.backspace:
#             current_word = current_word[:LAST_CHAR_INDEX]
#             pyperclip.copy(current_word)
#     except AttributeError:
#         pass
#
#


# def on_press(key):
#     global current_word, win_pressed
#     try:
#         if key == keyboard.Key.cmd:
#             win_pressed = True
#             return
#         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
#             return
#         if isinstance(key, keyboard.KeyCode) and (key.char.isalnum() or key.char == '#'):
#             current_word += key.char
#         elif key in [Key.space, Key.enter, Key.shift_r] or (
#                 isinstance(key, keyboard.KeyCode) and key.char in string.punctuation and key.char != '#'):
#             pyperclip.copy(current_word)
#             current_word = EMPTY_STR
#         elif key == Key.backspace:
#             current_word = current_word[:LAST_CHAR_INDEX]
#             pyperclip.copy(current_word)
#     except AttributeError:
#         pass  # todo process special keys


# def on_press(key):
#     global current_word, win_pressed
#     try:
#         if key == keyboard.Key.cmd:
#             win_pressed = True
#             return
#         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
#             return
#         if isinstance(key, keyboard.KeyCode):
#             current_word += key.char
#         elif key in [Key.space, Key.enter, Key.shift_r] or (
#                 isinstance(key, keyboard.KeyCode) and key.char != '#'):
#             pyperclip.copy(current_word)
#             current_word = EMPTY_STR
#         elif key == Key.backspace:
#             current_word = current_word[:LAST_CHAR_INDEX]
#             pyperclip.copy(current_word)
#     except AttributeError:
#         pass


# def on_press(key):
#     global current_word, win_pressed
#     try:
#         if key == keyboard.Key.cmd:
#             win_pressed = True
#             return
#         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
#             return
#         if isinstance(key, keyboard.KeyCode):
#             current_word += key.char
#         elif key in [Key.space, Key.enter, Key.shift_r]:
#             pyperclip.copy(current_word)
#             current_word = EMPTY_STR
#         elif key == Key.backspace:
#             current_word = current_word[:LAST_CHAR_INDEX]
#             pyperclip.copy(current_word)
#     except AttributeError:
#         pass
#
#
# def on_release(key):
#     global win_pressed
#     if key == keyboard.Key.cmd:
#         win_pressed = False
#
#
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

# from pynput import keyboard
# from pynput.keyboard import Key
#
# # Constants for the program
# EMPTY_STR = ""
# V_CHAR = 'v'
# LAST_CHAR_INDEX = -1
#
# # Global variables to hold the current word and the state of the 'win' key
# current_word = EMPTY_STR
# win_pressed = False
#
#
# def on_press(key):
#     """
#     Function to handle key press events.
#
#     Args:
#         key (pynput.keyboard.Key): The key that was pressed.
#
#     Global:
#         current_word (str): The current word being typed.
#         win_pressed (bool): Whether the 'win' key is pressed.
#     """
#     global current_word, win_pressed
#     try:
#         # If 'win' key is pressed, set win_pressed to True and return
#         if key == keyboard.Key.cmd:
#             win_pressed = True
#             return
#         # If 'win' key is pressed and 'v' is pressed, return
#         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
#             return
#         # If any character key is pressed, add it to current_word
#         if isinstance(key, keyboard.KeyCode):
#             current_word += key.char
#         # If space, enter, or shift_r is pressed, or a character key other than '#' is pressed,
#         # copy current_word to clipboard and reset current_word
#         elif key in [Key.space, Key.enter, Key.shift_r]:
#             pyperclip.copy(current_word)
#             current_word = EMPTY_STR
#         # If backspace is pressed, remove the last character from current_word and update the clipboard
#         elif key == Key.backspace:
#             current_word = current_word[:LAST_CHAR_INDEX]
#             pyperclip.copy(current_word)
#     except AttributeError:
#         pass
#
#
# def on_release(key):
#     """
#     Function to handle key release events.
#
#     Args:
#         key (pynput.keyboard.Key): The key that was released.
#
#     Global:
#         win_pressed (bool): Whether the 'win' key is pressed.
#     """
#     global win_pressed
#     # If 'win' key is released, set win_pressed to False
#     if key == keyboard.Key.cmd:
#         win_pressed = False
#
#
# # Start the listener to listen for key press and release events
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

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
    global current_word, win_pressed, backspace_pressed
    try:
        if key == keyboard.Key.cmd:
            win_pressed = True
            return
        if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
            return
        if isinstance(key, keyboard.KeyCode):
            if backspace_pressed:
                backspace_pressed = False
                pyperclip.copy(current_word)
            current_word += key.char
        elif key in [Key.space, Key.enter, Key.shift_r]:
            pyperclip.copy(current_word)
            current_word = EMPTY_STR
        elif key == Key.backspace:
            current_word = current_word[:LAST_CHAR_INDEX]
            backspace_pressed = True
    except AttributeError:
        pass


# def on_press(key):
#     global current_word, win_pressed
#     try:
#         if key == keyboard.Key.cmd:
#             win_pressed = True
#             return
#         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
#             return
#         if isinstance(key, keyboard.KeyCode) and key.char is not None:
#             current_word += key.char
#         elif key in [Key.space, Key.enter, Key.shift_r]:
#             pyperclip.copy(current_word)
#             current_word = EMPTY_STR
#         elif key == Key.backspace:
#             current_word = current_word[:LAST_CHAR_INDEX]
#             pyperclip.copy(current_word)
#     except AttributeError:
#         pass


def on_release(key):
    global win_pressed
    if key == keyboard.Key.cmd:
        win_pressed = False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
