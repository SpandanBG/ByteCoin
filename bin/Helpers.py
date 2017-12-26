import json
import time
import threading


"""
This script contains all the helper functions
"""

# Json Loader
def loadJson(path=None, text=None):
    try:
        if path is not None:
            file = open(path, "r")
            data = file.read()
            file.close()
            return json.loads(data)
        elif text is not None:
            return json.loads(text)
        else:
            return None
    except Exception:
        return None

# Countdown thread
class Clock(threading.Thread):
    def __init__(self, this, id):
        threading.Thread.__init__(self)
        self._callingClass = this
        self._ticks = 0
        self._clock_id = id
        self._exit = False
        return

    def run(self):
        while self._exit is False and self._ticks > 0:
            time.sleep(1)
            self._ticks = self._ticks - 1
            if self._ticks == 0:
                self._callingClass.timed(self._clock_id)
        self._exit = True
        return

    def countDown(self, ticks):
        self._ticks = ticks
        return

    def stop(self):
        self._exit = True

    def clockStopped(self):
        return not self.isAlive()

# Stack Class
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
        return

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def all_items(self):
        return self._items