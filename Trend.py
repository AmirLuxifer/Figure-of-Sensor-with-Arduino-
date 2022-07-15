# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GAZ4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import codecs
import csv
import glob
import os
import shutil
import sys
import sqlite3
import datetime as dt
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog, QApplication
from pyqtgraph import PlotWidget
import winsound
import SeePast

with open('com.txt', 'r') as f:
    COMI = f.readline()

ser = serial.Serial(COMI, 115200, timeout=0.1)
ser.close()
ser.open()
Rename_time_file = [dt.datetime.now().strftime('%Y-%m-%d %H.%M.%S')]
DataSinglePlot = [0]
DataSinglePlot2 = [0]
DataSinglePlot3 = [0]
DataSinglePlot4 = [0]
DataMergePlot = [0]
DataMergePlot2 = [0]
DataMergePlot3 = [0]
DataMergePlot4 = [0]


def view():
    conn = sqlite3.connect("name4.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def update(id, R, G, B):
    conn = sqlite3.connect("name4.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET R=?,G=?,B=? WHERE id=?", (R, G, B, id))
    conn.commit()
    conn.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global SingleGraph1, SingleGraph2, SingleGraph3, SingleGraph4
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1272, 832)
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_setting = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_setting.setStyleSheet("font: 11pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.comboBox_setting.setObjectName("comboBox_setting")
        self.comboBox_setting.addItem("")
        self.comboBox_setting.addItem("")
        self.comboBox_setting.addItem("")
        self.comboBox_setting.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_setting, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 8, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 7, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.Save_Setting_buttom_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Save_Setting_buttom_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Save_Setting_buttom_1.setMouseTracking(False)
        self.Save_Setting_buttom_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Save_Setting_buttom_1.setAcceptDrops(False)
        self.Save_Setting_buttom_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "font: 11pt \"Tahoma\";\n"
                                                 "background-color: rgb(102, 102, 102);\n"
                                                 "")
        self.Save_Setting_buttom_1.setFlat(False)
        self.Save_Setting_buttom_1.setObjectName("Save_Setting_buttom_1")
        self.gridLayout_2.addWidget(self.Save_Setting_buttom_1, 1, 6, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 11pt \"Tahoma\";\n"
                                        "background-color: rgb(102, 102, 102);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 11pt \"Tahoma\";\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(0, 0, 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setStyleSheet("font: 15pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setStyleSheet("font: 15pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.graphicsView_4 = PlotWidget(self.tab)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout_3.addWidget(self.graphicsView_4, 6, 2, 2, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("font: 15pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.graphicsView_2 = PlotWidget(self.tab)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_3.addWidget(self.graphicsView_2, 2, 2, 2, 1)
        self.graphicsView = PlotWidget(self.tab)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 2, 2, 1)
        self.graphicsView_3 = PlotWidget(self.tab)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout_3.addWidget(self.graphicsView_3, 4, 2, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setStyleSheet("font: 15pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setStyleSheet("background-color: rgb(0, 255, 64);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3.addWidget(self.widget_2, 3, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setStyleSheet("background-color: rgb(0, 255, 64);")
        self.widget.setObjectName("widget")
        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.tab)
        self.widget_3.setStyleSheet("background-color: rgb(0, 255, 64);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3.addWidget(self.widget_3, 5, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.tab)
        self.widget_4.setStyleSheet("background-color: rgb(0, 255, 64);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3.addWidget(self.widget_4, 7, 0, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lcdNumber_3.setFont(font)
        self.lcdNumber_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcdNumber_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_3.setProperty("intValue", 0)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout_3.addWidget(self.lcdNumber_3, 4, 1, 2, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout_3.addWidget(self.lcdNumber_4, 6, 1, 2, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_3.addWidget(self.lcdNumber_2, 2, 1, 2, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 0, 1, 2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem4, 3, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setStyleSheet("font: 15pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_3.setStyleSheet("font: 15pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_4.setStyleSheet("font: 15pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.checkBox_4)
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setStyleSheet("font: 15pt \"Tahoma\";color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem7)
        self.gridLayout_6.addLayout(self.formLayout_2, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 0, 1, 1, 1)
        self.graphicsView_Merge = PlotWidget(self.tab_2)
        self.graphicsView_Merge.setObjectName("graphicsView_Merge")
        self.gridLayout_6.addWidget(self.graphicsView_Merge, 0, 0, 7, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem9, 6, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 18pt \"Tahoma\";\n"
                                        "background-color: rgb(102, 102, 102);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ##############################################################################################################################################################################################################
        self.pushButton_2.clicked.connect(self.color)
        self.Save_Setting_buttom_1.clicked.connect(self.setting)
        self.pushButton_3.clicked.connect(self.runseepast)
        SingleGraph1 = self.graphicsView.plot(pen=(view()[0][2], view()[0][3], view()[0][4]))
        SingleGraph2 = self.graphicsView_2.plot(pen=(view()[1][2], view()[1][3], view()[1][4]))
        SingleGraph3 = self.graphicsView_3.plot(pen=(view()[2][2], view()[2][3], view()[2][4]))
        SingleGraph4 = self.graphicsView_4.plot(pen=(view()[3][2], view()[3][3], view()[3][4]))
        # self.graphicsView.getPlotItem().hideAxis('bottom')
        # self.graphicsView_2.getPlotItem().hideAxis('bottom')
        # self.graphicsView_3.getPlotItem().hideAxis('bottom')
        # self.graphicsView_4.getPlotItem().hideAxis('bottom')
        self.checkBox.stateChanged.connect(self.sensor1)
        self.checkBox_2.stateChanged.connect(self.sensor2)
        self.checkBox_3.stateChanged.connect(self.sensor3)
        self.checkBox_4.stateChanged.connect(self.sensor4)

        self.seepast = None

    def runseepast(self):
        if self.seepast == None:
            self.w = QtWidgets.QMainWindow()
            ui = SeePast.Ui_MainWindow()
            ui.setupUi(self.w)
            self.w.show().show()

    def color(self):
        global color
        color = QColorDialog.getColor()

    def setting(self):
        global SingleGraph1, SingleGraph2, SingleGraph3, SingleGraph4
        if str(self.comboBox_setting.currentText()) == view()[0][1]:
            try:
                update(id=1, R=color.getRgb()[0], G=color.getRgb()[1],
                       B=color.getRgb()[2])
                self.graphicsView.removeItem(SingleGraph1)
                SingleGraph1 = self.graphicsView.plot(pen=(view()[0][2], view()[0][3], view()[0][4]))
            except:
                pass
        if str(self.comboBox_setting.currentText()) == view()[1][1]:
            try:
                update(id=2, R=color.getRgb()[0], G=color.getRgb()[1],
                       B=color.getRgb()[2])
                self.graphicsView_2.removeItem(SingleGraph2)
                SingleGraph2 = self.graphicsView_2.plot(pen=(view()[1][2], view()[1][3], view()[1][4]))
            except:
                pass
        if str(self.comboBox_setting.currentText()) == view()[2][1]:
            try:
                update(id=3, R=color.getRgb()[0], G=color.getRgb()[1],
                       B=color.getRgb()[2])
                self.graphicsView_3.removeItem(SingleGraph3)
                SingleGraph3 = self.graphicsView_3.plot(pen=(view()[2][2], view()[2][3], view()[2][4]))
            except:
                pass
        if str(self.comboBox_setting.currentText()) == view()[3][1]:
            try:
                update(id=4, R=color.getRgb()[0], G=color.getRgb()[1],
                       B=color.getRgb()[2])
                self.graphicsView_4.removeItem(SingleGraph4)
                SingleGraph4 = self.graphicsView_4.plot(pen=(view()[3][2], view()[3][3], view()[3][4]))
            except:
                pass

    def sensor1(self):
        global MergeGraph1

        if self.checkBox.isChecked():
            MergeGraph1 = self.graphicsView_Merge.plot(pen=(view()[0][2], view()[0][3], view()[0][4]),
                                                       name=view()[0][1])
        else:
            self.graphicsView_Merge.addLegend().removeItem(MergeGraph1)
            MergeGraph1.clear()
            self.graphicsView_Merge.removeItem(MergeGraph1)

    def sensor2(self):
        global MergeGraph2
        if self.checkBox_2.isChecked():
            MergeGraph2 = self.graphicsView_Merge.plot(pen=(view()[1][2], view()[1][3], view()[1][4]),
                                                       name=view()[1][1])
        else:
            self.graphicsView_Merge.addLegend().removeItem(MergeGraph2)
            MergeGraph2.clear()
            self.graphicsView_Merge.removeItem(MergeGraph2)

    def sensor3(self):
        global MergeGraph3
        if self.checkBox_3.isChecked():
            MergeGraph3 = self.graphicsView_Merge.plot(pen=(view()[2][2], view()[2][3], view()[2][4]),
                                                       name=view()[2][1])
        else:
            self.graphicsView_Merge.addLegend().removeItem(MergeGraph3)
            MergeGraph3.clear()
            self.graphicsView_Merge.removeItem(MergeGraph3)

    def sensor4(self):
        global MergeGraph4
        if self.checkBox_4.isChecked():
            MergeGraph4 = self.graphicsView_Merge.plot(pen=(view()[3][2], view()[3][3], view()[3][4]),
                                                       name=view()[3][1])
        else:
            self.graphicsView_Merge.addLegend().removeItem(MergeGraph4)
            MergeGraph4.clear()
            self.graphicsView_Merge.removeItem(MergeGraph4)

    def update100(self):
        global a, b, c, d
        try:
            line = codecs.decode((ser.readline()), 'ascii')
            DataArray = line.split(',')
            a = round(float(DataArray[0]) / 5, 3)
            b = round(float(DataArray[1]) / 5, 3)
            c = round(float(DataArray[2]) / 5, 3)
            d = round(float(DataArray[3]) / 5, 3)
            DataSinglePlot.append(float(a))
            DataSinglePlot2.append(float(b))
            DataSinglePlot3.append(float(c))
            DataSinglePlot4.append(float(d))
            self.lcdNumber.display(float(DataSinglePlot[-1]))
            self.lcdNumber_2.display(float(DataSinglePlot2[-1]))
            self.lcdNumber_3.display(float(DataSinglePlot3[-1]))
            self.lcdNumber_4.display(float(DataSinglePlot4[-1]))
            SingleGraph1.setData(DataSinglePlot)
            SingleGraph2.setData(DataSinglePlot2)
            SingleGraph3.setData(DataSinglePlot3)
            SingleGraph4.setData(DataSinglePlot4)
            # self.graphicsView.setYRange(min=0, max=5, padding=0.05)
            # self.graphicsView_2.setYRange(min=0, max=5, padding=0.05)
            # self.graphicsView_3.setYRange(min=0, max=5, padding=0.05)
            # self.graphicsView_4.setYRange(min=0, max=5, padding=0.05)
            # self.graphicsView.setXRange(min=len(DataSinglePlot) - 1000, max=len(DataSinglePlot), padding=0.05)
            # self.graphicsView_2.setXRange(min=len(DataSinglePlot2) - 1000, max=len(DataSinglePlot2), padding=0.05)
            # self.graphicsView_3.setXRange(min=len(DataSinglePlot3) - 1000, max=len(DataSinglePlot3), padding=0.05)
            # self.graphicsView_4.setXRange(min=len(DataSinglePlot4) - 1000, max=len(DataSinglePlot4), padding=0.05)
            ################   checkBox  ###################
            DataMergePlot.append(float(a))
            DataMergePlot2.append(float(b))
            DataMergePlot3.append(float(c))
            DataMergePlot4.append(float(d))

            if self.checkBox.isChecked():
                MergeGraph1.setData(DataMergePlot)
                # self.graphicsView_Merge.setXRange(min=len(DataMergePlot) - 2000, max=len(DataMergePlot), padding=0.05)
            if self.checkBox_2.isChecked():
                MergeGraph2.setData(DataMergePlot2)
                # self.graphicsView_Merge.setXRange(min=len(DataMergePlot2) - 2000, max=len(DataMergePlot2), padding=0.05)
            if self.checkBox_3.isChecked():
                MergeGraph3.setData(DataMergePlot3)
                # self.graphicsView_Merge.setXRange(min=len(DataMergePlot3) - 2000, max=len(DataMergePlot3), padding=0.05)
            if self.checkBox_4.isChecked():
                MergeGraph4.setData(DataMergePlot4)
                # self.graphicsView_Merge.setXRange(min=len(DataMergePlot4) - 2000, max=len(DataMergePlot4), padding=0.05)

            if len(DataSinglePlot) == 1000:
                del DataSinglePlot[0]
                del DataSinglePlot2[0]
                del DataSinglePlot3[0]
                del DataSinglePlot4[0]

            if len(DataMergePlot) == 5000:
                del DataMergePlot[0]
                del DataMergePlot2[0]
                del DataMergePlot3[0]
                del DataMergePlot4[0]

            app.processEvents()
        except ValueError:
            pass
        except AttributeError:
            pass
        try:

            if os.path.isfile('Data_is_saving\\log_data.csv'):
                with open("Data_is_saving\\log_data.csv", "a", newline='') as f:
                    writer = csv.writer(f, delimiter=",")
                    writer.writerow(
                        [dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), a, b, c, d])
                    if a > view()[0][6] or a < view()[0][5]:
                        self.widget.setStyleSheet("background-color: rgb(255, 0, 0);")
                        with open("Log_Warning_File\\log_Warning_data_sensor1.csv", "a",
                                  newline='') as f:
                            writer = csv.writer(f, delimiter=",")
                            writer.writerow(
                                [dt.datetime.now().strftime("%D %H:%M:%S.%f %p"), a])
                    else:
                        self.widget.setStyleSheet("background-color: rgb(0, 255, 0);")

                    if b > view()[1][6] or b < view()[1][5]:
                        self.widget_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                        with open("Log_Warning_File\\log_Warning_data_sensor2.csv", "a",
                                  newline='') as f:
                            writer = csv.writer(f, delimiter=",")
                            writer.writerow(
                                [dt.datetime.now().strftime("%D %H:%M:%S.%f %p"), b])
                    else:
                        self.widget_2.setStyleSheet("background-color: rgb(0, 255, 0);")

                    if c > view()[2][6] or c < view()[2][5]:
                        self.widget_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                        with open("Log_Warning_File\\log_Warning_data_sensor3.csv", "a",
                                  newline='') as f:
                            writer = csv.writer(f, delimiter=",")
                            writer.writerow(
                                [dt.datetime.now().strftime("%D %H:%M:%S.%f %p"), c])
                    else:
                        self.widget_3.setStyleSheet("background-color: rgb(0, 255, 0);")

                    if d > view()[3][6] or d < view()[3][5]:
                        self.widget_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                        with open("Log_Warning_File\\log_Warning_data_sensor4.csv", "a",
                                  newline='') as f:
                            writer = csv.writer(f, delimiter=",")
                            writer.writerow(
                                [dt.datetime.now().strftime("%D %H:%M:%S.%f %p"), d])
                    else:
                        self.widget_4.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                with open("Data_is_saving\\log_data.csv", "a", newline='') as f:
                    fieldnames = ['DATE', 'XLZ', 'Sensor 01', 'Sensor 02', 'Sensor 03']
                    writer = csv.DictWriter(f, delimiter=",", fieldnames=fieldnames)
                    writer.writeheader()
        except PermissionError:
            pass
        except ValueError:
            pass
        except IndexError:
            pass
        except NameError:
            pass
        if os.path.getsize('Data_is_saving\\log_data.csv') > 100 * 1000000:
            Rename_time_file.append(dt.datetime.now().strftime('%Y-%m-%d %H.%M.%S'))
            os.rename('Data_is_saving\\log_data.csv',
                      '(' + str(Rename_time_file[-2]) + ')' + '--' + '(' + str(
                          Rename_time_file[-1]) + ')' + '.csv')
        if len(Rename_time_file) == 3:
            del Rename_time_file[0]
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if '.csv' in f:
                src_path = f
                dst_path = "Log_File\\{}".format(f)
                shutil.move(src_path, dst_path)
            else:
                pass

    ##############################################################################################################################################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trends - JAV"))
        self.comboBox_setting.setItemText(0, _translate("MainWindow", view()[0][1]))
        self.comboBox_setting.setItemText(1, _translate("MainWindow", view()[1][1]))
        self.comboBox_setting.setItemText(2, _translate("MainWindow", view()[2][1]))
        self.comboBox_setting.setItemText(3, _translate("MainWindow", view()[3][1]))
        self.Save_Setting_buttom_1.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Select your Color GraghView"))
        self.label_3.setText(_translate("MainWindow", view()[2][1]))
        self.label_2.setText(_translate("MainWindow", view()[1][1]))
        self.label_4.setText(_translate("MainWindow", view()[3][1]))
        self.label.setText(_translate("MainWindow", view()[0][1]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Trend Sensors"))
        self.checkBox.setText(_translate("MainWindow", view()[0][1]))
        self.checkBox_3.setText(_translate("MainWindow", view()[2][1]))
        self.checkBox_2.setText(_translate("MainWindow", view()[1][1]))
        self.checkBox_4.setText(_translate("MainWindow", view()[3][1]))
        self.pushButton_3.setText(_translate("MainWindow", "            Run SeePast           "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Trend Merge"))
        self.graphicsView_Merge.addLegend()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
timer = QtCore.QTimer()
timer.timeout.connect(ui.update100)
timer.start(0)
sys.exit(app.exec_())
