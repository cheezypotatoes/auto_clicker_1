import threading
import tkinter as tk
from listener import start_keyboard_loop


class CustomKeybindManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Auto Clicker")
        self.setup_gui()
        self.start_keyboard_listener()

    def setup_gui(self):
        # Create a label widget and add it to the window
        label_text = "Hello There, Press G to start"
        label = tk.Label(self, text=label_text)
        label.pack(pady=10)  # Add some padding around the label

    @staticmethod
    def start_keyboard_listener():
        # Create a thread for running the keyboard listener
        keyboard_listener_thread = threading.Thread(target=start_keyboard_loop)
        keyboard_listener_thread.daemon = True
        keyboard_listener_thread.start()


if __name__ == "__main__":
    app = CustomKeybindManager()
    app.mainloop()
