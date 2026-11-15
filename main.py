import threading
import time

from canbus import can_loop

def main():
    threading.Thread(
        target=can_loop,
        daemon=True
    ).start()
