# # # # # # import pyperclip
# # # # # #
# # # # # # from pynput import keyboard
# # # # # # from pynput.keyboard import Key
# # # # # #
# # # # # # EMPTY_STR = ""
# # # # # # V_CHAR = 'v'
# # # # # # LAST_CHAR_INDEX = -1
# # # # # #
# # # # # # current_word = EMPTY_STR
# # # # # # win_pressed = False
# # # # # # backspace_pressed = False
# # # # # #
# # # # # #
# # # # # # def on_press(key):
# # # # # #     global current_word, win_pressed
# # # # # #     try:
# # # # # #         if key == keyboard.Key.cmd:
# # # # # #             win_pressed = True
# # # # # #             return
# # # # # #         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
# # # # # #             return
# # # # # #         if isinstance(key, keyboard.KeyCode) and key.char is not None:
# # # # # #             current_word += key.char
# # # # # #         elif key in [Key.space, Key.enter, Key.shift_r]:
# # # # # #             pyperclip.copy(current_word)
# # # # # #             current_word = EMPTY_STR
# # # # # #         elif key == Key.backspace:
# # # # # #             current_word = current_word[:LAST_CHAR_INDEX]
# # # # # #             pyperclip.copy(current_word)
# # # # # #     except AttributeError:
# # # # # #         pass
# # # # # #
# # # # # #
# # # # # # def on_release(key):
# # # # # #     global win_pressed
# # # # # #     if key == keyboard.Key.cmd:
# # # # # #         win_pressed = False
# # # # # #
# # # # # #
# # # # # # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
# # # # # #     listener.join()
# # # # #
# # # # # import pyperclip
# # # # # from pynput import keyboard
# # # # # from pynput.keyboard import Key
# # # # #
# # # # # EMPTY_STR = ""
# # # # # V_CHAR = 'v'
# # # # # LAST_CHAR_INDEX = -1
# # # # #
# # # # # current_word = EMPTY_STR
# # # # # win_pressed = False
# # # # # backspace_pressed = False
# # # # #
# # # # #
# # # # # def on_press(key):
# # # # #     global current_word, win_pressed
# # # # #     try:
# # # # #         if key == keyboard.Key.cmd:
# # # # #             win_pressed = True
# # # # #             return
# # # # #         if win_pressed and keyboard.KeyCode.from_char(V_CHAR):
# # # # #             return
# # # # #         if isinstance(key, keyboard.KeyCode) and key.char is not None:
# # # # #             current_word += key.char
# # # # #         elif key in [Key.space, Key.enter, Key.shift_r]:
# # # # #             pyperclip.copy(current_word)
# # # # #             current_word = EMPTY_STR
# # # # #         elif key == Key.backspace:
# # # # #             clipboard_content = pyperclip.paste()
# # # # #             if len(clipboard_content) < len(current_word):
# # # # #                 current_word = clipboard_content
# # # # #             pyperclip.copy(current_word)
# # # # #     except AttributeError:
# # # # #         pass
# # # # #
# # # # # def on_release(key):
# # # # #     global win_pressed
# # # # #     if key == keyboard.Key.cmd:
# # # # #         win_pressed = False
# # # # #
# # # # # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
# # # # #     listener.join()
# # # #
# # # # import pyperclip
# # # # from pynput import keyboard
# # # # from pynput.keyboard import Key
# # # #
# # # #
# # # # class KeyboardListener:
# # # #     def __init__(self):
# # # #         self.current_word = ""
# # # #         self.win_pressed = False
# # # #
# # # #     def on_press(self, key):
# # # #         if key == keyboard.Key.cmd:
# # # #             self.win_pressed = True
# # # #             return
# # # #         if self.win_pressed and key == keyboard.KeyCode.from_char('v'):
# # # #             return
# # # #         if isinstance(key, keyboard.KeyCode) and key.char is not None:
# # # #             self.current_word += key.char
# # # #         elif key in [Key.space, Key.enter, Key.shift_r]:
# # # #             pyperclip.copy(self.current_word)
# # # #             self.current_word = ""
# # # #         elif key == Key.backspace:
# # # #             clipboard_content = pyperclip.paste()
# # # #             if len(clipboard_content) < len(self.current_word):
# # # #                 self.current_word = clipboard_content
# # # #             pyperclip.copy(self.current_word)
# # # #
# # # #     def on_release(self, key):
# # # #         if key == keyboard.Key.cmd:
# # # #             self.win_pressed = False
# # # #
# # # #
# # # # listener = KeyboardListener()
# # # #
# # # # with keyboard.Listener(on_press=listener.on_press, on_release=listener.on_release) as listener:
# # # #     listener.join()
# # #
# # # import pyperclip
# # # from pynput import keyboard
# # # from pynput.keyboard import Key
# # #
# # # EMPTY_STRING = ""
# # # V_CHAR = 'v'
# # # SPECIAL_KEYS = [Key.space, Key.enter, Key.shift_r]
# # #
# # #
# # # class KeyboardListener:
# # #     def __init__(self):
# # #         self.current_word = EMPTY_STRING
# # #         self.win_pressed = False
# # #
# # #     # def on_press(self, key):
# # #     #     #     if key == keyboard.Key.cmd:
# # #     #     #         self.win_pressed = True
# # #     #     #         return
# # #     #     #     if self.win_pressed and key == keyboard.KeyCode.from_char(V_CHAR):
# # #     #     #         return
# # #     #     #     if isinstance(key, keyboard.KeyCode) and key.char is not None:
# # #     #     #         self.current_word += key.char
# # #     #     #     elif key in SPECIAL_KEYS:
# # #     #     #         pyperclip.copy(self.current_word)
# # #     #     #         self.current_word = EMPTY_STRING
# # #     #     #     elif key == Key.backspace:
# # #     #     #         clipboard_content = pyperclip.paste()
# # #     #     #         if len(clipboard_content) < len(self.current_word):
# # #     #     #             self.current_word = clipboard_content
# # #     #     #         pyperclip.copy(self.current_word)
# # #
# # #     def on_press(self, key):
# # #         if key == keyboard.Key.cmd:
# # #             self.win_pressed = True
# # #         elif self.win_pressed and key == keyboard.KeyCode.from_char(V_CHAR):
# # #             return
# # #         elif isinstance(key, keyboard.KeyCode) and key.char is not None:
# # #             self.current_word += key.char
# # #         elif key in SPECIAL_KEYS:
# # #             pyperclip.copy(self.current_word)
# # #             self.current_word = EMPTY_STRING
# # #         elif key == Key.backspace:
# # #             clipboard_content = pyperclip.paste()
# # #             if len(clipboard_content) < len(self.current_word):
# # #                 self.current_word = clipboard_content
# # #             pyperclip.copy(self.current_word)
# # #
# # #     def on_release(self, key):
# # #         if key == keyboard.Key.cmd:
# # #             self.win_pressed = False
# # #
# # # listener = KeyboardListener()
# # #
# # # with keyboard.Listener(on_press=listener.on_press, on_release=listener.on_release) as listener:
# # #     listener.join()
# # #
# #
# # import pyperclip
# # from pynput import keyboard
# # from pynput.keyboard import Key
# #
# # EMPTY_STRING = ""
# # V_CHAR = 'v'
# # SPECIAL_KEYS = [Key.space, Key.enter, Key.shift_r]
# #
# #
# # class KeyboardListener:
# #     def __init__(self):
# #         self.current_word = EMPTY_STRING
# #         self.win_pressed = False
# #
# #     def on_press(self, key):
# #         if key == keyboard.Key.cmd:
# #             self.win_pressed = True
# #         elif self.win_pressed and key == keyboard.KeyCode.from_char(V_CHAR):
# #             return
# #         elif isinstance(key, keyboard.KeyCode) and key.char is not None:
# #             self.current_word += key.char
# #         elif key in SPECIAL_KEYS:
# #             pyperclip.copy(self.current_word)
# #             self.current_word = EMPTY_STRING
# #         elif key == Key.backspace:
# #             clipboard_content = pyperclip.paste()
# #             if len(clipboard_content) < len(self.current_word):
# #                 self.current_word = clipboard_content
# #             pyperclip.copy(self.current_word)
# #
# #     def on_release(self, key):
# #         if key == keyboard.Key.cmd:
# #             self.win_pressed = False
# #
# #
# # listener = KeyboardListener()
# #
# # with keyboard.Listener(on_press=listener.on_press, on_release=listener.on_release) as listener:
# #     listener.join()
#
# import pyperclip
# import platform
# from pynput import keyboard
# from pynput.keyboard import Key
#
# EMPTY_STRING = ""
# V_CHAR = 'v'
# SPECIAL_KEYS = [Key.space, Key.enter, Key.shift_r]
#
#
# class KeyboardListener:
#     def __init__(self):
#         self.current_word = EMPTY_STRING
#         self.cmd_pressed = False
#         self.system = platform.system()
#
#     def on_press(self, key):
#         if self.system == 'Darwin' and key == keyboard.Key.cmd:
#             self.cmd_pressed = True
#         elif self.system in ['Windows', 'Linux'] and key == keyboard.Key.ctrl:
#             self.cmd_pressed = True
#         elif self.cmd_pressed and key == keyboard.KeyCode.from_char(V_CHAR):
#             return
#         elif isinstance(key, keyboard.KeyCode) and key.char is not None:
#             self.current_word += key.char
#         elif key in SPECIAL_KEYS:
#             pyperclip.copy(self.current_word)
#             self.current_word = EMPTY_STRING
#         elif key == Key.backspace:
#             clipboard_content = pyperclip.paste()
#             if len(clipboard_content) < len(self.current_word):
#                 self.current_word = clipboard_content
#             pyperclip.copy(self.current_word)
#
#     def on_release(self, key):
#         if self.system == 'Darwin' and key == keyboard.Key.cmd:
#             self.cmd_pressed = False
#         elif self.system in ['Windows', 'Linux'] and key == keyboard.Key.ctrl:
#             self.cmd_pressed = False
#
#
# listener = KeyboardListener()
#
# with keyboard.Listener(on_press=listener.on_press, on_release=listener.on_release) as listener:
#     listener.join()

