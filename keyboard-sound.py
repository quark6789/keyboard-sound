#!/usr/bin/env python3
import string
import time

from simpleaudio import WaveObject
from pynput import keyboard


sounds = {
    "backspace": WaveObject.from_wave_file("sounds/backspace.wav"),
    "caps_lock": WaveObject.from_wave_file("sounds/caps_lock.wav"),
    "enter": WaveObject.from_wave_file("sounds/enter.wav"),
    "space": WaveObject.from_wave_file("sounds/space.wav")
}
for letter in list(string.ascii_lowercase):
    sounds[letter] = WaveObject.from_wave_file(f"sounds/{letter}.wav")


def on_press(key):
    if isinstance(key, keyboard.KeyCode):  # Alphanumeric keys
        key_str = key.char.lower()
    elif isinstance(key, keyboard.Key):  # Special keys
        key_str = str(key)[4:]
    else:  # Unknown keys are None
        return
    
    try:
        play_obj = sounds[key_str].play()
    except KeyError:
        pass


def on_release(key):
    pass


if __name__ == "__main__":
    print("Press Ctrl + C to exit")
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    try:
        while(True):
            time.sleep(600)
    except KeyboardInterrupt:
        pass
