from bin import \
    CryCoin as CC, \
    Cryptowatch as CW, \
    Coindelta as CD, \
    ZPhase as ZP, \
    Helpers as HP

import threading
"""
This class is responsible to handle all back end and front end communications
"""
class Manager(threading.Thread):
    # Class Instants
    _EXCHANGE_RATE = 0.0
    _BEST_BID = 0.0
    _RATIO = 0.0
    _PROCESSED_VALUE = 0.0
    _Z = 0.0
    _crypto_cur = ""
    _IS_STOP_EXECUTED = False
    _TICKS = 5
    _clock_id = 0

    """--------------------- DEFAULTS"""
    def __init__(self):
        threading.Thread.__init__(self)
        self._exit = False

        self._ccoins = CC.CryCoin()
        self._zphase = ZP.ZPhase()
        self._command_stack = HP.Stack()

        self._is_refreshing = False
        return

    def set_ui_thread(self, this):
        self._calling_class = this
        return

    def run(self):
        while self._exit is False:
            while not self._command_stack.is_empty():
                _command = self._command_stack.pop()
                if _command == "refresh":
                    self._refresh()
                elif _command == "stop":
                    self._exit = True
                    break
        return

    """--------------------- COMMUTES"""
    def timed(self, id):
        if id == self._clock_id and self._IS_STOP_EXECUTED is False:
            self.refresh()
        return

    def newX(self, value, m_tag):
        if self._IS_STOP_EXECUTED is False and self._ccoins.m_select == m_tag:
            try:
                self._EXCHANGE_RATE = float(value)
                self._calling_class.newX(value)
                self._zphase.setXandY(self._EXCHANGE_RATE, self._BEST_BID)
                self._calling_class.update_ratio(self._zphase.ratio())
                self._calling_class.update_processed_rate(self._zphase.processRate())
            except Exception as e:
                # TODO: add logging here
                print(e)
        return

    def newY(self, value, m_tag):
        if self._IS_STOP_EXECUTED is False and self._ccoins.m_select == m_tag:
            try:
                self._BEST_BID = float(value)
                self._calling_class.newY(value)
                self._zphase.setXandY(self._EXCHANGE_RATE, self._BEST_BID)
                self._calling_class.update_ratio(self._zphase.ratio())
                self._calling_class.update_processed_rate(self._zphase.processRate())
            except Exception as e:
                # TODO: add logging here
                print(e)
        return

    def error(self, msg):
        if self._IS_STOP_EXECUTED is False:
            self._calling_class.error(msg)
        return

    """--------------------- PUBLIC"""
    def stop(self):
        self._command_stack.push("stop")
        self._IS_STOP_EXECUTED = True
        try:
            self.clock.stop()
        except Exception: pass
        return

    def cancel_refresh(self):
        try:
            self.clock.stop()
        except Exception: pass
        self._is_refreshing = False
        return

    def refresh(self):
        self._command_stack.push("refresh")
        return

    def setN(self, n):
        self._ccoins.setNselect(value=n)
        return

    def setM(self, m):
        self._ccoins.setMselect(value=m)
        return

    def setZ(self, Z):
        self._zphase.setBuyRate(Z)
        if self._IS_STOP_EXECUTED is False:
            self._calling_class.update_processed_rate(self._zphase.processRate())

    """--------------------- PRIVATE"""
    def _refresh(self):
        if self._IS_STOP_EXECUTED is False and self._is_refreshing is False:
            self._is_refreshing = True
            try:
                self._calling_class.error("CONNECTING...")
                cwatch = CW.Cryptowatch(self)
                cdelta = CD.Coindelta(self)

                cwatch.setPair(n=self._ccoins.n_select, m=self._ccoins.m_select)
                cdelta.set_id(self._ccoins.m_select)

                cwatch.start()
                cdelta.start()

                cwatch.join()
                cdelta.join()
                if self._IS_STOP_EXECUTED is False and self._is_refreshing is True:
                    self._calling_class.error("CONNECTED")
                    self._is_refreshing = False
                    self._clock_id = self._clock_id + 1
                    self.clock = HP.Clock(self, self._clock_id)
                    self.clock.countDown(self._TICKS)
                    self.clock.start()
            except Exception:
                if self._IS_STOP_EXECUTED is False:
                    self._calling_class.error("CONNECTION ERROR")
        return
