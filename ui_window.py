from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
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
"/* \u7a0b\u5e8f\u80cc\u666f */\n"
"#frameAppBackground {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"/* \u9876\u90e8\u680f */\n"
"#frameTopBackground {	\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"#frameTopButtons .QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"#frameTopButtons .QPushButton:hover {\n"
"	background-color: rgb(44, 49, 57);\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
""
                        "}\n"
"#frameTopButtons .QPushButton:pressed {\n"
"	background-color: rgb(23, 26, 30);\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"/* \u5e95\u90e8\u680f */\n"
"#frameBottomBackground {	\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
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
"	sele"
                        "ction-background-color: rgb(255, 121, 198);\n"
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
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
" }\n"
"QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"	border-radius: 4px\n"
" }\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: rgb(55, 63, 77);\n"
" }\n"
"\n"
"/* \u9009\u9879\u76d2 */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:ho"
                        "ver{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/images/icon/arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
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
        self.widgetTop = QWidget(self.frameTopBackground)
        self.widgetTop.setObjectName(u"widgetTop")
        self.widgetTop.setMinimumSize(QSize(0, 50))
        self.widgetTop.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.widgetTop)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelTitleInfo = QLabel(self.widgetTop)
        self.labelTitleInfo.setObjectName(u"labelTitleInfo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitleInfo.sizePolicy().hasHeightForWidth())
        self.labelTitleInfo.setSizePolicy(sizePolicy)
        self.labelTitleInfo.setMinimumSize(QSize(0, 0))
        self.labelTitleInfo.setMaximumSize(QSize(16777215, 16777215))
        self.labelTitleInfo.setFont(font)
        self.labelTitleInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.labelTitleInfo)


        self.gridLayout.addWidget(self.widgetTop, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frameTopButtons = QFrame(self.frameTopBackground)
        self.frameTopButtons.setObjectName(u"frameTopButtons")
        self.frameTopButtons.setMinimumSize(QSize(0, 50))
        self.frameTopButtons.setMaximumSize(QSize(16777215, 50))
        self.frameTopButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTopButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frameTopButtons)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btnMinimize = QPushButton(self.frameTopButtons)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(28, 28))
        self.btnMinimize.setMaximumSize(QSize(28, 28))
        self.btnMinimize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/icon/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMinimize.setIcon(icon)
        self.btnMinimize.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.btnMinimize)

        self.btnMaximizeRestore = QPushButton(self.frameTopButtons)
        self.btnMaximizeRestore.setObjectName(u"btnMaximizeRestore")
        self.btnMaximizeRestore.setMinimumSize(QSize(28, 28))
        self.btnMaximizeRestore.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 2.0 55 Regular"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.btnMaximizeRestore.setFont(font1)
        self.btnMaximizeRestore.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/icon/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMaximizeRestore.setIcon(icon1)
        self.btnMaximizeRestore.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.btnMaximizeRestore)

        self.btnClose = QPushButton(self.frameTopButtons)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(28, 28))
        self.btnClose.setMaximumSize(QSize(28, 28))
        self.btnClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/icon/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon2)
        self.btnClose.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.btnClose)


        self.gridLayout.addWidget(self.frameTopButtons, 0, 3, 1, 1, Qt.AlignmentFlag.AlignRight)

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

        self.gridLayout.addWidget(self.frameTopLogo, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)


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
        self.verticalLayout_15 = QVBoxLayout(self.frameContent)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.widgetContent = QWidget(self.frameContent)
        self.widgetContent.setObjectName(u"widgetContent")
        self.horizontalLayout_4 = QHBoxLayout(self.widgetContent)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.plainTextEditInput = QPlainTextEdit(self.widgetContent)
        self.plainTextEditInput.setObjectName(u"plainTextEditInput")
        self.plainTextEditInput.setMinimumSize(QSize(100, 100))
        self.plainTextEditInput.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.plainTextEditInput)

        self.plainTextEditOutput = QPlainTextEdit(self.widgetContent)
        self.plainTextEditOutput.setObjectName(u"plainTextEditOutput")
        self.plainTextEditOutput.setMinimumSize(QSize(100, 100))
        self.plainTextEditOutput.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.plainTextEditOutput)


        self.verticalLayout_15.addWidget(self.widgetContent)

        self.widgetButtons = QWidget(self.frameContent)
        self.widgetButtons.setObjectName(u"widgetButtons")
        self.verticalLayout_16 = QVBoxLayout(self.widgetButtons)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btnSet = QPushButton(self.widgetButtons)
        self.btnSet.setObjectName(u"btnSet")
        self.btnSet.setMinimumSize(QSize(150, 30))
        self.btnSet.setMaximumSize(QSize(16777215, 16777215))
        self.btnSet.setFont(font)

        self.verticalLayout_16.addWidget(self.btnSet)

        self.btnAppend = QPushButton(self.widgetButtons)
        self.btnAppend.setObjectName(u"btnAppend")
        self.btnAppend.setMinimumSize(QSize(150, 30))
        self.btnAppend.setMaximumSize(QSize(16777215, 16777215))
        self.btnAppend.setFont(font)

        self.verticalLayout_16.addWidget(self.btnAppend)

        self.btnClearInput = QPushButton(self.widgetButtons)
        self.btnClearInput.setObjectName(u"btnClearInput")
        self.btnClearInput.setMinimumSize(QSize(150, 30))
        self.btnClearInput.setMaximumSize(QSize(16777215, 16777215))
        self.btnClearInput.setFont(font)

        self.verticalLayout_16.addWidget(self.btnClearInput)

        self.btnClearOutput = QPushButton(self.widgetButtons)
        self.btnClearOutput.setObjectName(u"btnClearOutput")
        self.btnClearOutput.setMinimumSize(QSize(150, 30))
        self.btnClearOutput.setMaximumSize(QSize(16777215, 16777215))
        self.btnClearOutput.setFont(font)

        self.verticalLayout_16.addWidget(self.btnClearOutput)

        self.comboxSelect = QComboBox(self.widgetButtons)
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

        self.verticalLayout_16.addWidget(self.comboxSelect)


        self.verticalLayout_15.addWidget(self.widgetButtons)


        self.verticalLayout_2.addWidget(self.frameContent)

        self.frameBottomBackground = QFrame(self.contentBox)
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
        self.frameSizeGrip.setStyleSheet(u"background-image: url(:/images/icon/size-grip.png);")
        self.frameSizeGrip.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSizeGrip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_6.addWidget(self.frameSizeGrip)


        self.horizontalLayout_7.addWidget(self.widgetBottomBar)


        self.verticalLayout_2.addWidget(self.frameBottomBackground)


        self.verticalLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.frameAppBackground)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTitleInfo.setText(QCoreApplication.translate("MainWindow", u"Translator - can help you learn the language", None))
        self.btnMinimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        self.btnMinimize.setText("")
        self.btnMaximizeRestore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        self.btnMaximizeRestore.setText("")
        self.btnClose.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        self.btnClose.setText("")
        self.plainTextEditInput.setPlainText("")
        self.plainTextEditOutput.setPlainText("")
        self.btnSet.setText(QCoreApplication.translate("MainWindow", u"\u8986\u76d6\u7ffb\u8bd1", None))
        self.btnAppend.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u52a0\u7ffb\u8bd1", None))
        self.btnClearInput.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u5165", None))
        self.btnClearOutput.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u51fa", None))
        self.comboxSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"English >> \u4e2d\u6587", None))
        self.comboxSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65e5\u672c\u8a9e >> \u4e2d\u6587", None))
        self.comboxSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439 >> \u4e2d\u6587", None))
        self.comboxSelect.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e2d\u6587 >> English", None))
        self.comboxSelect.setItemText(4, QCoreApplication.translate("MainWindow", u"\u4e2d\u6587 >> \u65e5\u672c\u8a9e", None))
        self.comboxSelect.setItemText(5, QCoreApplication.translate("MainWindow", u"\u4e2d\u6587 >> \u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))

        self.labelCredits.setText(QCoreApplication.translate("MainWindow", u"  Created by HGG", None))
        self.labelVersion.setText(QCoreApplication.translate("MainWindow", u"v1.41006", None))
