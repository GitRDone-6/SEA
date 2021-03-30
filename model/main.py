from model import sea
from gui import ui_stacked
from control import control

def main():
    """
    Initialize subsystems
    :return:
    """
    gui = ui_stacked.Ui_MainWindow()
    mod = sea.SEA()
    con = control.Controller()

    # Connect subsystems
    gui.set_model(mod)
    mod.set_controller(con)
    con.set_gui(gui)

    # start subsystems threads
    gui.start()
    mod.start()
    con.start()




if __name__ == '__main__':
    main()