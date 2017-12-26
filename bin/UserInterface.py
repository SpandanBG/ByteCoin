from tkinter import Tk, LEFT, RIGHT, SUNKEN, BOTTOM, BOTH, X, StringVar, BooleanVar
from tkinter.ttk import Button, Label, Entry, Checkbutton, Frame, Style

"""
This is the user interface class base on the Tkinter
"""
class UserInterface:
    """-------------------------- CONSTANTS"""
    _LEFT_MARGIN = -50
    _BOTTOM_MARGIN = -180
    width = 300
    height = 400
    _TITLE = "ByteCoin"
    _icon = "config/icon.ico"

    def __init__(self):
        self.root = Tk()
        return

    def set_manager(self, this):
        self.manager = this
        return

    def start_ui(self):
        self.root.iconbitmap(default=self._icon)
        self._dimen_setup()
        self._style_setup()

        self._mainframe()
        self._main_app()
        self._remainder_setup()
        self._final_setup()

        self.root.resizable(0, 0)
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.root.mainloop()

    def _on_closing(self):
        self.manager.stop()
        self.manager.join()
        self.root.destroy()
        return

    """-------------------------- UI HANDLERS"""
    def newX(self, x_value):
        self._cryptowatch_var.set(x_value)
        return

    def newY(self, y_value):
        self._coindelta_var.set(y_value)
        return

    def newZ(self, input_object):
        try:
            value = float(self._buy_rate_input.get())
            self.manager.setZ(value)
        except Exception as e:
            self._buy_rate_input.delete(0, END)
            # TODO: add console logging
        return

    def update_ratio(self, value):
        self._ratio_var.set("%.2f" % (value))
        return

    def update_processed_rate(self, value):
        self._process_var.set("%.2f" % (value))
        return

    def coin_select(self, id):
        for key in self._coin_select_set:
            if key == id:
                self._coin_select_set[key].set(True)
                self.manager.setM(id)
                self.manager.cancel_refresh()
                self.manager.refresh()
                self.error("CHANGING...")
            else:
                self._coin_select_set[key].set(False)
        return

    def error(self, message):
        self._extra_notify.set(message)
        return

    """-------------------------- PRIVATES SETUPS"""
    def _dimen_setup(self):
        _screen_width = self.root.winfo_screenwidth()
        _screen_height = self.root.winfo_screenheight()
        self._x_position = (_screen_width - self.width) + self._LEFT_MARGIN
        self._y_position = (_screen_height - self.height) + self._BOTTOM_MARGIN

    def _style_setup(self):
        self._style = Style()
        self._style.configure("LabelTheme.TLabel", background="#ffffff")
        return

    def _mainframe(self):
        self.app = Frame(self.root)
        self.app.master.geometry("%dx%d+%d+%d" % (self.width, self.height, self._x_position, self._y_position))
        self.app.master.title(self._TITLE)
        self.app.pack(fill=BOTH, expand=True)
        return

    def _main_app(self):
        self._app_main = Frame(self.app, relief=SUNKEN)#, style="App.TFrame")
        self._app_main.pack(fill=BOTH, expand=True)
        return

    def _remainder_setup(self):
        self._buy_rate_ui()
        self._refresh_ui()
        self._crycoin_ui()
        self._cryptowatch_ui()
        self._coindelta_ui()
        self._ratio_ui()
        self._processed_value_ui()

    def _final_setup(self):
        self._coin_select_set = {
            'BCH': self._bch_var,
            'ETH': self._eth_var,
            'LTC': self._ltc_var,
            'OMG': self._omg_var,
            'XRP': self._xrp_var,
        }
        self._coin_select_set['BCH'].set(True)
        self.manager.setN("BTC")
        self.manager.setM("BCH")
        self._refresh_data()
        return None

    """-------------------------- PRIVATE HANDLERS"""
    def _refresh_data(self):
        self.manager.cancel_refresh()
        self.manager.refresh()
        return

    """-------------------------- UI COMPONENTS"""
    def _refresh_ui(self):
        refresh_box = Frame(self._app_main)
        refresh_box.pack(fill=X, padx=10, pady=8)

        self._extra_notify = StringVar()
        extra_label = Label(refresh_box, textvariable=self._extra_notify)
        self._extra_notify.set("")
        extra_label.pack(side=LEFT)

        refresh_btn = Button(refresh_box, text="REFRESH", command=self._refresh_data)
        refresh_btn.pack(fill=X, side=RIGHT)
        return None

    def _crycoin_ui(self):
        coin_box = Frame(self._app_main)
        coin_box.pack(fill=X, padx=10, pady=10)

        self._bch_var = BooleanVar()
        bch_cb = Checkbutton(coin_box, text="BCH", variable=self._bch_var, onvalue=1, offvalue=0, command=lambda: self.coin_select("BCH"))
        bch_cb.pack(fill=X, side=LEFT)

        self._eth_var = BooleanVar()
        eth_cb = Checkbutton(coin_box, text="ETH", variable=self._eth_var, onvalue=1, offvalue=0, command=lambda: self.coin_select("ETH"))
        eth_cb.pack(fill=X, side=LEFT)

        self._ltc_var = BooleanVar()
        ltc_cb = Checkbutton(coin_box, text="LTC", variable=self._ltc_var, onvalue=1, offvalue=0, command=lambda: self.coin_select("LTC"))
        ltc_cb.pack(fill=X, side=LEFT)

        self._omg_var = BooleanVar()
        omg_cb = Checkbutton(coin_box, text="OMG", variable=self._omg_var, onvalue=1, offvalue=0, command=lambda: self.coin_select("OMG"))
        omg_cb.pack(fill=X, side=LEFT)

        self._xrp_var = BooleanVar()
        xrp_cb = Checkbutton(coin_box, text="XRP", variable=self._xrp_var, onvalue=1, offvalue=0, command=lambda: self.coin_select("XRP"))
        xrp_cb.pack(fill=X, side=LEFT)
        return

    def _cryptowatch_ui(self):
        cryptowatch_box = Frame(self._app_main)
        cryptowatch_box.pack(fill=X, padx=10, pady=5)

        cryptowatch_tag = Label(cryptowatch_box, text="EXCHANGE\nRATE")
        cryptowatch_tag.pack(side=LEFT)

        self._cryptowatch_var = StringVar()
        cryptowatch_entry = Label(cryptowatch_box, \
                                textvariable=self._cryptowatch_var, \
                                font="Helvetica 16", \
                                style='LabelTheme.TLabel', \
                                anchor="center", \
                                relief=SUNKEN)
        self._cryptowatch_var.set(0.00)
        cryptowatch_entry.pack(fill=X, expand=True, side=RIGHT, ipady=2)
        return

    def _coindelta_ui(self):
        coindelta_box = Frame(self._app_main)
        coindelta_box.pack(fill=X, padx=10, pady=5)

        coindelta_tag = Label(coindelta_box, text="BEST BID    ")
        coindelta_tag.pack(side=LEFT)

        self._coindelta_var = StringVar()
        coindelta_entry = Label(coindelta_box, \
                            textvariable=self._coindelta_var, \
                            font="Helvetica 16", \
                            style='LabelTheme.TLabel', \
                            anchor="center", \
                            relief=SUNKEN)
        self._coindelta_var.set(0.00)
        coindelta_entry.pack(fill=X, expand=True, side=RIGHT, ipady=2)
        return

    def _ratio_ui(self):
        ratio_box = Frame(self._app_main)
        ratio_box.pack(fill=X, padx=10, pady=10)

        ratio_tag = Label(ratio_box, text="RATIO", anchor="center")
        ratio_tag.pack(fill=X, side=BOTTOM)

        self._ratio_var = StringVar()
        ratio_entry = Label(ratio_box, \
                              textvariable=self._ratio_var, \
                              font="Helvetica 20", \
                              style='LabelTheme.TLabel', \
                              anchor="center", \
                            relief=SUNKEN)
        self._ratio_var.set(0.00)
        ratio_entry.pack(fill=X, ipady=12)
        return

    def _processed_value_ui(self):
        process_box = Frame(self._app_main)
        process_box.pack(fill=X, padx=12, pady=12)

        process_tag = Label(process_box, text="PROCESSED VALUE", anchor="center")
        process_tag.pack(fill=X, side=BOTTOM)

        self._process_var = StringVar()
        process_entry = Label(process_box, \
                              textvariable=self._process_var, \
                              font="Helvetica 20", \
                              style='LabelTheme.TLabel', \
                              anchor="center", \
                              relief=SUNKEN)
        self._process_var.set(0.00)
        process_entry.pack(fill=X, ipady=10)
        return

    def _buy_rate_ui(self):
        input_box = Frame(self.app, borderwidth=1)
        input_box.pack(fill=X, padx=5, pady=5)

        entry_label = Label(input_box, text="BUY RATE")
        entry_label.pack(side=LEFT)

        self._buy_rate_input = Entry(input_box)
        self._buy_rate_input.bind('<Return>', self.newZ)
        self._buy_rate_input.pack(fill=X, expand=True, side=RIGHT)
        return
