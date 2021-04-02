# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stackediSjcyw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PyQt5 import Qt
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QAction, QWidget, QStackedWidget, QGridLayout, QSplitter, \
    QVBoxLayout, QStatusBar, QMenu, QMenuBar, QSizePolicy, QSpacerItem, QComboBox, QLineEdit, QLabel, QFrame, \
    QPlainTextEdit, QTableWidgetItem, QTableWidget, QTabWidget, QLayout, QMainWindow, QApplication
#from model import tool_configuration, sea
import threading

# from model import run_config

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *


class Ui_MainWindow(object):

#    __model: sea.SEA

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 751)
        self.action_tool = QAction(MainWindow)
        self.action_tool.setObjectName(u"action_tool")
        self.action_tool.triggered.connect(self.action_tool_on_click)
        self.actionRun_List = QAction(MainWindow)
        self.actionRun_List.setObjectName(u"actionRun_List")
        self.actionConfiguration_of_Runs = QAction(MainWindow)
        self.actionConfiguration_of_Runs.setObjectName(u"actionConfiguration_of_Runs")
        self.actionDetailed_Statistical_Data = QAction(MainWindow)
        self.actionDetailed_Statistical_Data.setObjectName(u"actionDetailed_Statistical_Data")
        self.actionXML_Report = QAction(MainWindow)
        self.actionXML_Report.setObjectName(u"actionXML_Report")
        self.action_run_list = QAction(MainWindow)
        self.action_run_list.setObjectName(u"action_run_list")
        self.action_run_list.triggered.connect(self.action_run_list_on_click)
        self.action_configuration_of_Run = QAction(MainWindow)
        self.action_configuration_of_Run.setObjectName(u"action_configuration_of_Run")
        self.action_configuration_of_Run.triggered.connect(self.action_configuration_of_run_on_click)
        self.action_detailed_specific_data = QAction(MainWindow)
        self.action_detailed_specific_data.setObjectName(u"action_detailed_specific_data")
        self.action_detailed_specific_data.triggered.connect(self.action_detailed_specific_data_on_click)
        self.action_xml_report_area = QAction(MainWindow)
        self.action_xml_report_area.setObjectName(u"action_xml_report_area")
        self.action_xml_report_area.triggered.connect(self.action_xml_report_area_on_click)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stacked_content_area = QStackedWidget(self.centralwidget)
        self.stacked_content_area.setObjectName(u"stacked_content_area")
        self.run_content_area = QWidget()
        self.run_content_area.setObjectName(u"run_content_area")
        self.horizontalLayout_2 = QHBoxLayout(self.run_content_area)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stacked_run_content_area = QStackedWidget(self.run_content_area)
        self.stacked_run_content_area.setObjectName(u"stacked_run_content_area")

        '''
        From this point most of the widgets we care about are below.
        '''

        self.run_list_area = QWidget()
        self.run_list_area.setObjectName(u"run_list_area")
        self.gridLayout = QGridLayout(self.run_list_area)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.run_list_area)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)


        self.table_run_list = QTableWidget(self.layoutWidget)
        if (self.table_run_list.columnCount() < 4):
            self.table_run_list.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_run_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_run_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_run_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_run_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_run_list.setObjectName(u"table_run_list")
        self.table_run_list.horizontalHeader().setVisible(False)
        self.table_run_list.horizontalHeader().setCascadingSectionResizes(True)
        self.table_run_list.horizontalHeader().setDefaultSectionSize(200)
        self.table_run_list.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_run_list.horizontalHeader().setStretchLastSection(True)
        self.table_run_list.verticalHeader().setProperty("showSortIndicator", False)
        self.table_run_list.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.table_run_list)

        self.button_add_run = QPushButton(self.layoutWidget)
        self.button_add_run.setObjectName(u"button_add_run")
        self.button_add_run.clicked.connect(self.button_add_run_on_click)

        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_add_run.setFont(font)

        self.verticalLayout.addWidget(self.button_add_run)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button_play_run = QPushButton(self.layoutWidget1)
        self.button_play_run.setObjectName(u"button_play_run")
        self.button_play_run.clicked.connect(self.button_play_run_on_click)
        self.button_play_run.setFont(font)

        self.horizontalLayout_3.addWidget(self.button_play_run)

        self.button_pause_run = QPushButton(self.layoutWidget1)
        self.button_pause_run.setObjectName(u"button_pause_run")
        self.button_pause_run.clicked.connect(self.button_pause_run_on_click)
        self.button_pause_run.setFont(font)

        self.horizontalLayout_3.addWidget(self.button_pause_run)

        self.button_stop_run = QPushButton(self.layoutWidget1)
        self.button_stop_run.setObjectName(u"button_stop_run")
        self.button_stop_run.clicked.connect(self.button_stop_run_on_click)
        self.button_stop_run.setFont(font)

        self.horizontalLayout_3.addWidget(self.button_stop_run)

        self.splitter.addWidget(self.layoutWidget1)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.label_3 = QLabel(self.run_list_area)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.stacked_run_content_area.addWidget(self.run_list_area)
        self.configuration_run_area = QWidget()
        self.configuration_run_area.setObjectName(u"configuration_run_area")
        self.gridLayout_2 = QGridLayout(self.configuration_run_area)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.splitter_4 = QSplitter(self.configuration_run_area)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.layoutWidget2 = QWidget(self.splitter_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_run_name = QLabel(self.layoutWidget2)
        self.label_run_name.setObjectName(u"label_run_name")

        self.verticalLayout_2.addWidget(self.label_run_name)

        self.textline_run_name = QLineEdit(self.layoutWidget2)
        self.textline_run_name.setObjectName(u"textline_run_name")

        self.verticalLayout_2.addWidget(self.textline_run_name)

        self.splitter_3.addWidget(self.layoutWidget2)
        self.layoutWidget3 = QWidget(self.splitter_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_run_desc = QLabel(self.layoutWidget3)
        self.label_run_desc.setObjectName(u"label_run_desc")

        self.verticalLayout_3.addWidget(self.label_run_desc)

        self.textbox_run_desc = QPlainTextEdit(self.layoutWidget3)
        self.textbox_run_desc.setObjectName(u"textbox_run_desc")

        self.verticalLayout_3.addWidget(self.textbox_run_desc)

        self.splitter_3.addWidget(self.layoutWidget3)
        self.splitter_4.addWidget(self.splitter_3)
        self.layoutWidget4 = QWidget(self.splitter_4)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_whitelist = QLabel(self.layoutWidget4)
        self.label_whitelist.setObjectName(u"label_whitelist")

        self.verticalLayout_5.addWidget(self.label_whitelist)

        self.textbox_whitelist = QPlainTextEdit(self.layoutWidget4)
        self.textbox_whitelist.setObjectName(u"textbox_whitelist")

        self.verticalLayout_5.addWidget(self.textbox_whitelist)

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_blacklist = QLabel(self.layoutWidget4)
        self.label_blacklist.setObjectName(u"label_blacklist")

        self.verticalLayout_7.addWidget(self.label_blacklist)

        self.textbox_blacklist = QPlainTextEdit(self.layoutWidget4)
        self.textbox_blacklist.setObjectName(u"textbox_blacklist")

        self.verticalLayout_7.addWidget(self.textbox_blacklist)

        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.splitter_4.addWidget(self.layoutWidget4)

        self.verticalLayout_8.addWidget(self.splitter_4)

        self.splitter_2 = QSplitter(self.configuration_run_area)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setFrameShape(QFrame.Box)
        self.splitter_2.setOrientation(Qt.Vertical)
        self.layoutWidget5 = QWidget(self.splitter_2)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dropdown_scantype = QComboBox(self.layoutWidget5)
        self.dropdown_scantype.setObjectName(u"dropdown_scantype")
        self.dropdown_scantype.setFont(font)
        self.dropdown_scantype.setEditable(True)

        self.verticalLayout_4.addWidget(self.dropdown_scantype)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.splitter_2.addWidget(self.layoutWidget5)
        self.label_or = QLabel(self.splitter_2)
        self.label_or.setObjectName(u"label_or")
        self.label_or.setFont(font)
        self.label_or.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.label_or)
        self.layoutWidget6 = QWidget(self.splitter_2)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.button_browse_config_file = QPushButton(self.layoutWidget6)
        self.button_browse_config_file.setObjectName(u"button_browse_config_file")
        self.button_browse_config_file.clicked.connect(self.button_browse_config_file_on_click)
        self.button_browse_config_file.setFont(font)

        self.verticalLayout_6.addWidget(self.button_browse_config_file)

        self.label_run_config_filename = QLabel(self.layoutWidget6)
        self.label_run_config_filename.setObjectName(u"label_run_config_filename")
        self.label_run_config_filename.setFrameShape(QFrame.Box)

        self.verticalLayout_6.addWidget(self.label_run_config_filename)

        self.splitter_2.addWidget(self.layoutWidget6)

        self.verticalLayout_8.addWidget(self.splitter_2)

        self.gridLayout_4.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.button_save_run_config = QPushButton(self.configuration_run_area)
        self.button_save_run_config.setObjectName(u"button_save_run_config")
        self.button_save_run_config.clicked.connect(self.button_save_run_config_on_click)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_save_run_config.sizePolicy().hasHeightForWidth())
        self.button_save_run_config.setSizePolicy(sizePolicy)
        self.button_save_run_config.setFont(font)

        self.horizontalLayout_6.addWidget(self.button_save_run_config)

        self.button_cancel_run_config = QPushButton(self.configuration_run_area)
        self.button_cancel_run_config.setObjectName(u"button_cancel_run_config")
        self.button_cancel_run_config.clicked.connect(self.button_cancel_run_config_on_click)
        sizePolicy.setHeightForWidth(self.button_cancel_run_config.sizePolicy().hasHeightForWidth())
        self.button_cancel_run_config.setSizePolicy(sizePolicy)
        self.button_cancel_run_config.setFont(font)

        self.horizontalLayout_6.addWidget(self.button_cancel_run_config)

        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.label_4 = QLabel(self.configuration_run_area)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.stacked_run_content_area.addWidget(self.configuration_run_area)
        self.detailed_run_area = QWidget()
        self.detailed_run_area.setObjectName(u"detailed_run_area")
        self.gridLayout_5 = QGridLayout(self.detailed_run_area)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter_5 = QSplitter(self.detailed_run_area)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.layoutWidget7 = QWidget(self.splitter_5)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)



        '''
        Statistical Data Table start
        '''
        self.table_statistical_data = QTableWidget(self.layoutWidget7)
        if (self.table_statistical_data.columnCount() < 7):
            self.table_statistical_data.setColumnCount(7)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_statistical_data.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_statistical_data.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_statistical_data.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_statistical_data.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_statistical_data.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_statistical_data.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_statistical_data.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        self.table_statistical_data.setObjectName(u"table_statistical_data")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_statistical_data.sizePolicy().hasHeightForWidth())
        self.table_statistical_data.setSizePolicy(sizePolicy1)
        self.table_statistical_data.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_statistical_data.horizontalHeader().setCascadingSectionResizes(True)
        self.table_statistical_data.horizontalHeader().setDefaultSectionSize(130)
        self.table_statistical_data.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_statistical_data.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_9.addWidget(self.table_statistical_data)
        '''
        Statistical Data Table end
        '''



        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.button_play_detailed_run = QPushButton(self.layoutWidget7)
        self.button_play_detailed_run.setObjectName(u"button_play_detailed_run")
        self.button_play_detailed_run.clicked.connect(self.button_play_detailed_run_on_click)
        self.button_play_detailed_run.setFont(font)

        self.horizontalLayout_7.addWidget(self.button_play_detailed_run)

        self.button_pause_detailed_run = QPushButton(self.layoutWidget7)
        self.button_pause_detailed_run.setObjectName(u"button_pause_detailed_run")
        self.button_pause_detailed_run.clicked.connect(self.button_pause_detailed_run_on_click)
        self.button_pause_detailed_run.setFont(font)

        self.horizontalLayout_7.addWidget(self.button_pause_detailed_run)

        self.button_stop_detailed_run = QPushButton(self.layoutWidget7)
        self.button_stop_detailed_run.setObjectName(u"button_stop_detailed_run")
        self.button_stop_detailed_run.clicked.connect(self.button_stop_detailed_run_on_click)
        self.button_stop_detailed_run.setFont(font)

        self.horizontalLayout_7.addWidget(self.button_stop_detailed_run)

        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.splitter_5.addWidget(self.layoutWidget7)
        self.tab_scan_result_area = QTabWidget(self.splitter_5)
        self.tab_scan_result_area.setObjectName(u"tab_scan_result_area")
        self.splitter_5.addWidget(self.tab_scan_result_area)

        self.gridLayout_5.addWidget(self.splitter_5, 0, 0, 1, 1)

        self.stacked_run_content_area.addWidget(self.detailed_run_area)
        self.xml_report_area = QWidget()
        self.xml_report_area.setObjectName(u"xml_report_area")
        self.gridLayout_6 = QGridLayout(self.xml_report_area)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_report_name = QLabel(self.xml_report_area)
        self.label_report_name.setObjectName(u"label_report_name")

        self.verticalLayout_10.addWidget(self.label_report_name)

        self.textline_report_name = QLineEdit(self.xml_report_area)
        self.textline_report_name.setObjectName(u"textline_report_name")

        self.verticalLayout_10.addWidget(self.textline_report_name)

        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_report_desc = QLabel(self.xml_report_area)
        self.label_report_desc.setObjectName(u"label_report_desc")

        self.verticalLayout_11.addWidget(self.label_report_desc)

        self.textbox_report_desc = QPlainTextEdit(self.xml_report_area)
        self.textbox_report_desc.setObjectName(u"textbox_report_desc")

        self.verticalLayout_11.addWidget(self.textbox_report_desc)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_16.addLayout(self.verticalLayout_12)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.dropbox_run_pair = QComboBox(self.xml_report_area)
        self.dropbox_run_pair.setObjectName(u"dropbox_run_pair")
        self.dropbox_run_pair.setFont(font)
        self.dropbox_run_pair.setEditable(True)

        self.verticalLayout_14.addWidget(self.dropbox_run_pair)

        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.dropbox_scan_duel = QComboBox(self.xml_report_area)
        self.dropbox_scan_duel.setObjectName(u"dropbox_scan_duel")
        self.dropbox_scan_duel.setFont(font)
        self.dropbox_scan_duel.setEditable(True)

        self.verticalLayout_15.addWidget(self.dropbox_scan_duel)

        self.horizontalLayout_8.addLayout(self.verticalLayout_15)

        self.button_remove_report = QPushButton(self.xml_report_area)
        self.button_remove_report.setObjectName(u"button_remove_report")
        self.button_remove_report.clicked.connect(self.button_remove_report_on_click)
        self.button_remove_report.setFont(font)

        self.horizontalLayout_8.addWidget(self.button_remove_report)

        self.verticalLayout_19.addLayout(self.horizontalLayout_8)

        self.label_or_2 = QLabel(self.xml_report_area)
        self.label_or_2.setObjectName(u"label_or_2")
        self.label_or_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_or_2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.dropbox_run_solo = QComboBox(self.xml_report_area)
        self.dropbox_run_solo.setObjectName(u"dropbox_run_solo")
        self.dropbox_run_solo.setFont(font)
        self.dropbox_run_solo.setEditable(True)

        self.verticalLayout_13.addWidget(self.dropbox_run_solo)

        self.verticalLayout_19.addLayout(self.verticalLayout_13)

        self.verticalLayout_16.addLayout(self.verticalLayout_19)

        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.button_add_report = QPushButton(self.xml_report_area)
        self.button_add_report.setObjectName(u"button_add_report")
        self.button_add_report.clicked.connect(self.button_add_report_on_click)
        self.button_add_report.setFont(font)

        self.horizontalLayout_10.addWidget(self.button_add_report)

        self.button_generate_report = QPushButton(self.xml_report_area)
        self.button_generate_report.setObjectName(u"button_generate_report")
        self.button_generate_report.clicked.connect(self.button_generate_report_on_click)
        self.button_generate_report.setFont(font)

        self.horizontalLayout_10.addWidget(self.button_generate_report)

        self.button_cancel_report = QPushButton(self.xml_report_area)
        self.button_cancel_report.setObjectName(u"button_cancel_report")
        self.button_cancel_report.clicked.connect(self.button_cancel_report_on_click)
        self.button_cancel_report.setFont(font)

        self.horizontalLayout_10.addWidget(self.button_cancel_report)

        self.verticalLayout_17.addLayout(self.horizontalLayout_10)

        self.gridLayout_6.addLayout(self.verticalLayout_17, 1, 0, 1, 1)

        self.label = QLabel(self.xml_report_area)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.stacked_run_content_area.addWidget(self.xml_report_area)

        self.horizontalLayout_2.addWidget(self.stacked_run_content_area)

        self.stacked_content_area.addWidget(self.run_content_area)
        self.tool_content_area = QWidget()
        self.tool_content_area.setObjectName(u"tool_content_area")
        self.gridLayout_3 = QGridLayout(self.tool_content_area)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stacked_tool_content_area = QStackedWidget(self.tool_content_area)
        self.stacked_tool_content_area.setObjectName(u"stacked_tool_content_area")
        self.stacked_tool_content_area.setFont(font)
        self.tool_list_area = QWidget()
        self.tool_list_area.setObjectName(u"tool_list_area")
        self.gridLayout_7 = QGridLayout(self.tool_list_area)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.splitter_9 = QSplitter(self.tool_list_area)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setFrameShape(QFrame.WinPanel)
        self.splitter_9.setOrientation(Qt.Horizontal)
        self.layoutWidget8 = QWidget(self.splitter_9)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.tool_list_title = QLabel(self.layoutWidget8)
        self.tool_list_title.setObjectName(u"tool_list_title")
        self.tool_list_title.setFont(font)
        self.tool_list_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.tool_list_title)

        self.tableWidget = QTableWidget(self.layoutWidget8)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_20.addWidget(self.tableWidget)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushbutton_add_tool = QPushButton(self.layoutWidget8)
        self.pushbutton_add_tool.setObjectName(u"pushbutton_add_tool")
        self.pushbutton_add_tool.clicked.connect(self.pushbutton_add_tool_on_click)

        self.horizontalLayout_9.addWidget(self.pushbutton_add_tool)

        self.pushbutton_delete_tool = QPushButton(self.layoutWidget8)
        self.pushbutton_delete_tool.setObjectName(u"pushbutton_delete_tool")
        self.pushbutton_delete_tool.clicked.connect(self.pushbutton_delete_tool_on_click)

        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushbutton_delete_tool.setFont(font1)

        self.horizontalLayout_9.addWidget(self.pushbutton_delete_tool)

        self.pushbutton_move_up = QPushButton(self.layoutWidget8)
        self.pushbutton_move_up.setObjectName(u"pushbutton_move_up")
        self.pushbutton_move_up.clicked.connect(self.pushbutton_move_up_on_click)

        self.horizontalLayout_9.addWidget(self.pushbutton_move_up)

        self.pushbutton_move_down = QPushButton(self.layoutWidget8)
        self.pushbutton_move_down.setObjectName(u"pushbutton_move_down")
        self.pushbutton_move_down.clicked.connect(self.pushbutton_move_down_on_click)

        self.horizontalLayout_9.addWidget(self.pushbutton_move_down)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.verticalLayout_20.addLayout(self.horizontalLayout_9)

        self.splitter_9.addWidget(self.layoutWidget8)
        self.splitter_8 = QSplitter(self.splitter_9)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Vertical)
        self.tool_specification_label = QLabel(self.splitter_8)
        self.tool_specification_label.setObjectName(u"tool_specification_label")
        self.tool_specification_label.setAlignment(Qt.AlignCenter)
        self.splitter_8.addWidget(self.tool_specification_label)
        self.layoutWidget9 = QWidget(self.splitter_8)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.splitter_7 = QSplitter(self.layoutWidget9)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setFrameShape(QFrame.Box)
        self.splitter_7.setOrientation(Qt.Vertical)
        self.layoutWidget10 = QWidget(self.splitter_7)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_tool_name = QLabel(self.layoutWidget10)
        self.label_tool_name.setObjectName(u"label_tool_name")

        self.horizontalLayout_13.addWidget(self.label_tool_name)

        self.lineedit_tool_name = QLineEdit(self.layoutWidget10)
        self.lineedit_tool_name.setObjectName(u"lineedit_tool_name")

        self.horizontalLayout_13.addWidget(self.lineedit_tool_name)

        self.splitter_7.addWidget(self.layoutWidget10)
        self.layoutWidget11 = QWidget(self.splitter_7)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_tool_description = QLabel(self.layoutWidget11)
        self.label_tool_description.setObjectName(u"label_tool_description")

        self.horizontalLayout_14.addWidget(self.label_tool_description)

        self.plaintextedit_tool_description = QPlainTextEdit(self.layoutWidget11)
        self.plaintextedit_tool_description.setObjectName(u"plaintextedit_tool_description")

        self.horizontalLayout_14.addWidget(self.plaintextedit_tool_description)

        self.splitter_7.addWidget(self.layoutWidget11)
        self.layoutWidget12 = QWidget(self.splitter_7)
        self.layoutWidget12.setObjectName(u"layoutWidget12")
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_tool_path = QLabel(self.layoutWidget12)
        self.label_tool_path.setObjectName(u"label_tool_path")

        self.horizontalLayout_15.addWidget(self.label_tool_path)

        self.lineedit_tool_path = QLineEdit(self.layoutWidget12)
        self.lineedit_tool_path.setObjectName(u"lineedit_tool_path")

        self.horizontalLayout_15.addWidget(self.lineedit_tool_path)

        self.button_tool_path_browse = QPushButton(self.layoutWidget12)
        self.button_tool_path_browse.setObjectName(u"button_tool_path_browse")
        self.button_tool_path_browse.clicked.connect(self.button_tool_path_browse_on_click)

        self.horizontalLayout_15.addWidget(self.button_tool_path_browse)

        self.splitter_7.addWidget(self.layoutWidget12)
        self.layoutWidget13 = QWidget(self.splitter_7)
        self.layoutWidget13.setObjectName(u"layoutWidget13")
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_option_argument = QLabel(self.layoutWidget13)
        self.label_option_argument.setObjectName(u"label_option_argument")

        self.horizontalLayout_16.addWidget(self.label_option_argument)

        self.plaintextedit_tool_option_argument = QPlainTextEdit(self.layoutWidget13)
        self.plaintextedit_tool_option_argument.setObjectName(u"plaintextedit_tool_option_argument")

        self.horizontalLayout_16.addWidget(self.plaintextedit_tool_option_argument)

        self.button_option_argument_add = QPushButton(self.layoutWidget13)
        self.button_option_argument_add.setObjectName(u"button_option_argument_add")
        self.button_option_argument_add.clicked.connect(self.button_option_argument_add_on_click)

        self.horizontalLayout_16.addWidget(self.button_option_argument_add)

        self.splitter_7.addWidget(self.layoutWidget13)
        self.layoutWidget14 = QWidget(self.splitter_7)
        self.layoutWidget14.setObjectName(u"layoutWidget14")
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_output_data = QLabel(self.layoutWidget14)
        self.label_output_data.setObjectName(u"label_output_data")

        self.horizontalLayout_17.addWidget(self.label_output_data)

        self.plaintextedit_tool_data_specification = QPlainTextEdit(self.layoutWidget14)
        self.plaintextedit_tool_data_specification.setObjectName(u"plaintextedit_tool_data_specification")

        self.horizontalLayout_17.addWidget(self.plaintextedit_tool_data_specification)

        self.button_output_data_add = QPushButton(self.layoutWidget14)
        self.button_output_data_add.setObjectName(u"button_output_data_add")
        self.button_output_data_add.clicked.connect(self.button_output_data_add_on_click)

        self.horizontalLayout_17.addWidget(self.button_output_data_add)

        self.splitter_7.addWidget(self.layoutWidget14)

        self.verticalLayout_21.addWidget(self.splitter_7)

        self.pushbutton_export_tool_spec_file = QPushButton(self.layoutWidget9)
        self.pushbutton_export_tool_spec_file.setObjectName(u"pushbutton_export_tool_spec_file")
        self.pushbutton_export_tool_spec_file.clicked.connect(self.pushbutton_export_tool_spec_file_on_click)

        self.verticalLayout_21.addWidget(self.pushbutton_export_tool_spec_file)

        self.tool_specification_OR_label = QLabel(self.layoutWidget9)
        self.tool_specification_OR_label.setObjectName(u"tool_specification_OR_label")
        self.tool_specification_OR_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.tool_specification_OR_label)

        self.splitter_6 = QSplitter(self.layoutWidget9)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setFrameShape(QFrame.Box)
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.tool_specification_file_input = QLineEdit(self.splitter_6)
        self.tool_specification_file_input.setObjectName(u"tool_specification_file_input")
        self.splitter_6.addWidget(self.tool_specification_file_input)
        self.tool_specification_browse_button = QPushButton(self.splitter_6)
        self.tool_specification_browse_button.setObjectName(u"tool_specification_browse_button")
        self.tool_specification_browse_button.clicked.connect(self.tool_specification_browse_button_on_click)
        self.splitter_6.addWidget(self.tool_specification_browse_button)

        self.verticalLayout_21.addWidget(self.splitter_6)

        self.splitter_8.addWidget(self.layoutWidget9)
        self.layoutWidget15 = QWidget(self.splitter_8)
        self.layoutWidget15.setObjectName(u"layoutWidget15")
        self.verticalLayout_18 = QVBoxLayout(self.layoutWidget15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_3)

        self.tool_dependency_label = QLabel(self.layoutWidget15)
        self.tool_dependency_label.setObjectName(u"tool_dependency_label")
        self.tool_dependency_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.tool_dependency_label)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_2 = QLabel(self.layoutWidget15)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_12.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.layoutWidget15)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_12.addWidget(self.lineEdit)

        self.verticalLayout_18.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.value_text = QLineEdit(self.layoutWidget15)
        self.value_text.setObjectName(u"value_text")

        self.horizontalLayout_11.addWidget(self.value_text)

        self.dependent_data_drop_down_2 = QComboBox(self.layoutWidget15)
        self.dependent_data_drop_down_2.addItem("")
        self.dependent_data_drop_down_2.addItem("")
        self.dependent_data_drop_down_2.setObjectName(u"dependent_data_drop_down_2")

        self.horizontalLayout_11.addWidget(self.dependent_data_drop_down_2)

        self.dependent_data_drop_down = QComboBox(self.layoutWidget15)
        self.dependent_data_drop_down.addItem("")
        self.dependent_data_drop_down.addItem("")
        self.dependent_data_drop_down.setObjectName(u"dependent_data_drop_down")

        self.horizontalLayout_11.addWidget(self.dependent_data_drop_down)

        self.dependency_remove_button = QPushButton(self.layoutWidget15)
        self.dependency_remove_button.setObjectName(u"dependency_remove_button")
        self.dependency_remove_button.clicked.connect(self.dependency_remove_button_on_click)

        self.horizontalLayout_11.addWidget(self.dependency_remove_button)

        self.verticalLayout_18.addLayout(self.horizontalLayout_11)

        self.pushbutton_add_tool_specification = QPushButton(self.layoutWidget15)
        self.pushbutton_add_tool_specification.setObjectName(u"pushbutton_add_tool_specification")
        self.pushbutton_add_tool_specification.clicked.connect(self.pushbutton_add_tool_specification_on_click)

        self.verticalLayout_18.addWidget(self.pushbutton_add_tool_specification)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)

        self.cancel_save_layout = QHBoxLayout()
        self.cancel_save_layout.setObjectName(u"cancel_save_layout")
        self.save_button = QPushButton(self.layoutWidget15)
        self.save_button.setObjectName(u"save_button")
        self.save_button.clicked.connect(self.save_button_on_click)

        self.cancel_save_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton(self.layoutWidget15)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.clicked.connect(self.cancel_button_on_click)

        self.cancel_save_layout.addWidget(self.cancel_button)

        self.verticalLayout_18.addLayout(self.cancel_save_layout)

        self.splitter_8.addWidget(self.layoutWidget15)
        self.splitter_9.addWidget(self.splitter_8)

        self.gridLayout_7.addWidget(self.splitter_9, 0, 0, 1, 1)

        self.stacked_tool_content_area.addWidget(self.tool_list_area)
        self.detailed_tool_area = QWidget()
        self.detailed_tool_area.setObjectName(u"detailed_tool_area")
        self.stacked_tool_content_area.addWidget(self.detailed_tool_area)

        self.gridLayout_3.addWidget(self.stacked_tool_content_area, 0, 1, 1, 1)

        self.stacked_content_area.addWidget(self.tool_content_area)

        self.horizontalLayout.addWidget(self.stacked_content_area)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 24))
        self.menuSEA_Menu = QMenu(self.menubar)
        self.menuSEA_Menu.setObjectName(u"menuSEA_Menu")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSEA_Menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSEA_Menu.addAction(self.action_run_list)
        self.menuSEA_Menu.addAction(self.action_configuration_of_Run)
        self.menuSEA_Menu.addAction(self.action_detailed_specific_data)
        self.menuSEA_Menu.addAction(self.action_xml_report_area)
        self.menuSEA_Menu.addSeparator()
        self.menuSEA_Menu.addAction(self.action_tool)

        self.retranslateUi(MainWindow)

        self.stacked_content_area.setCurrentIndex(0)
        self.stacked_run_content_area.setCurrentIndex(1)
        self.tab_scan_result_area.setCurrentIndex(2)
        self.stacked_tool_content_area.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    def add_scan_tab(self, tool_name: str):
        # TODO Find out how to make a layout for the tab widgets under tab_scan_result_area
        # TODO Set the widget to contain a text area that can be written to by programming but not by the GUI
        # TODO Find out how to generate the tabs during runtime. This should be done through the control.
        # TODO Learn how to start the tools and force the output to go into the non-writting area.
        # Refer to 396 and 1001
        '''
        self.add_scan_tab()
        self.example_scan_output_1 = QWidget()
        self.example_scan_output_1.setObjectName(u"example_scan_output_1")
        self.tab_scan_result_area.addTab(self.example_scan_output_1, "")
        self.example_scan_output_2 = QWidget()
        self.example_scan_output_2.setObjectName(u"example_scan_output_2")
        self.tab_scan_result_area.addTab(self.example_scan_output_2, "")
        self.example_scan_output_3 = QWidget()
        self.example_scan_output_3.setObjectName(u"example_scan_output_3")
        self.tab_scan_result_area.addTab(self.example_scan_output_3, "")
        :param tool_name:
        '''

        new_scan_output_tab = QWidget()
        new_scan_output_tab.setObjectName(tool_name)
        self.tab_scan_result_area.addTab(new_scan_output_tab)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_tool.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.actionRun_List.setText(QCoreApplication.translate("MainWindow", u"Run List", None))
        self.actionConfiguration_of_Runs.setText(
            QCoreApplication.translate("MainWindow", u"Configuration of Runs", None))
        self.actionDetailed_Statistical_Data.setText(
            QCoreApplication.translate("MainWindow", u"Detailed Statistical Data", None))
        self.actionXML_Report.setText(QCoreApplication.translate("MainWindow", u"XML Report", None))
        self.action_run_list.setText(QCoreApplication.translate("MainWindow", u"Run List", None))
        self.action_configuration_of_Run.setText(QCoreApplication.translate("MainWindow", u"Configuration of Run", None))
        self.action_detailed_specific_data.setText(
            QCoreApplication.translate("MainWindow", u"Detailed Statistical Data", None))
        self.action_xml_report_area.setText(QCoreApplication.translate("MainWindow", u"XML Report", None))
        ___qtablewidgetitem = self.table_run_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name of Run \u21f5", None));
        ___qtablewidgetitem1 = self.table_run_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Description of Run", None));
        ___qtablewidgetitem2 = self.table_run_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Result with Timestamp", None));
        ___qtablewidgetitem3 = self.table_run_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Control Status", None));
        self.button_add_run.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_play_run.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.button_pause_run.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.button_stop_run.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Run List</span></p></body></html>",
                                                        None))
        self.label_run_name.setText(QCoreApplication.translate("MainWindow",
                                                               u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Run Name</span></p></body></html>",
                                                               None))
        self.label_run_desc.setText(QCoreApplication.translate("MainWindow",
                                                               u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Run Description</span></p></body></html>",
                                                               None))
        self.label_whitelist.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Whitelisted IP Target</span></p></body></html>",
                                                                None))
        self.label_blacklist.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Blacklisted IP Target</span></p></body></html>",
                                                                None))
        self.dropdown_scantype.setCurrentText(QCoreApplication.translate("MainWindow", u"Scan Type", None))
        self.label_or.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.button_browse_config_file.setText(
            QCoreApplication.translate("MainWindow", u"Run Configuration File...", None))
        self.label_run_config_filename.setText(QCoreApplication.translate("MainWindow",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">example_run_config.xml</span></p></body></html>",
                                                                          None))
        self.button_save_run_config.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.button_cancel_run_config.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Configuration of the Selected Run</span></p></body></html>",
                                                        None))
        ___qtablewidgetitem4 = self.table_statistical_data.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Name of Scan \u21f5", None));
        ___qtablewidgetitem5 = self.table_statistical_data.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Execution Number \u21f5", None));
        ___qtablewidgetitem6 = self.table_statistical_data.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Start Time \u21f5", None));
        ___qtablewidgetitem7 = self.table_statistical_data.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"End Time \u21f5", None));
        ___qtablewidgetitem8 = self.table_statistical_data.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Scanned IPs", None));
        ___qtablewidgetitem9 = self.table_statistical_data.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Successful Execution/Failure", None));
        ___qtablewidgetitem10 = self.table_statistical_data.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Control Status", None));
        self.button_play_detailed_run.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.button_pause_detailed_run.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.button_stop_detailed_run.setText(QCoreApplication.translate("MainWindow", u"Stop", None))



        # TODO we also need to update this adding text part. It needs to write the names of the tabs. It seems
        # that the ui doesn't need to be "refreshed" as it should update on its own.
        '''
        There perhaps should be a method to call so that it may update the text of the tab that was just created.
        '''
        self.update_tab_text()




        self.label_report_name.setText(QCoreApplication.translate("MainWindow",
                                                                  u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Report Name</span></p></body></html>",
                                                                  None))
        self.label_report_desc.setText(QCoreApplication.translate("MainWindow",
                                                                  u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Report Description</span></p></body></html>",
                                                                  None))
        self.dropbox_run_pair.setCurrentText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.dropbox_scan_duel.setCurrentText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.button_remove_report.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_or_2.setText(QCoreApplication.translate("MainWindow",
                                                           u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">OR</span></p></body></html>",
                                                           None))
        self.dropbox_run_solo.setCurrentText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.button_add_report.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_generate_report.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.button_cancel_report.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">XML Report</span></p></body></html>",
                                                      None))
        self.tool_list_title.setText(QCoreApplication.translate("MainWindow", u"Tool List", None))
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Name of Tool \u21f5", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Description of Tool", None));
        self.pushbutton_add_tool.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushbutton_delete_tool.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushbutton_move_up.setText(QCoreApplication.translate("MainWindow", u"\u1431", None))
        self.pushbutton_move_down.setText(QCoreApplication.translate("MainWindow", u"\u142f", None))
        self.tool_specification_label.setText(QCoreApplication.translate("MainWindow", u"Tool Specification", None))
        self.label_tool_name.setText(QCoreApplication.translate("MainWindow", u"Tool Name: ", None))
        self.label_tool_description.setText(QCoreApplication.translate("MainWindow", u"Tool Description:", None))
        self.label_tool_path.setText(QCoreApplication.translate("MainWindow", u"Tool Path:", None))
        self.button_tool_path_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_option_argument.setText(QCoreApplication.translate("MainWindow", u"Option and Argument: ", None))
        self.button_option_argument_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_output_data.setText(QCoreApplication.translate("MainWindow", u"Output Data Specification: ", None))
        self.button_output_data_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushbutton_export_tool_spec_file.setText(
            QCoreApplication.translate("MainWindow", u"Export as Tool Specification File...", None))
        self.tool_specification_OR_label.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.tool_specification_file_input.setText("")
        self.tool_specification_file_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Tool Specification File", None))
        self.tool_specification_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.tool_dependency_label.setText(QCoreApplication.translate("MainWindow", u"Tool Dependency", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dependency Expression: ", None))
        self.value_text.setText("")
        self.value_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.dependent_data_drop_down_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Operator", None))
        self.dependent_data_drop_down_2.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.dependent_data_drop_down.setItemText(0, QCoreApplication.translate("MainWindow", u"Dependent Data", None))
        self.dependent_data_drop_down.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.dependency_remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushbutton_add_tool_specification.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.menuSEA_Menu.setTitle(QCoreApplication.translate("MainWindow", u"SEA Menu", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

    def update_tab_text(self):
        """
        Responsible for updating the tabs. Maybe a data structure that adding tabs method may also call.
        TODO This should be callable from the control so that it may update with the scans.
        :return:
        self.tab_scan_result_area.setTabText(self.tab_scan_result_area.indexOf(self.example_scan_output_1),
                                             QCoreApplication.translate("MainWindow", u"Name of Scan 1", None))
        self.tab_scan_result_area.setTabText(self.tab_scan_result_area.indexOf(self.example_scan_output_2),
                                             QCoreApplication.translate("MainWindow", u"...", None))
        self.tab_scan_result_area.setTabText(self.tab_scan_result_area.indexOf(self.example_scan_output_3),
                                             QCoreApplication.translate("MainWindow", u">>", None))
        """


    # retranslateUi

    def action_run_list_on_click(self):
        # Set to run side
        self.stacked_content_area.setCurrentIndex(0)
        # Set to run list
        self.stacked_run_content_area.setCurrentIndex(0)

    def action_configuration_of_run_on_click(self):
        # Set to run side
        self.stacked_content_area.setCurrentIndex(0)
        # Set to run configuration
        self.stacked_run_content_area.setCurrentIndex(1)

    def action_detailed_specific_data_on_click(self):
        # Set to run side
        self.stacked_content_area.setCurrentIndex(0)
        # Set to detailed speicic data
        self.stacked_run_content_area.setCurrentIndex(2)

    def action_xml_report_area_on_click(self):
        # Set to run side
        self.stacked_content_area.setCurrentIndex(0)
        # set to xml report area
        self.stacked_run_content_area.setCurrentIndex(3)

    def action_tool_on_click(self):
        # Set to tool side
        self.stacked_content_area.setCurrentIndex(1)

    def pushbutton_add_tool_on_click(self):
        # TODO add implementation
        print('pushbutton_add_tool_on_click')

    def pushbutton_delete_tool_on_click(self):
        # TODO add implementation
        print('pushbutton_delete_tool_on_click')

    def pushbutton_move_down_on_click(self):
        # TODO add implementation
        print('pushbutton_move_down_on_click')

    def pushbutton_move_up_on_click(self):
        # TODO add implementation
        print('pushbutton_move_up_on_click')

    def button_tool_path_browse_on_click(self):
        # TODO add implementation
        print('button_tool_path_browse_on_click')

    def button_option_argument_add_on_click(self):
        # TODO add implementation
        print('button_option_argument_add_on_click')

    def button_output_data_add_on_click(self):
        # TODO add implementation
        print('button_output_data_add_on_click')

    def pushbutton_export_tool_spec_file_on_click(self):
        # TODO add implementation
        print('pushbutton_export_tool_spec_file_on_click')

    def tool_specification_browse_button_on_click(self):
        # TODO add implementation
        print('tool_specification_browse_button_on_click')

    def dependency_remove_button_on_click(self):
        # TODO add implementation
        print('dependency_remove_button_on_click')

    def pushbutton_add_tool_specification_on_click(self):
        # TODO add implementation
        print('pushbutton_add_tool_specification_on_click')

    def save_button_on_click(self):
        # TODO add implementation
        #tool_configuration.ToolConfiguration.save_config()
        print('save_button_on_click')

    def cancel_button_on_click(self):
        # TODO add implementation
        print('cancel_button_on_click')

    def button_play_detailed_run_on_click(self):
        # TODO add implementation
        print('button_play_detailed_run_on_click')

    def button_pause_detailed_run_on_click(self):
        # TODO add implementation
        print('button_pause_detailed_run_on_click')

    def button_stop_detailed_run_on_click(self):
        # TODO add implementation
        print('button_stop_detailed_run_on_click')

    def button_remove_report_on_click(self):
        # TODO add implementation
        print('button_remove_report_on_click')

    def button_add_report_on_click(self):
        # TODO add implementation
        print('button_add_report_on_click')

    def button_cancel_report_on_click(self):
        # TODO add implementation
        print('button_cancel_report_on_click')

    def button_generate_report_on_click(self):
        # TODO add implementation
        print('button_generate_report_on_click')

    def button_add_run_on_click(self):
        # TODO add implementation
        print('button_add_run_on_click')

    def button_pause_run_on_click(self):
        # TODO add implementation
        print('button_pause_run_on_click')

    def button_play_run_on_click(self):
        # TODO add implementation
        print('button_play_run_on_click')

    def button_stop_run_on_click(self):
        # TODO add implementation
        print('button_stop_run_on_click')

    def button_browse_config_file_on_click(self):
        # TODO add implementation
        print('button_browse_config_file_on_click')

    def button_save_run_config_on_click(self):
        # TODO add implementation
        print('button_save_run_config_on_click')

    def button_cancel_run_config_on_click(self):
        # TODO add implementation
        print('button_cancel_run_config_on_click')

    '''
    def set_model(self, mod: sea.SEA):
        self.__model = mod
        pass
    '''

    def run(self):
        pass

    def start(self):
        app = QApplication([])
        application = ThisWindow()
        application.show()
        sys.exit(app.exec())


class ThisWindow(QMainWindow):

    def __init__(self):
        super(ThisWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    application = ThisWindow()
    application.show()
    sys.exit(app.exec())
