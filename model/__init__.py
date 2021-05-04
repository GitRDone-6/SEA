import sys

from PyQt5.QtWidgets import QApplication

from model.sea import SEA
from control.control import Controller
from gui.ui_stacked import ThisWindow


def main():
    model = SEA()

    control = Controller()

    app = QApplication([])
    view = ThisWindow()

    view.ui_main.insert_model(model)
    control.insert_gui(view.ui_main)
    model.set_controller(control)

    view.ui_main.build_Tool_list_table()
    view.ui_main.build_scan_type_combobox()

    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

