import sys
import datetime as dt
import sqlite3

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1174, 771)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setIconSize(QtCore.QSize(100, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.formLayout = QtWidgets.QFormLayout(self.frame2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame2)
        self.label.setStyleSheet("font: italic 12pt \"Georgia\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name_frame2 = QtWidgets.QLineEdit(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.name_frame2.sizePolicy().hasHeightForWidth())
        self.name_frame2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_frame2.setFont(font)
        self.name_frame2.setObjectName("name_frame2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_frame2)
        self.label_2 = QtWidgets.QLabel(self.frame2)
        self.label_2.setStyleSheet("font: italic 12pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.start_frame2 = QtWidgets.QDateTimeEdit(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_frame2.sizePolicy().hasHeightForWidth())
        self.start_frame2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_frame2.setFont(font)
        self.start_frame2.setObjectName("start_frame2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.start_frame2)
        self.label_3 = QtWidgets.QLabel(self.frame2)
        self.label_3.setStyleSheet("font: italic 12pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.finish_frame2 = QtWidgets.QDateTimeEdit(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finish_frame2.sizePolicy().hasHeightForWidth())
        self.finish_frame2.setSizePolicy(sizePolicy)
        self.finish_frame2.setBaseSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finish_frame2.setFont(font)
        self.finish_frame2.setObjectName("finish_frame2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.finish_frame2)
        self.label_4 = QtWidgets.QLabel(self.frame2)
        self.label_4.setStyleSheet("font: italic 12pt \"Georgia\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.description_frame2 = QtWidgets.QTextEdit(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description_frame2.sizePolicy().hasHeightForWidth())
        self.description_frame2.setSizePolicy(sizePolicy)
        self.description_frame2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_frame2.setFont(font)
        self.description_frame2.setObjectName("description_frame2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.description_frame2)
        self.ok_btn = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        self.ok_btn.setStyleSheet("background-color: rgb(111, 200, 255)")
        self.ok_btn.setObjectName("ok_btn")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)
        self.cancel_btn.setAutoDefault(False)
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cancel_btn)
        self.gridLayout_3.addWidget(self.frame2, 1, 0, 1, 1)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.NewTask_btn = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewTask_btn.sizePolicy().hasHeightForWidth())
        self.NewTask_btn.setSizePolicy(sizePolicy)
        self.NewTask_btn.setMinimumSize(QtCore.QSize(0, 34))
        self.NewTask_btn.setAutoFillBackground(False)
        self.NewTask_btn.setStyleSheet("font: 9pt \"MV Boli\";\n"
                                       "background-color: rgb(172, 255, 157)")
        self.NewTask_btn.setObjectName("NewTask_btn")
        self.gridLayout_2.addWidget(self.NewTask_btn, 0, 0, 1, 1)
        self.hide_inactive = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hide_inactive.sizePolicy().hasHeightForWidth())
        self.hide_inactive.setSizePolicy(sizePolicy)
        self.hide_inactive.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.hide_inactive.setStyleSheet("font: 9pt \"MV Boli\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_inactive.setIcon(icon)
        self.hide_inactive.setIconSize(QtCore.QSize(25, 25))
        self.hide_inactive.setObjectName("hide_inactive")
        self.gridLayout_2.addWidget(self.hide_inactive, 0, 6, 1, 1)
        self.Logo_btn = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo_btn.sizePolicy().hasHeightForWidth())
        self.Logo_btn.setSizePolicy(sizePolicy)
        self.Logo_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Logo_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Logo_btn.setIcon(icon1)
        self.Logo_btn.setIconSize(QtCore.QSize(35, 35))
        self.Logo_btn.setObjectName("Logo_btn")
        self.gridLayout_2.addWidget(self.Logo_btn, 0, 13, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame1)
        self.treeWidget.setMinimumSize(QtCore.QSize(821, 0))
        self.treeWidget.setMouseTracking(True)
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0,
                                                      QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(1, font)
        self.treeWidget.headerItem().setTextAlignment(2,
                                                      QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget.headerItem().setFont(2, font)
        self.gridLayout_2.addWidget(self.treeWidget, 1, 0, 1, 14)
        self.Logo_label = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo_label.sizePolicy().hasHeightForWidth())
        self.Logo_label.setSizePolicy(sizePolicy)
        self.Logo_label.setStyleSheet("font: 16pt \"MV Boli\";")
        self.Logo_label.setObjectName("Logo_label")
        self.gridLayout_2.addWidget(self.Logo_label, 0, 12, 1, 1)
        self.hide_done = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hide_done.sizePolicy().hasHeightForWidth())
        self.hide_done.setSizePolicy(sizePolicy)
        self.hide_done.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.hide_done.setStyleSheet("font: 9pt \"MV Boli\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("galochka.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_done.setIcon(icon2)
        self.hide_done.setIconSize(QtCore.QSize(25, 25))
        self.hide_done.setObjectName("hide_done")
        self.gridLayout_2.addWidget(self.hide_done, 0, 5, 1, 1)
        self.not_done_btn = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_done_btn.sizePolicy().hasHeightForWidth())
        self.not_done_btn.setSizePolicy(sizePolicy)
        self.not_done_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("red_x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.not_done_btn.setIcon(icon3)
        self.not_done_btn.setIconSize(QtCore.QSize(25, 25))
        self.not_done_btn.setObjectName("not_done_btn")
        self.gridLayout_2.addWidget(self.not_done_btn, 0, 4, 1, 1)
        self.NewElement_btn = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewElement_btn.sizePolicy().hasHeightForWidth())
        self.NewElement_btn.setSizePolicy(sizePolicy)
        self.NewElement_btn.setMinimumSize(QtCore.QSize(0, 34))
        self.NewElement_btn.setAutoFillBackground(False)
        self.NewElement_btn.setStyleSheet("font: 9pt \"MV Boli\";\n"
                                          "background-color: rgb(193, 205, 255)")
        self.NewElement_btn.setIconSize(QtCore.QSize(16, 30))
        self.NewElement_btn.setObjectName("NewElement_btn")
        self.gridLayout_2.addWidget(self.NewElement_btn, 0, 1, 1, 1)
        self.bin_btn = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bin_btn.sizePolicy().hasHeightForWidth())
        self.bin_btn.setSizePolicy(sizePolicy)
        self.bin_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bin_btn.setIcon(icon4)
        self.bin_btn.setIconSize(QtCore.QSize(25, 25))
        self.bin_btn.setObjectName("bin_btn")
        self.gridLayout_2.addWidget(self.bin_btn, 0, 3, 1, 1)
        self.Done_btn = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Done_btn.sizePolicy().hasHeightForWidth())
        self.Done_btn.setSizePolicy(sizePolicy)
        self.Done_btn.setText("")
        self.Done_btn.setIcon(icon2)
        self.Done_btn.setIconSize(QtCore.QSize(25, 25))
        self.Done_btn.setObjectName("Done_btn")
        self.gridLayout_2.addWidget(self.Done_btn, 0, 2, 1, 1)
        self.report_btn = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report_btn.sizePolicy().hasHeightForWidth())
        self.report_btn.setSizePolicy(sizePolicy)
        self.report_btn.setMinimumSize(QtCore.QSize(93, 34))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.report_btn.setFont(font)
        self.report_btn.setStyleSheet("font: 9pt \"MV Boli\";\n"
                                      "background-color: rgb(255, 190, 146)")
        self.report_btn.setObjectName("report_btn")
        self.gridLayout_2.addWidget(self.report_btn, 0, 7, 1, 1)
        self.gridLayout_3.addWidget(self.frame1, 0, 0, 1, 1)
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_done_task = QtWidgets.QDateTimeEdit(self.frame3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_done_task.sizePolicy().hasHeightForWidth())
        self.start_done_task.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_done_task.setFont(font)
        self.start_done_task.setObjectName("start_done_task")
        self.verticalLayout.addWidget(self.start_done_task)
        self.finish_done_task = QtWidgets.QDateTimeEdit(self.frame3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finish_done_task.sizePolicy().hasHeightForWidth())
        self.finish_done_task.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finish_done_task.setFont(font)
        self.finish_done_task.setObjectName("finish_done_task")
        self.verticalLayout.addWidget(self.finish_done_task)
        self.show_done_tasks_btn = QtWidgets.QPushButton(self.frame3)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.show_done_tasks_btn.setFont(font)
        self.show_done_tasks_btn.setStyleSheet("font: 12pt \"MV Boli\";\n"
                                               "background-color: rgb(170, 170, 255)")
        self.show_done_tasks_btn.setObjectName("show_done_tasks_btn")
        self.verticalLayout.addWidget(self.show_done_tasks_btn)
        self.done_tasks_table = QtWidgets.QTableWidget(self.frame3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done_tasks_table.sizePolicy().hasHeightForWidth())
        self.done_tasks_table.setSizePolicy(sizePolicy)
        self.done_tasks_table.setObjectName("done_tasks_table")
        self.done_tasks_table.setColumnCount(2)
        self.done_tasks_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.done_tasks_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.done_tasks_table.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.done_tasks_table)
        self.close_btn = QtWidgets.QPushButton(self.frame3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setStyleSheet("color: rgb(255, 0, 0);")
        self.close_btn.setObjectName("close_btn")
        self.verticalLayout.addWidget(self.close_btn)
        self.gridLayout_3.addWidget(self.frame3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1174, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Название:"))
        self.label_2.setText(_translate("MainWindow", "Начало:"))
        self.start_frame2.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy HH:mm"))
        self.label_3.setText(_translate("MainWindow", "Конец:"))
        self.finish_frame2.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy HH:mm"))
        self.label_4.setText(_translate("MainWindow", "Описание:"))
        self.ok_btn.setText(_translate("MainWindow", "ОК"))
        self.cancel_btn.setText(_translate("MainWindow", "Отмена"))
        self.NewTask_btn.setToolTip(_translate("MainWindow", "Добавить новую задачу"))
        self.NewTask_btn.setText(_translate("MainWindow", "Новая задача"))
        self.hide_inactive.setToolTip(_translate("MainWindow", "Скрыть неактивные задачи"))
        self.hide_inactive.setText(_translate("MainWindow", "Скрыть"))
        self.treeWidget.setToolTip(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Тема"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Начало"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Срок"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "id"))
        self.Logo_label.setText(_translate("MainWindow", "TaskPlanner"))
        self.hide_done.setToolTip(_translate("MainWindow", "Скрыть выполненные задачи"))
        self.hide_done.setText(_translate("MainWindow", "Скрыть"))
        self.not_done_btn.setToolTip(_translate("MainWindow", "Отметить задачу невыполненной"))
        self.NewElement_btn.setToolTip(_translate("MainWindow", "Добавить новую подзадачу"))
        self.NewElement_btn.setText(_translate("MainWindow", "Новый подэлемент"))
        self.bin_btn.setToolTip(_translate("MainWindow", "Удалить задачу"))
        self.Done_btn.setToolTip(_translate("MainWindow", "Отметить задачу выполненной"))
        self.report_btn.setText(_translate("MainWindow", "Отчет выполненных задач"))
        self.start_done_task.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy HH:mm"))
        self.finish_done_task.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy HH:mm"))
        self.show_done_tasks_btn.setText(_translate("MainWindow", "Показать выполненные задачи"))
        item = self.done_tasks_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Задача"))
        item = self.done_tasks_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Время выполнения"))
        self.close_btn.setText(_translate("MainWindow", "Закрыть"))


class MyWidget(QMainWindow):
    RED = QColor(255, 0, 0)
    PURPLE = QColor(85, 0, 127)
    GREY = QColor(170, 170, 170)
    GREEN = QColor(0, 255, 0)
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('orders.db',
                                    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")
        self.create_database()
        uic.loadUi('TaskPlanner.ui', self)  # Загружаем дизайн
        self.initUI()
        self.NewTask_btn.clicked.connect(self.create_task)
        self.NewElement_btn.clicked.connect(self.create_task)
        self.treeWidget.hideColumn(3)
        self.Done_btn.clicked.connect(self.ticked_task)
        self.bin_btn.clicked.connect(self.delete_task)
        self.ok_btn.pressed.connect(self.save_info_frame2)
        self.cancel_btn.pressed.connect(self.save_info_frame2)
        self.treeWidget.itemDoubleClicked.connect(self.show_frame2)
        self.resized.connect(self.change_size)
        self.not_done_btn.clicked.connect(self.not_ticked)
        self.hide_done.clicked.connect(self.hide_done_tasks)
        self.hide_inactive.clicked.connect(self.hide_inactive_tasks)
        self.report_btn.clicked.connect(self.show_frame3)
        self.show_done_tasks_btn.clicked.connect(self.show_report_done_tasks)
        self.close_btn.clicked.connect(self.close_frame3)
        self.task_structure = {}
        self.current_task = None
        self.hide_green_tasks = None
        self.hide_grey_tasks = None
        self.my_format = '%d.%m.%Y %H:%M'
        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.task_status_update)  # По истечении таймера запускается функция task_status_update
        self.timer.start(60000)  # Запуск таймера на 1 минуту
        self.task_status_update()
        self.frame2.hide()
        self.frame3.hide()

    def initUI(self):
        self.setWindowTitle('TaskPlanner')

    def resizeEvent(self, event):
        """
        Переопределение метода базового класса, добавление сигнала изменения размера основного окна.
        """
        self.resized.emit()
        return super(MyWidget, self).resizeEvent(event)

    def hide_inactive_tasks(self):
        """
        При нажатии на "Скрыть неактивные задачи" они становятся невидимыми
        (параметр self.hide_grey_tasks = True). Если при нажатии кнопки будущие задачи итак были
        скрыты, они снова становятся видимыми (параметр self.hide_grey_tasks = False)
        """
        if self.hide_grey_tasks:
            self.hide_grey_tasks = False
        else:
            self.hide_grey_tasks = True
        self.task_status_update()

    def hide_done_tasks(self):
        """
        При нажатии на "Скрыть выполненные задачи" они становятся невидимыми
        (параметр self.hide_green_tasks = True). Если при нажатии кнопки выполненные задачи итак были
        скрыты, они снова становятся видимыми (параметр self.hide_green_tasks = False).
        """
        if self.hide_green_tasks:
            self.hide_green_tasks = False
        else:
            self.hide_green_tasks = True
        self.task_status_update()

    def show_frame3(self):
        self.frame1.hide()
        self.frame3.show()
        self.start_done_task.setDateTime(dt.datetime.now())
        self.finish_done_task.setDateTime(dt.datetime.now())

    def close_frame3(self):
        self.frame3.hide()
        self.frame1.show()

    def show_report_done_tasks(self):
        try:
            start = dt.datetime.strptime(self.start_done_task.text(), self.my_format)
            finish = dt.datetime.strptime(self.finish_done_task.text(), self.my_format)
            tasks = self.cur.execute(
                '''SELECT tr.theme, tm.time_done FROM tree as tr, time as tm WHERE tr.id = tm.task_id AND tm.time_done >= ? AND tm.time_done <= ?''',
                (start, finish)).fetchall()
            self.done_tasks_table.setRowCount(0)
            for i, task in enumerate(tasks):
                self.done_tasks_table.setRowCount(self.done_tasks_table.rowCount() + 1)
                self.done_tasks_table.setItem(i, 0, QTableWidgetItem(task[0]))
                self.done_tasks_table.setItem(i, 1, QTableWidgetItem(
                    dt.datetime.strftime(task[1], self.my_format)))
            self.done_tasks_table.resizeColumnsToContents()
        except Exception as err:
            print(err)

    def not_ticked(self):
        """
        При отмене у задачи статуса "выполненной" функция not_ticked вызывает рекурсивную функцию
        delete_done_status от выбранной задачи и удаляет статус "выполненной" у этой задачи и ее
        предков (если они есть). После отрабатывания функции delete_done_status вызывается
        task_status_update(), чтобы обновить базу данных и дерево.
        """
        try:
            task = self.treeWidget.selectedItems()[0]
            self.delete_done_status(task)
            self.task_status_update()
        except Exception as err:
            print(err)

    def delete_done_status(self, task):
        """
        Удаление у задачи статуса 'выполненная' и рекурсивный вызов функции от ее предка, если он
        был выполнен.
        """
        try:
            self.cur.execute('''UPDATE tree SET status=False WHERE id=?''', (task.text(3),))
            self.cur.execute('''DELETE FROM time WHERE task_id=?''', (task.text(3),))
            self.conn.commit()
            parent = task.parent()
            if parent:
                if self.cur.execute('''SELECT status FROM tree WHERE id=?''',
                                    (parent.text(3),)).fetchall():
                    self.delete_done_status(parent)
        except Exception as err:
            print(err)

    def change_size(self):
        """
        Изменение ширины первого столба в дереве, когда размер окна изменяется.
        """
        self.treeWidget.setColumnWidth(0, self.treeWidget.size().width() -
                                       self.treeWidget.columnWidth(1) * 2)

    def show_frame2(self, item):
        """
        Появление второго окна при двойном клике на задачу. Автоматическое заполнение формы данными
        из дерева и базы данных.
        """
        self.current_task = item
        self.frame2.show()
        self.frame1.hide()
        self.name_frame2.setText(self.current_task.text(0))
        self.start_frame2.setDateTime(
            dt.datetime.strptime(self.current_task.text(1), self.my_format))
        self.finish_frame2.setDateTime(
            dt.datetime.strptime(self.current_task.text(2), self.my_format))
        description = self.cur.execute('''SELECT description FROM tree WHERE id=?''',
                                       (self.current_task.text(3),)).fetchone()
        self.description_frame2.setText(description[0])

    def save_info_frame2(self):
        """
        Если во втором окне пользователь ответил да, после редактирования задачи, то дерево
        заполняется новой информацией и вызывается функция change_task. Если же пользователь ответил
        нет, то второе окно закрывается и возвращается главное окно без изменений.
        """
        try:
            if self.sender().text() == 'ОК':
                self.frame1.show()
                self.frame2.hide()
                print(self.name_frame2.text(), self.start_frame2.text(), self.finish_frame2.text(),
                      self.description_frame2.toPlainText())
                print(self.current_task)
                self.current_task.setText(0, self.name_frame2.text())
                self.current_task.setText(1, self.start_frame2.text())
                self.current_task.setText(2, self.finish_frame2.text())
                self.cur.execute('''UPDATE tree SET description=? WHERE id=?''',
                                 (self.description_frame2.toPlainText(), self.current_task.text(3)))
                self.conn.commit()
                self.change_task(self.current_task)
            else:
                self.frame1.show()
                self.frame2.hide()
        except Exception as err:
            print(err)

    def create_task(self):
        """
        Если была нажата кнопка "Новый подэлемент", то к выбранной задаче добавляется подзадача,
        которая заполняется во втором и третьем столбце текущей датой и следующей датой
        соответственно (переменные start, finish). Даты в дереве преобразованы в строку.
        Новая подзадача сохраняется в базе данных со всеми данными из дерева, а потом четвертый
        столбец дерева (невидимый) заполняется id
        подзадачи из базы данных. Открытие второго окна для редактирования.
        Если пользователь кликнул на кнопку "Новая задача", то к qtreewidget добавляется задача,
        которая заполняется во втором и третьем столбце текущей датой и следующей датой
        соответственно (переменные start, finish). Даты в дереве преобразованы в строку.
        Новая задача сохраняется в базе данных со всеми данными из дерева, а потом четвертый
        столбец дерева (невидимый) заполняется id
        задачи из базы данных. Открытие второго окна для редактирования.
        """
        start = dt.datetime.today()
        finish = dt.datetime.today() + dt.timedelta(days=1)
        if self.sender().text() == 'Новый подэлемент':
            try:
                parent = self.treeWidget.selectedItems()[0]
                if parent:
                    child = QTreeWidgetItem(parent)
                    child.setText(0, 'Новый подэлемент')
                    child.setText(1, dt.datetime.strftime(start, self.my_format))
                    child.setText(2, dt.datetime.strftime(finish, self.my_format))
                    query = self.cur.execute('''INSERT INTO tree(theme, start, finish, parent_id, status) 
                        VALUES(?, ?, ?, ?, ?);''', (
                        child.text(0), start, finish, int(parent.text(3)), False))
                    child.setText(3, str(query.lastrowid))
                    self.conn.commit()
                    self.show_frame2(child)
            except Exception as err:
                print('Выберете задачу')
        elif self.sender().text() == 'Новая задача':
            root = QTreeWidgetItem(self.treeWidget)
            root.setText(0, 'Новая задача')
            root.setText(1, dt.datetime.strftime(start, self.my_format))
            root.setText(2, dt.datetime.strftime(finish, self.my_format))
            query = self.cur.execute(
                '''INSERT INTO tree(theme, start, finish, parent_id, status) 
                VALUES(?, ?, ?, ?, ?);''',
                (root.text(0), start, finish, None, False))
            root.setText(3, str(query.lastrowid))
            self.conn.commit()
            self.show_frame2(root)

    def change_task(self, item):
        """
        Редактирование базы данных изменением данных задач, полученных из второго окна.
        Преобразование дат из строки в объект datetime.
        """
        self.cur.execute('''UPDATE tree SET theme=?, start=?, finish=? WHERE id=?''',
                         (item.text(0), dt.datetime.strptime(item.text(1), self.my_format),
                          dt.datetime.strptime(item.text(2), self.my_format), int(item.text(3))))
        self.conn.commit()
        self.task_status_update()

    def ticked_task(self):
        """
        Вызов рекурсивной функции update_done_status от выбранной задачи при изменении ее
        статуса на "выполненную".
        """
        try:
            task = self.treeWidget.selectedItems()[0]
            self.update_done_status(task)
        except Exception as err:
            print(err)

    def update_done_status(self, task):
        """
        Если у задачи есть потомки, то выполняется проверка, все ли ее подзадачи выполнены. Если нет,
        то высвечивается предупреждение, что не все подзадачи выполнены и функция ничего не
        возвращает. Если все подзадачи выполнены, то задача становится зеленой, в базе данных ее
        статус меняется на "выполненную". Если эта задача является подзадачей другой задачи, то
        вызывается функция all_children_done. Если функция вернула True, то высвечивается
        предложение отметить задачу выполненной. Если ответ да, то функция вызывается от этой задачи.
        """
        try:
            task_id = task.text(3)
            parent = task.parent()
            if task.childCount():
                if not self.all_children_done(task_id):
                    valid = QMessageBox.warning(
                        self, '', "Не все подзадачи выполнены",
                        QMessageBox.Ok)
                    return
            task.setForeground(0, MyWidget.GREEN)
            task.setForeground(1, MyWidget.GREEN)
            task.setForeground(2, MyWidget.GREEN)
            self.cur.execute('''UPDATE tree SET status=True WHERE id=?''', (task_id,))
            self.cur.execute('''INSERT INTO time(task_id, time_done) 
                        VALUES(?, ?);''', (task_id, dt.datetime.now()))
            self.conn.commit()
            if parent:
                if self.all_children_done(parent.text(3)):
                    valid = QMessageBox.question(
                        self, '', "Вы выполнили все подзадачи, отметить задачу выполненной?",
                        QMessageBox.Yes, QMessageBox.No)
                    if valid == QMessageBox.Yes:
                        self.update_done_status(parent)
        except Exception as err:
            print(err)

    def all_children_done(self, task_id):
        """
        Если функция нашла хотя бы одну задачу со статусом "невыполненная", то возвращается False,
        если же нет - True.
        """
        if self.cur.execute('''SELECT id FROM tree WHERE parent_id=? and status=?''',
                            (task_id, False)).fetchone():
            return False
        return True

    def task_status_update(self):
        """
        На основе данных из базы данных создается словарь с ключом-id задачи и значением-словаря,
        в котором ключи: название(значение-строка),
        начало срока (значение-объект datetime), конец срока (значение-объект datetime), id родителя
        (значение-число), дети (значение-список id подзадач), статус (значение-True/False) и описание
        (значение-строка).
        Дерево очищается и заполняется заново на основе словаря. idб начало и конец срока
        преобразуются в строку. Вызывается функция get_color с аргументами - статус, начало и конец
        срока. в полученный цвет окрашивается задача. В зависимости от значения переменных
        hide_green_tasks, hide_grey_tasks и цвета задача становится невидимой (или нет, если она не
        подошла ни под одно условие). Запускается рекурсивная функция add_children от id задачи и ее
        родителя. Запускается таймер на 1 минуту (в миллисекундах).
        """
        print('task_status_update')
        try:
            self.task_structure = {}
            tasks = self.cur.execute('''SELECT * FROM tree''').fetchall()
            self.treeWidget.clear()
            for task in tasks:
                self.task_structure[task[0]] = {'theme': task[1], 'start': task[2],
                                                'finish': task[3],
                                                'parent_id': task[4], 'children': [],
                                                'status': task[5], 'description': task[6]}
                if task[4]:
                    self.task_structure[task[4]]['children'].append(task[0])
            for taskid, task in self.task_structure.items():
                if not task['parent_id']:
                    root = QTreeWidgetItem(self.treeWidget)
                    root.setText(0, task['theme'])
                    root.setText(1, dt.datetime.strftime(task['start'], self.my_format))
                    root.setText(2, dt.datetime.strftime(task['finish'], self.my_format))
                    root.setText(3, str(taskid))
                    color = self.get_color(task['status'], task['start'], task['finish'])
                    for i in range(3):
                        root.setForeground(i, color)
                    if self.hide_green_tasks:
                        if self.task_structure[taskid]['status']:
                            root.setHidden(True)
                    if self.hide_grey_tasks:
                        if self.task_structure[taskid]['start'] > dt.datetime.now():
                            if self.task_structure[taskid]['finish'] > dt.datetime.now():
                                root.setHidden(True)
                    self.add_children(taskid, root)
            self.treeWidget.expandAll()
            self.timer.start(60000)
        except Exception as err:
            print(err)

    def add_children(self, taskid, parent):
        """
        Прохождение по списку "детей" из словаря для заданного ключа и добавление подзадач в дерево.
        Преобразование id, начала и конца срока в строку. Вызов функции get_color от статуса, начала
        и конца срока задачи, получение из нее цвета. В зависимости от значения переменных
        hide_green_tasks, hide_grey_tasks и цвета подзадача становится невидимой (или нет, если она
        не подошла ни под одно условие). Рекурсивный вызов функции от этой подзадачи и ее родителя.
        """
        for ch in self.task_structure[taskid]['children']:
            child_data = self.task_structure[ch]
            child = QTreeWidgetItem(parent)
            child.setText(0, child_data['theme'])
            child.setText(1, dt.datetime.strftime(child_data['start'], self.my_format))
            child.setText(2, dt.datetime.strftime(child_data['finish'], self.my_format))
            child.setText(3, str(ch))
            color = self.get_color(child_data['status'], child_data['start'],
                                   child_data['finish'])
            for i in range(3):
                child.setForeground(i, color)
            if self.hide_green_tasks:
                if self.task_structure[ch]['status']:
                    child.setHidden(True)
            if self.hide_grey_tasks:
                if self.task_structure[ch]['start'] > dt.datetime.now():
                    if self.task_structure[ch]['finish'] > dt.datetime.now():
                        child.setHidden(True)
            self.add_children(ch, child)

    def get_color(self, status, start, finish):
        """
        Если статус задачи True, то возвращается зеленый цвет(задача выполнена),
        если дата начала и конца срока
        задачи меньше сегоднешней даты, то возвращается красный цвет (задача просрочена). Если же
        дата начала срока меньше сегоднешней даты, а конец равен или больше, то возвращается
        фиолетовый цвет (задача активна). Если и начало, и конец срока больше сегоднешней даты, то
        возвращается серый цвет (задача неактивна).
        """
        if status:
            return MyWidget.GREEN
        if start <= dt.datetime.now():
            if finish < dt.datetime.now():
                return MyWidget.RED
            else:
                return MyWidget.PURPLE
        else:
            return MyWidget.GREY

    def delete_task(self):
        """
        Перед удалением задачи или подзадачи высвечивается вопрос с уточнением, точно ли
        пользователь хочет удалить задачу. Если у выбранной задачи есть родитель, то применяется
        removeChild, если нет - takeTopLevelItem. Удаление этой задачи со всеми ее элементами из
        базы данных.
        """
        try:
            task = self.treeWidget.selectedItems()[0]
            parent = task.parent()
            valid = QMessageBox.question(
                self, '', "Вы действительно хотите удалить задачу?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                self.cur.execute('''DELETE FROM tree WHERE id=?''', (task.text(3),))
                self.conn.commit()
                if parent:
                    parent.removeChild(task)
                else:
                    self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(task))
        except Exception as err:
            print('delete', err)

    def create_database(self):
        """
        Создание базы данных (название ее столбцов и принимаемые ими значения).
        """
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tree (
    id          INTEGER   PRIMARY KEY AUTOINCREMENT,
    theme       TEXT      NOT NULL,
    start       timestamp,
    finish      timestamp,
    parent_id   INTEGER   REFERENCES tree (id) ON DELETE CASCADE,
    status      BOOLEAN   DEFAULT (False),
    description TEXT
);""")
        self.cur.execute('''CREATE TABLE IF NOT EXISTS time (
    id          INTEGER   PRIMARY KEY AUTOINCREMENT,
    task_id   INTEGER  REFERENCES tree (id) ON DELETE CASCADE,
    time_done timestamp
);''')
        self.conn.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.showMaximized()
    sys.exit(app.exec_())
