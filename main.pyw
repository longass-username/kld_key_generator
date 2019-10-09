from PyQt5 import QtCore, QtGui, QtWidgets
from Cryptodome.Cipher import DES3
from binascii import unhexlify
from random import randint
import qt_window
import sys
import re
import os


class App(QtWidgets.QMainWindow, qt_window.Ui_MainWindow):

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
            if not os.path.exists(os.path.join(os.getcwd(), 'output')):
                os.makedirs(os.path.join(os.getcwd(), 'output'))

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
