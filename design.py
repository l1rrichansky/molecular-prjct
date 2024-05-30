# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QIcon(QIcon.fromTheme(u"appointment-new"))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 50, 1141, 201))
        self.label.setStyleSheet(u"font: 800 50pt \"Open Sans ExtraBold\";\n"
"")
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(430, 310, 341, 81))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 10px solid white;\n"
"font: 800 36pt \"Open Sans ExtraBold\";\n"
"")
        self.lineEdit.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(580, 530, 351, 101))
        self.label_4.setCursor(QCursor(Qt.WhatsThisCursor))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(u"<html><head/><body><p><span style=\" font-weight:700;\">\u0411\u044b\u0432\u0430\u0435\u0442</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_4.setToolTipDuration(-1)
        self.label_4.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(950, 530, 331, 101))
        self.label_5.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_5.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1300, 530, 531, 101))
        self.label_6.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_6.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(580, 650, 611, 101))
        self.label_7.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_7.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(580, 770, 671, 101))
        self.label_8.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_8.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1270, 770, 561, 101))
        self.label_9.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_9.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1210, 650, 621, 101))
        self.label_10.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_10.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(580, 890, 651, 101))
        self.label_11.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_11.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(940, 310, 551, 81))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 183, 140);\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 30pt \"Open Sans ExtraBold\";\n"
"")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(1250, 890, 581, 101))
        self.label_12.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_12.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 530, 461, 461))
        self.label_13.setStyleSheet(u"border-radius: 20px;       \n"
"background-color: #e6e6e6;")
        self.label_13.setPixmap(QPixmap(u":/images/RyLl-E9w_400x400.jpg"))
        self.label_13.setScaledContents(True)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(90, 260, 1741, 31))
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setLineWidth(8)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(300, 60, 201, 191))
        self.label_14.setStyleSheet(u"background-color:#e6e6e6;")
        self.label_14.setPixmap(QPixmap(u":/images/RyLl-E9w_400x400.jpg"))
        self.label_14.setScaledContents(True)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(90, 420, 1741, 31))
        self.line_2.setStyleSheet(u"")
        self.line_2.setLineWidth(8)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(90, 460, 1741, 51))
        self.label_16.setStyleSheet(u"background-color:#e6e6e6;\n"
"font: 9pt \"Segoe UI\";\n"
"border-radius: 20px;                     /* <----  20px  */ \n"
"border: 4px solid #A0A0A0;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(780, 320, 141, 61))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background:rgba(255,255,255,0);\n"
"font: 800 italic 46pt \"Open Sans ExtraBold\";\n"
"\n"
"")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(400, 370, 16, 16))
        self.pushButton_3.setCursor(QCursor(Qt.CrossCursor))
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: #b6b6b6;\n"
"border-radius: 5px;                     /* <----  20px  */ \n"
"border: 0px solid #094065;\n"
"font: 800 20pt \"Open Sans ExtraBold\";\n"
"")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(1060, 400, 431, 20))
        self.label_17.setStyleSheet(u"font: 600 italic 15pt \"Open Sans SemiBold\";")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(1630, 10, 281, 20))
        self.label_18.setStyleSheet(u"font: 600 italic 15pt \"Open Sans SemiBold\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u0438 \u0438 \u0432\u0438\u0434\u0430 \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u043e\u0440\u0443\u0441\u0441\u043a\u0430\u044f \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0430\u043a\u0430\u0434\u0435\u043c\u0438\u044f \u0441\u0432\u044f\u0437\u0438", None))
#if QT_CONFIG(statustip)
        self.label_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0440\u0435", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u043f\u043f\u0440\u0430\u0440</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0434\u0443\u0445", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0434\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0442 \u044d\u0442\u0438\u043b\u043e\u0432\u044b\u0439 40%", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0442 \u044d\u0442\u0438\u043b\u043e\u0432\u044b\u0439 70%", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0442 \u0438\u0437\u043e\u043f\u0440\u043e\u043f\u0438\u043b\u043e\u0432\u044b\u0439", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043d\u0437\u0438\u043d 92", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c 646", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u043b\u043e \u0440\u0430\u0441\u0442\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0435\u0449\u0435\u0441\u0442\u0432\u043e", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0438\u0446\u0435\u0440\u0438\u043d", None))
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_16.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0412\u0442", None))
        self.pushButton_3.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"*\u0434\u043b\u044f \u0441\u043c\u0435\u043d\u044b \u0440\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043d\u0435\u0451", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"F11 - \u041f\u043e\u043b\u043d\u043e\u044d\u043a\u0440\u0430\u043d\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c", None))
    # retranslateUi

