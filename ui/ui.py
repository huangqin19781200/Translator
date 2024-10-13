from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QSize(900, 500))
        icon = QIcon()
        icon.addFile(u":/images/icon/winlogo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 2.0 55 Regular"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* \u5168\u5c40\u8bbe\u7f6e */\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 12pt \"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 2.0 55 Regular\";\n"
"}\n"
"QMainWindow {\n"
"	border: none;\n"
"}\n"
"\n"
"/* \u9876\u90e8\u680f */\n"
"#frameTopBackground {	\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"#frameTopBackground .QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"}\n"
"#frameTopBackground .QPushButton:hover {\n"
"	background-color: rgb(44, 49, 57);\n"
"	border-style: solid;\n"
"}\n"
"#frameTopBackground .QPushButton:pressed {\n"
"	background-color: rgb(23, 26, 30);\n"
"	border-style: solid;\n"
"}\n"
"\n"
"/* \u4e2d\u95f4\u680f */\n"
"#frameContent {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* \u5e95\u90e8\u680f */\n"
"#frameBottomBackground {	\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
""
                        "/* \u6309\u94ae */\n"
"#frameContent QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#frameContent QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#frameContent QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* \u591a\u884c\u8f93\u5165\u6846 */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761 */\n"
"QScrollBar:vertical {\n"
"	bord"
                        "er: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 0px 0 0px 0;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
"}")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.frameAppBackground = QFrame(self.styleSheet)
        self.frameAppBackground.setObjectName(u"frameAppBackground")
        self.frameAppBackground.setStyleSheet(u"")
        self.frameAppBackground.setFrameShape(QFrame.Shape.NoFrame)
        self.frameAppBackground.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frameAppBackground)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameTopBackground = QFrame(self.frameAppBackground)
        self.frameTopBackground.setObjectName(u"frameTopBackground")
        self.frameTopBackground.setMinimumSize(QSize(0, 50))
        self.frameTopBackground.setMaximumSize(QSize(16777215, 50))
        self.frameTopBackground.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTopBackground.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frameTopBackground)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 10, 0)
        self.btnClose = QPushButton(self.frameTopBackground)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(50, 50))
        self.btnClose.setMaximumSize(QSize(50, 50))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClose.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/icon/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon1)
        self.btnClose.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btnClose, 0, 4, 1, 1)

        self.frameTopLogo = QFrame(self.frameTopBackground)
        self.frameTopLogo.setObjectName(u"frameTopLogo")
        self.frameTopLogo.setMinimumSize(QSize(50, 50))
        self.frameTopLogo.setMaximumSize(QSize(50, 50))
        self.frameTopLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTopLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.logo = QFrame(self.frameTopLogo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 5, 42, 42))
        self.logo.setMinimumSize(QSize(42, 42))
        self.logo.setMaximumSize(QSize(42, 42))
        self.logo.setStyleSheet(u"background-image: url(:/images/icon/logo.png);")
        self.logo.setFrameShape(QFrame.Shape.NoFrame)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frameTopLogo, 0, 0, 1, 1)

        self.btnMinimize = QPushButton(self.frameTopBackground)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(50, 50))
        self.btnMinimize.setMaximumSize(QSize(50, 50))
        self.btnMinimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/icon/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMinimize.setIcon(icon2)
        self.btnMinimize.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btnMinimize, 0, 2, 1, 1)

        self.btnMaximizeRestore = QPushButton(self.frameTopBackground)
        self.btnMaximizeRestore.setObjectName(u"btnMaximizeRestore")
        self.btnMaximizeRestore.setMinimumSize(QSize(50, 50))
        self.btnMaximizeRestore.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 2.0 55 Regular"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.btnMaximizeRestore.setFont(font1)
        self.btnMaximizeRestore.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/icon/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMaximizeRestore.setIcon(icon3)
        self.btnMaximizeRestore.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btnMaximizeRestore, 0, 3, 1, 1)

        self.widgetTop = QWidget(self.frameTopBackground)
        self.widgetTop.setObjectName(u"widgetTop")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetTop.sizePolicy().hasHeightForWidth())
        self.widgetTop.setSizePolicy(sizePolicy)
        self.widgetTop.setMinimumSize(QSize(0, 50))
        self.widgetTop.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.widgetTop)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelTitleInfo = QLabel(self.widgetTop)
        self.labelTitleInfo.setObjectName(u"labelTitleInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelTitleInfo.sizePolicy().hasHeightForWidth())
        self.labelTitleInfo.setSizePolicy(sizePolicy1)
        self.labelTitleInfo.setMinimumSize(QSize(0, 0))
        self.labelTitleInfo.setMaximumSize(QSize(16777215, 16777215))
        self.labelTitleInfo.setFont(font)
        self.labelTitleInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.labelTitleInfo)


        self.gridLayout.addWidget(self.widgetTop, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frameTopBackground)

        self.contentBox = QFrame(self.frameAppBackground)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameContent = QFrame(self.contentBox)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"")
        self.frameContent.setFrameShape(QFrame.Shape.NoFrame)
        self.frameContent.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frameContent)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.widgetButtons_2 = QWidget(self.frameContent)
        self.widgetButtons_2.setObjectName(u"widgetButtons_2")
        self.gridLayout_4 = QGridLayout(self.widgetButtons_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnSet = QPushButton(self.widgetButtons_2)
        self.btnSet.setObjectName(u"btnSet")
        self.btnSet.setMinimumSize(QSize(150, 30))
        self.btnSet.setMaximumSize(QSize(16777215, 16777215))
        self.btnSet.setFont(font)
        self.btnSet.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btnSet, 0, 2, 1, 1)

        self.btnAppend = QPushButton(self.widgetButtons_2)
        self.btnAppend.setObjectName(u"btnAppend")
        self.btnAppend.setMinimumSize(QSize(150, 30))
        self.btnAppend.setMaximumSize(QSize(16777215, 16777215))
        self.btnAppend.setFont(font)
        self.btnAppend.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btnAppend, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widgetButtons_2, 3, 0, 1, 1)

        self.plainTextEditOutput = QPlainTextEdit(self.frameContent)
        self.plainTextEditOutput.setObjectName(u"plainTextEditOutput")
        self.plainTextEditOutput.setMinimumSize(QSize(100, 100))
        self.plainTextEditOutput.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.plainTextEditOutput, 2, 3, 1, 1)

        self.plainTextEditInput = QPlainTextEdit(self.frameContent)
        self.plainTextEditInput.setObjectName(u"plainTextEditInput")
        self.plainTextEditInput.setMinimumSize(QSize(100, 100))
        self.plainTextEditInput.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.plainTextEditInput, 2, 0, 1, 1)

        self.widgetButtons_3 = QWidget(self.frameContent)
        self.widgetButtons_3.setObjectName(u"widgetButtons_3")
        self.gridLayout_5 = QGridLayout(self.widgetButtons_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.comboxSelect = QComboBox(self.widgetButtons_3)
        self.comboxSelect.addItem("")
        self.comboxSelect.addItem("")
        self.comboxSelect.addItem("")
        self.comboxSelect.addItem("")
        self.comboxSelect.addItem("")
        self.comboxSelect.addItem("")
        self.comboxSelect.setObjectName(u"comboxSelect")
        self.comboxSelect.setMinimumSize(QSize(150, 30))
        self.comboxSelect.setMaximumSize(QSize(16777215, 16777215))
        self.comboxSelect.setFont(font)
        self.comboxSelect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboxSelect.setStyleSheet(u"QComboBox{\n"
"	background: transparent;\n"
"	border-radius: 5px;\n"
"	border: 2px solid transparent;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	width: 25px; \n"
"	background-image: url(:/images/icon/arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(40, 44, 52);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.gridLayout_5.addWidget(self.comboxSelect, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_3.addWidget(self.widgetButtons_3, 0, 0, 1, 4)

        self.widgetButtons = QWidget(self.frameContent)
        self.widgetButtons.setObjectName(u"widgetButtons")
        self.gridLayout_2 = QGridLayout(self.widgetButtons)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnClearOutput = QPushButton(self.widgetButtons)
        self.btnClearOutput.setObjectName(u"btnClearOutput")
        self.btnClearOutput.setMinimumSize(QSize(150, 30))
        self.btnClearOutput.setMaximumSize(QSize(16777215, 16777215))
        self.btnClearOutput.setFont(font)
        self.btnClearOutput.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/icon/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClearOutput.setIcon(icon4)

        self.gridLayout_2.addWidget(self.btnClearOutput, 0, 1, 1, 1)

        self.btnClearInput = QPushButton(self.widgetButtons)
        self.btnClearInput.setObjectName(u"btnClearInput")
        self.btnClearInput.setMinimumSize(QSize(150, 30))
        self.btnClearInput.setMaximumSize(QSize(16777215, 16777215))
        self.btnClearInput.setFont(font)
        self.btnClearInput.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnClearInput.setIcon(icon4)

        self.gridLayout_2.addWidget(self.btnClearInput, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widgetButtons, 3, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frameContent)


        self.verticalLayout.addWidget(self.contentBox)

        self.frameBottomBackground = QFrame(self.frameAppBackground)
        self.frameBottomBackground.setObjectName(u"frameBottomBackground")
        self.frameBottomBackground.setMinimumSize(QSize(0, 22))
        self.frameBottomBackground.setMaximumSize(QSize(16777215, 22))
        self.frameBottomBackground.setFrameShape(QFrame.Shape.NoFrame)
        self.frameBottomBackground.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frameBottomBackground)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelCredits = QLabel(self.frameBottomBackground)
        self.labelCredits.setObjectName(u"labelCredits")
        self.labelCredits.setMinimumSize(QSize(0, 22))
        self.labelCredits.setMaximumSize(QSize(16777215, 22))
        self.labelCredits.setFont(font)
        self.labelCredits.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.labelCredits)

        self.labelVersion = QLabel(self.frameBottomBackground)
        self.labelVersion.setObjectName(u"labelVersion")
        self.labelVersion.setMinimumSize(QSize(0, 22))
        self.labelVersion.setMaximumSize(QSize(16777215, 22))
        self.labelVersion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.labelVersion)

        self.widgetBottomBar = QWidget(self.frameBottomBackground)
        self.widgetBottomBar.setObjectName(u"widgetBottomBar")
        self.widgetBottomBar.setMinimumSize(QSize(22, 22))
        self.widgetBottomBar.setMaximumSize(QSize(22, 16777215))
        self.widgetBottomBar.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.horizontalLayout_6 = QHBoxLayout(self.widgetBottomBar)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frameSizeGrip = QFrame(self.widgetBottomBar)
        self.frameSizeGrip.setObjectName(u"frameSizeGrip")
        self.frameSizeGrip.setMinimumSize(QSize(10, 10))
        self.frameSizeGrip.setMaximumSize(QSize(10, 10))
        self.frameSizeGrip.setCursor(QCursor(Qt.CursorShape.SizeFDiagCursor))
        self.frameSizeGrip.setStyleSheet(u"background-image: url(:/images/icon/size-grip.png);")
        self.frameSizeGrip.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSizeGrip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_6.addWidget(self.frameSizeGrip)


        self.horizontalLayout_7.addWidget(self.widgetBottomBar)


        self.verticalLayout.addWidget(self.frameBottomBackground)


        self.appMargins.addWidget(self.frameAppBackground)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        self.btnClose.setToolTip("")

        self.btnClose.setText("")

        self.btnMinimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))

        self.btnMinimize.setText("")

        self.btnMaximizeRestore.setToolTip("")

        self.btnMaximizeRestore.setText("")
        self.labelTitleInfo.setText(QCoreApplication.translate("MainWindow", u"Translator - can help you learn the language", None))
        self.btnSet.setText(QCoreApplication.translate("MainWindow", u"\u8986\u76d6\u7ffb\u8bd1", None))
        self.btnAppend.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u52a0\u7ffb\u8bd1", None))
        self.plainTextEditOutput.setPlainText("")
        self.plainTextEditInput.setPlainText("")
        self.comboxSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"English  >>  \u4e2d\u6587", None))
        self.comboxSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u6587  >>  English", None))
        self.comboxSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439  >>  \u4e2d\u6587", None))
        self.comboxSelect.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e2d\u6587  >>  \u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.comboxSelect.setItemText(4, QCoreApplication.translate("MainWindow", u"\u65e5\u672c\u8a9e  >>  \u4e2d\u6587", None))
        self.comboxSelect.setItemText(5, QCoreApplication.translate("MainWindow", u"\u4e2d\u6587  >>  \u65e5\u672c\u8a9e", None))

        self.btnClearOutput.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u51fa", None))
        self.btnClearInput.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u5165", None))
        self.labelCredits.setText(QCoreApplication.translate("MainWindow", u"  Created by HGG", None))
        self.labelVersion.setText(QCoreApplication.translate("MainWindow", u"v1.2.0", None))