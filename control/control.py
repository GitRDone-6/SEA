from gui import ui_stacked

class Controller:

    def __init__(self, view: ui_stacked.Ui_MainWindow):
        self.__view = view



    def add_more_tabs(self) -> None:
        """
        Supposed to add more tabs to the scan tabs under Detailed View.

        Instead of extracting the code to add the actual widgets into the tab widgets, request the gui to do it
        and just provide the information it needs.

        use s
        :return:
        """
        # self.__view.add_scan_tab() <--- use this


        self.example_scan_output_1 = QWidget()
        self.example_scan_output_1.setObjectName(u"example_scan_output_1")
        self.tab_scan_result_area.addTab(self.example_scan_output_1, "")
        self.example_scan_output_2 = QWidget()
        self.example_scan_output_2.setObjectName(u"example_scan_output_2")
        self.tab_scan_result_area.addTab(self.example_scan_output_2, "")
        self.example_scan_output_3 = QWidget()
        self.example_scan_output_3.setObjectName(u"example_scan_output_3")
        self.tab_scan_result_area.addTab(self.example_scan_output_3, "")