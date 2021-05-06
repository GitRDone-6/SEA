import sys

from PyQt5.QtWidgets import QApplication

from model.sea import SEA
from control.control import Controller
from gui.ui_stacked import ThisWindow

def main():

    #Make Model
    model = SEA()

    #Make Control
    control = Controller()

    #Make GUI
    app = QApplication([])
    view = ThisWindow()

    #Connect the three subsystems
    view.ui_main.insert_model(model)
    control.insert_gui(view.ui_main)
    model.set_controller(control)

    #Other important building calls for view
    view.ui_main.build_Tool_list_table()
    view.ui_main.build_scan_type_combobox()
    view.ui_main.update_table_run_list()



    view.show()
    #model.join()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

