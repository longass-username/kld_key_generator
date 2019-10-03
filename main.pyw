from PyQt5 import QtCore, QtGui, QtWidgets
from Cryptodome.Cipher import DES3
from binascii import unhexlify
from random import randint
#import pyDes
import sys
import re
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(788, 544)
        MainWindow.setMaximumSize(QtCore.QSize(788, 544))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(0, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.sec_is_enabled = QtWidgets.QCheckBox(self.centralwidget)
        self.sec_is_enabled.setMinimumSize(QtCore.QSize(0, 31))
        self.sec_is_enabled.setText("")
        self.sec_is_enabled.setObjectName("sec_is_enabled")
        self.verticalLayout_2.addWidget(self.sec_is_enabled)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.first_comp = QtWidgets.QLineEdit(self.centralwidget)
        self.first_comp.setMinimumSize(QtCore.QSize(431, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.first_comp.setFont(font)
        self.first_comp.setText("")
        self.first_comp.setMaxLength(32)
        self.first_comp.setObjectName("first_comp")
        self.horizontalLayout.addWidget(self.first_comp)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(211, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.second_comp = QtWidgets.QLineEdit(self.centralwidget)
        self.second_comp.setEnabled(False)
        self.second_comp.setMinimumSize(QtCore.QSize(431, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.second_comp.setFont(font)
        self.second_comp.setText("")
        self.second_comp.setMaxLength(32)
        self.second_comp.setObjectName("second_comp")
        self.horizontalLayout_2.addWidget(self.second_comp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.ZMK_button = QtWidgets.QPushButton(self.centralwidget)
        self.ZMK_button.setMinimumSize(QtCore.QSize(271, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ZMK_button.setFont(font)
        self.ZMK_button.setObjectName("ZMK_button")
        self.horizontalLayout_4.addWidget(self.ZMK_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.format_box = QtWidgets.QComboBox(self.centralwidget)
        self.format_box.setAcceptDrops(False)
        self.format_box.setObjectName("format_box")
        self.format_box.addItem("")
        self.format_box.addItem("")
        self.format_box.addItem("")
        self.format_box.addItem("")
        # self.format_box.addItem("")
        self.horizontalLayout_10.addWidget(self.format_box)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(141, 31))
        self.label_3.setMaximumSize(QtCore.QSize(141, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.key_amount = QtWidgets.QSpinBox(self.centralwidget)
        self.key_amount.setMinimumSize(QtCore.QSize(109, 22))
        self.key_amount.setMaximumSize(QtCore.QSize(109, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.key_amount.setFont(font)
        self.key_amount.setMinimum(1)
        self.key_amount.setMaximum(10000)
        self.key_amount.setProperty("value", 100)
        self.key_amount.setObjectName("key_amount")
        self.horizontalLayout_9.addWidget(self.key_amount)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.apply_sett_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apply_sett_button.setFont(font)
        self.apply_sett_button.setObjectName("apply_sett_button")
        self.horizontalLayout_10.addWidget(self.apply_sett_button)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        spacerItem13 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem13)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem14 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.loger = QtWidgets.QTextBrowser(self.centralwidget)
        self.loger.setMinimumSize(QtCore.QSize(746, 192))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loger.setFont(font)
        self.loger.setObjectName("loger")
        self.horizontalLayout_6.addWidget(self.loger)
        spacerItem15 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem16 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem16)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem17 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setEnabled(False)
        self.start_button.setMinimumSize(QtCore.QSize(93, 28))
        self.start_button.setMaximumSize(QtCore.QSize(93, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_7.addWidget(self.start_button)
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.horizontalLayout_7.addWidget(self.progress_bar)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem18 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.key_amount.setEnabled(False)
        self.format_box.setEnabled(False)
        self.apply_sett_button.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PBF key generator"))
        self.label.setText(_translate("MainWindow", "First component"))
        self.label_2.setText(_translate("MainWindow", "Second component"))
        self.ZMK_button.setText(_translate("MainWindow", "Apply ZMK"))
        self.label_4.setText(_translate("MainWindow", "Format"))
        self.format_box.setItemText(0, _translate("MainWindow", "DEF"))
        self.format_box.setItemText(1, _translate("MainWindow", "MUL"))
        self.format_box.setItemText(2, _translate("MainWindow", "PSB"))
        self.format_box.setItemText(3, _translate("MainWindow", "BRS"))
        # self.format_box.setItemText(4, _translate("MainWindow", "MIB"))
        self.label_3.setText(_translate("MainWindow", "Amount of keys:"))
        self.apply_sett_button.setText(_translate("MainWindow", "Apply settings"))
        self.loger.setHtml(_translate("MainWindow",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; "
                                      "font-weight:400; font-style:normal;\">\n "
                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                      "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br "
                                      "/></p></body></html>"))
        self.start_button.setText(_translate("MainWindow", "START"))


class App(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.key = None
        self.path = None
        self.cypher = None
        self.file_name = None
        self.file_format = None
        self.zmk_check_val = None
        self.full_key_list = None
        self.key_list_2file = None
        self.amount_of_keys = None

        self.zmk_applied = False
        self.box_is_checked = False
        self.settings_applied = False
        self.setupUi(self)

        self.sec_is_enabled.stateChanged.connect(self.enable_sec_comp)
        self.ZMK_button.clicked.connect(self.apply_zmk)
        self.apply_sett_button.clicked.connect(self.apply_sett)
        self.start_button.clicked.connect(self.start_process)

    def start_process(self):
        self.ZMK_button.setEnabled(False)
        self.key_amount.setEnabled(False)
        self.format_box.setEnabled(False)
        self.first_comp.setEnabled(False)
        self.second_comp.setEnabled(False)
        self.start_button.setEnabled(False)
        self.sec_is_enabled.setEnabled(False)
        self.apply_sett_button.setEnabled(False)

        self.full_key_list = self.get_key_list(self.amount_of_keys)
        self.progress_bar.setValue(25)
        self.encode_key_list()
        self.progress_bar.setValue(50)
        self.write_in_file()

        self.loger.setText('File {} successfully generated!You can find it in "output" folder\n'
                           'Full path:\n{}'.format(self.file_name, os.path.join(os.getcwd(), self.path)))
        self.progress_bar.setValue(100)

    def write_in_file(self):
        def get_file_name(file_name=self.file_format + '_' + self.zmk_check_val + '_' + str(self.amount_of_keys),
                          file_form=None,
                          copy_number='',
                          counter=0):
            if(self.file_format == 'DEF' or
               self.file_format == 'PSB' or
               self.file_format == 'MUL'):
                file_form = '.keys'
            elif self.file_format == 'MIB':
                file_form = '.1keys'
            elif self.file_format == 'BRS':
                file_form = '.2keys'

            if counter > 0:
                copy_number = '(' + str(counter) + ')'

            self.path = os.path.join('output', file_name + copy_number + file_form)
            if os.path.exists(self.path):
                counter += 1
                return get_file_name(counter=counter)
            else:
                return file_name + copy_number + file_form

        def def_mode():
            start_of_file = '<?xml version="1.0"  encoding="windows-1251"?>\n' \
                            '<keyset>\n'
            structure = '<packet number="{}">\n' \
                        '<key type="KLKANSI" name="KLK" keyval="{}" checkval="{}"/>\n' \
                        '</packet>\n'
            end_of_file = '</keyset>'

            serial_number = 1
            full_string = start_of_file

            for keys in self.key_list_2file:
                encoded_key = keys[1]
                check_value = keys[2]
                full_string += structure.format(serial_number, encoded_key, check_value)
                serial_number += 1

            full_string += end_of_file

            self.progress_bar.setValue(75)
            return full_string

        def mul_mode():
            start_of_file = '<?xml version="1.0"  encoding="windows-1251"?>\n' \
                            '<keyset>\n'
            structure_1 = '<packet number="{}">\n' \
                          '<key type="KLKANSI" name="TMK_MAC" keyval="{}" checkval="{}"/>\n'
            structure_2 = '<key type="KLKANSI" name="TMK_PIN" keyval="{}" checkval="{}"/>\n' \
                          '</packet>\n'
            end_of_file = '</keyset>'

            serial_number = 1
            struct_changer = False
            full_string = start_of_file

            for keys in self.key_list_2file:
                encoded_key = keys[1]
                check_value = keys[2]
                if struct_changer:
                    full_string += structure_2.format(encoded_key, check_value)
                    struct_changer = False
                    serial_number += 1
                else:
                    full_string += structure_1.format(serial_number, encoded_key, check_value)
                    struct_changer = True

            full_string += end_of_file

            self.progress_bar.setValue(75)
            return full_string

        def brs_mode():
            start_of_file = '<?xml version="1.0"  encoding="windows-1251"?>\n' \
                            '<keyset>\n'
            structure = '<packet keynum="{}" serialPIN="{}" serialSAM="{}" KLK_LMK="{}" check3="{}" ' \
                        'zpkzmk="MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"/>\n'
            end_of_file = '</keyset>'

            serial_number = 1
            full_string = start_of_file

            for keys in self.key_list_2file:
                encoded_key = keys[1]
                check_value = keys[2]
                full_string += structure.format(serial_number, serial_number, serial_number, encoded_key, check_value)
                serial_number += 1

            full_string += end_of_file

            self.progress_bar.setValue(75)
            return full_string

        def write_data(data):
            self.file_name = get_file_name()
            directory = 'output\\' + self.file_name
            file = open(directory, 'w')
            file.write(data)
            file.close()

        if(self.file_format == 'DEF' or
           self.file_format == 'PSB'):
            write_data(def_mode())
        elif self.file_format == 'MUL':
            write_data(mul_mode())
        elif self.file_format == 'BRS':
            write_data(brs_mode())

    def encode_key_list(self):
        if self.key_list_2file is None:
            self.key_list_2file = []

        for single_key in self.full_key_list:
            res = self.cypher.encrypt(unhexlify(single_key))

            check_val_cypher = DES3.new(unhexlify(single_key), DES3.MODE_ECB)
            #check_val_cypher = pyDes.triple_des(unhexlify(single_key), pyDes.ECB)
            check_val = check_val_cypher.encrypt(unhexlify('00000000000000000000000000000000'))
            check_val = check_val.hex().upper()[:6]
            self.key_list_2file.append([single_key, res.hex().upper(), check_val])

    def get_key_list(self, num):
        def get_rand_key():
            def get_rand_16():
                if randint(0, 1):
                    return chr(randint(48, 57))
                else:
                    return chr(randint(65, 70))

            return ''.join([get_rand_16() for i in range(32)])

        if self.file_format == 'MUL':
            num *= 2

        key_list = []
        while len(key_list) != num:
            new_key = get_rand_key()
            if new_key not in key_list:
                key_list.append(new_key)

        self.progress_bar.setValue(25)
        return key_list

    def apply_zmk(self):
        if self.zmk_is_legal():
            self.key = self.zmk_compile()
            key_in_bytes = unhexlify(self.key)
            try:
                self.cypher = DES3.new(key_in_bytes, DES3.MODE_ECB)
                #self.cypher = pyDes.triple_des(key_in_bytes, pyDes.ECB)
                self.loger.setText('ZMK accepted!\nClear component:{}'.format(self.key))
                self.zmk_applied = True

                self.zmk_check_val = self.cypher.encrypt(unhexlify('00000000000000000000000000000000'))
                self.zmk_check_val = self.zmk_check_val.hex().upper()[:6]

                self.key_amount.setEnabled(True)
                self.format_box.setEnabled(True)
                self.apply_sett_button.setEnabled(True)
                if self.settings_applied:
                    self.start_button.setEnabled(True)
            except ValueError:
                self.loger.setText('Triple DES key degenerates to single DES.\n'
                                   'ZMK must be more secure!')
                self.start_button.setEnabled(False)

    def zmk_compile(self):
        def hex_splitter(zmk):
            template = re.compile('.{2}')
            return re.findall(template, zmk)

        zmk_1 = str(self.first_comp.text())
        if not self.box_is_checked:
            return zmk_1
        else:
            zmk_2 = str(self.second_comp.text())

        zmk_1 = hex_splitter(zmk_1)
        zmk_2 = hex_splitter(zmk_2)
        comp_zmk = ''
        for i in range(16):
            temp = hex(int(zmk_1[i], 16) ^ int(zmk_2[i], 16)).replace('0x', '')
            if len(temp) < 2: temp = '0' + temp
            comp_zmk += temp.upper()
        return comp_zmk

    def zmk_is_legal(self):
        template = re.compile(r'[0-9a-fA-F]{32}')
        if re.search(template, self.first_comp.text()):
            if ((self.box_is_checked and re.search(template, self.second_comp.text())) or
                    not self.box_is_checked):
                self.loger.setText('')
                return True
            else:
                self.loger.setText('[ERROR]Invalid ZMK!')
                self.start_button.setEnabled(False)
                return False
        else:
            self.loger.setText('[ERROR]Invalid ZMK!')
            self.start_button.setEnabled(False)
            return False

    def enable_sec_comp(self, state):
        if state == QtCore.Qt.Checked:
            self.second_comp.setEnabled(True)
            self.box_is_checked = True
        else:
            self.second_comp.setEnabled(False)
            self.box_is_checked = False

    def apply_sett(self):
        self.amount_of_keys = int(self.key_amount.value())
        self.file_format = str(self.format_box.currentText())

        self.settings_applied = True
        self.loger.setText('{}\nSettings applied!'.format(str(self.loger.toPlainText())))

        if self.zmk_applied:
            self.start_button.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