import pyperclip
import platform
from pynput import keyboard
from pynput.keyboard import Key

EMPTY_STRING = ""
V_CHAR = 'v'
SPECIAL_KEYS = [Key.space, Key.enter, Key.shift_r]
SYSTEM_DARWIN = 'Darwin'
SYSTEM_WINDOWS = 'Windows'
SYSTEM_LINUX = 'Linux'


# todo /fix  when I write 'bbbbXRTH' and then remove 'XRTH' the app should add only 'bbbb'. rewrite like this
class KeyboardListener:
    def __init__(self):
        self.current_word = EMPTY_STRING
        self.cmd_pressed = False
        self.system = platform.system()

    def on_press(self, key):
        if self.system == SYSTEM_DARWIN and key == keyboard.Key.cmd:
            self.cmd_pressed = True
        elif self.system in [SYSTEM_WINDOWS, SYSTEM_LINUX] and key == keyboard.Key.ctrl:
            self.cmd_pressed = True
        elif self.cmd_pressed and key == keyboard.KeyCode.from_char(V_CHAR):
            return
        elif isinstance(key, keyboard.KeyCode) and key.char is not None:
            self.current_word += key.char
        elif key in SPECIAL_KEYS:
            pyperclip.copy(self.current_word)
            self.current_word = EMPTY_STRING
        elif key == Key.backspace:
            clipboard_content = pyperclip.paste()
            if len(clipboard_content) < len(self.current_word):
                self.current_word = clipboard_content
            pyperclip.copy(self.current_word)

    def on_release(self, key):
        if self.system == SYSTEM_DARWIN and key == keyboard.Key.cmd:
            self.cmd_pressed = False
        elif self.system in [SYSTEM_WINDOWS, SYSTEM_LINUX] and key == keyboard.Key.ctrl:
            self.cmd_pressed = False


listener = KeyboardListener()

with keyboard.Listener(on_press=listener.on_press, on_release=listener.on_release) as listener:
    listener.join()
