import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsColorizeEffect
from PySide6.QtGui import QPixmap, QDoubleValidator, Qt, QColor, QPalette, QRegularExpressionValidator
from PySide6.QtCore import QFile, Qt, QLocale, QPropertyAnimation, QEasingCurve, QPoint, QVariantAnimation, QAbstractAnimation, QRegularExpression

from design import Ui_MainWindow

from pandas import read_excel


def get_style(name):  # получаем stylesheet из файла в каталоге static
    stylefile = QFile(f"./static/{name}")
    stylefile.open(QFile.OpenModeFlag.ReadOnly)
    return stylefile.readAll().toStdString()


class CustomDoubleValidator(QRegularExpressionValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Регулярное выражение для чисел с точкой или запятой
        self.setRegularExpression(QRegularExpression(r"^-?\d*[.,]?\d+$"))

    def validate(self, input, pos):
        # Заменяем запятые на точки
        input = input.replace(',', '.')
        return super().validate(input, pos)

    def fixup(self, input):
        return input.replace(',', '.')


class Atom(QMainWindow):
    def __init__(self):
        super(Atom, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        validator = CustomDoubleValidator(self)
        self.ui.lineEdit.setValidator(validator)
        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.change_type)
        self.ui.label_13.setStyleSheet(get_style("image.css"))
        self.ui.label_13.setPixmap(QPixmap(u"images/bsac.png"))
        self.ui.label_14.setStyleSheet(get_style("logo.css"))
        self.ui.label_14.setPixmap(QPixmap(u"images/bsac.png"))
        self.ui.label_16.setStyleSheet(get_style("log_default.css"))
        self.ui.pushButton.setStyleSheet(get_style("button.css"))
        self.ui.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        for i in range(9):
            exec(f'self.ui.label_{i + 4}.setStyleSheet(get_style("default.css"))')
            exec(f'self.ui.label_{i + 4}.setToolTip(get_style("label_{i + 4}.html"))')

    def change_type(self):
        if self.ui.pushButton_2.text() == "нВт":
            self.ui.pushButton_2.setText("дБм")
        else:
            self.ui.pushButton_2.setText("нВт")

        """ def enter_value_edit2(self):  # изменение lineEdit_2(дБм) при вводе в lineEdit(нВт)
                self.ui.lineEdit_2.setText("")
        
        def enter_value_edit1(self):  # изменение lineEdit(нВт) при вводе в lineEdit_2(дБм)
                self.ui.lineEdit.setText("")"""

    """def click(self):
        value_nvt = 0
        value_dbm = 0
        if self.ui.lineEdit.text() != "":
            value_nvt = float(self.ui.lineEdit.text())
        elif self.ui.lineEdit_2.text() != "":
            value_dbm = float(self.ui.lineEdit_2.text())
        else:
            pass
        data = read_excel('data.xlsx', nrows=10)
        convert = get_style('default.css')
        for i in range(9):  # делаем все label серыми
            exec(f'self.ui.label_{i + 4}.setStyleSheet(convert)')
        self.ui.label_16.setStyleSheet("background-color:#e6e6e6;border-radius: 5px;")
        check = True
        for i in range(9):
            # print(data['nvt_a'][i], value, data['nvt_b'][i])
            if data['nvt_a'][i] <= value_nvt <= data['nvt_b'][i] or data['dbm_a'][i] <= value_dbm <= data['dbm_b'][i]:
                convert = get_style('selected.css')
                exec(f'self.ui.label_{i + 4}.setStyleSheet(convert)')
                pixmap = QPixmap(f'./images/{data["image"][i]}')
                self.ui.label_13.setPixmap(pixmap)
                self.ui.label_16.setStyleSheet("background-color: rgb(120, 183, 140);border-radius: 5px;")
                self.ui.label_16.setText("")
                check = False
        if check:
            self.ui.label_16.setStyleSheet("background-color:#f07575;text-align:center;border-radius: 5px;font: 600 italic 10pt \"Open Sans SemiBold\";")
            self.ui.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui.label_13.setPixmap(QPixmap("./images/bsac.png"))
            self.ui.label_16.setText("Вещество не определено")"""
    def keyPressEvent(self, event):
        # если нажата клавиша F11
        if event.key() == Qt.Key.Key_F11:
            # если в полный экран
            if self.isFullScreen():
                # вернуть прежнее состояние
                self.showNormal()
            else:
                # иначе во весь экран
                self.showFullScreen()

    def click(self):
        self.cubik()
        value_nvt = 0
        value_dbm = 0
        if self.ui.lineEdit.text() != '':
            if self.ui.pushButton_2.text() == "дБм":
                value_dbm = float(self.ui.lineEdit.text())
            else:
                value_nvt = float(self.ui.lineEdit.text())
        data = read_excel('data.xlsx', nrows=10)
        convert = get_style('default.css')
        for i in range(9):  # делаем все label серыми
            exec(f'self.ui.label_{i + 4}.setStyleSheet(convert)')
        self.ui.label_16.setStyleSheet("background-color:#e6e6e6;border-radius: 5px;")
        check = True
        for i in range(9):
            # print(data['nvt_a'][i], value, data['nvt_b'][i])
            if data['nvt_a'][i] <= value_nvt <= data['nvt_b'][i] or data['dbm_a'][i] <= value_dbm <= data['dbm_b'][i]:
                convert = get_style('selected.css')
                exec(f'self.ui.label_{i + 4}.setStyleSheet(convert)')
                pixmap = QPixmap(f'./images/{data["image"][i]}')
                self.ui.label_13.setPixmap(pixmap)
                self.ui.label_16.setStyleSheet(get_style("log_green.css"))
                self.ui.label_16.setText("Вещество определено")
                self.ui.pushButton_3.setStyleSheet(get_style("cub_green.css"))
                check = False

        if check:
            self.ui.label_16.setStyleSheet(get_style("log_red.css"))
            self.ui.label_16.setText("Вещество не определено")
            self.ui.label_13.setPixmap(QPixmap("./images/bsac.png"))
            self.ui.pushButton_3.setStyleSheet(get_style("cub_red.css"))
    f = True

    def cubik(self):
        self.ui.anim = QPropertyAnimation(self.ui.pushButton_3, b"pos")
        self.ui.anim.setStartValue(QColor(120, 183, 140))
        self.ui.anim.setEasingCurve(QEasingCurve.InOutCubic)
        x_cord = self.ui.pushButton_3.pos().x()
        y_cord = self.ui.pushButton_3.pos().y()

        #print(x_cord, y_cord)
        if self.f:
            self.ui.anim.setStartValue(QPoint(x_cord, y_cord))
            self.ui.anim.setEndValue(QPoint(400, 310))
            self.f = False
        else:
            self.ui.anim.setStartValue(QPoint(x_cord, y_cord))
            self.ui.anim.setEndValue(QPoint(400, 370))
            self.f = True

        self.ui.anim.setDuration(800)
        self.ui.anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Atom()
    window.show()

    sys.exit(app.exec())