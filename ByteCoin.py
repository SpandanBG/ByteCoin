#!/usr/bin/python3
from bin import UserInterface as UI, Manager as MG

def main():
    try:
        ui = UI.UserInterface()
        mg = MG.Manager()

        ui.set_manager(mg)
        mg.set_ui_thread(ui)

        mg.start()
        ui.start_ui()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
