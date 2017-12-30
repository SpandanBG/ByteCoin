"""
This class is responsible to create a log file of each run
of the application
"""

class ConsoleLog:
    # Constants
    _LOG_DIR = "log/"

    """------------------------------DEFAULT"""
    def __init__(self):
        self._file_name = self._gen_file_name()
        return

    """------------------------------PUBLIC"""
    def log(self, msg):
        return

    """------------------------------PRIVATE"""
    def _gen_file_name(self):
        return
