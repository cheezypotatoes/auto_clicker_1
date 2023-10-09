import keyboard
import threading
import pyautogui


class ThreadCanPause(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._running_event = threading.Event()
        self.daemon = True

    def start(self):
        super().start()
        self._running_event.set()

    def pause(self):
        self._running_event.clear()

    def resume(self):
        self._running_event.set()

    def running(self):
        return self._running_event.is_set()

    def toggle(self):
        if self.running():
            self.pause()
        else:
            self.resume()


class MyLoop(ThreadCanPause):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.condition_met = False

    def run(self):
        while True:
            if self.running() and self.condition_met:
                pyautogui.click()


def start_keyboard_loop():
    # Initialize the loop
    loop = MyLoop()

    # Avoid it running automatically
    press_g_once = False

    def handle_g_key(event):
        nonlocal press_g_once
        # Doesn't automatically toggle() when the program starts
        if event.event_type == keyboard.KEY_DOWN and press_g_once:
            loop.toggle()
        else:
            # Start the program manually from the parent class if it's the first time
            loop.condition_met = True
            press_g_once = True
            loop.start()

    keyboard.on_press_key("g", handle_g_key)
    keyboard.wait('=')
