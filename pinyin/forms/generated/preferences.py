# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/preferences.ui'
#
# Created: Thu Jun 11 00:50:25 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(900, 650)
        self.gridLayout = QtGui.QGridLayout(Preferences)
        self.gridLayout.setObjectName("gridLayout")
        self.livePreviewGroupBox = QtGui.QGroupBox(Preferences)
        self.livePreviewGroupBox.setObjectName("livePreviewGroupBox")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.livePreviewGroupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fieldsFrame = QtGui.QFrame(self.livePreviewGroupBox)
        self.fieldsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fieldsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.fieldsFrame.setObjectName("fieldsFrame")
        self.verticalLayout_8.addWidget(self.fieldsFrame)
        self.gridLayout.addWidget(self.livePreviewGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Preferences)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.textTab = QtGui.QWidget()
        self.textTab.setObjectName("textTab")
        self.verticalLayout = QtGui.QVBoxLayout(self.textTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hanziPinyinSettingsFrame = QtGui.QGroupBox(self.textTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hanziPinyinSettingsFrame.sizePolicy().hasHeightForWidth())
        self.hanziPinyinSettingsFrame.setSizePolicy(sizePolicy)
        self.hanziPinyinSettingsFrame.setObjectName("hanziPinyinSettingsFrame")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.hanziPinyinSettingsFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pinyinTonesLabel = QtGui.QLabel(self.hanziPinyinSettingsFrame)
        self.pinyinTonesLabel.setObjectName("pinyinTonesLabel")
        self.verticalLayout_5.addWidget(self.pinyinTonesLabel)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.numericPinyinTonesRadio = QtGui.QRadioButton(self.hanziPinyinSettingsFrame)
        self.numericPinyinTonesRadio.setChecked(True)
        self.numericPinyinTonesRadio.setObjectName("numericPinyinTonesRadio")
        self.verticalLayout_7.addWidget(self.numericPinyinTonesRadio)
        self.tonifiedPinyinTonesRadio = QtGui.QRadioButton(self.hanziPinyinSettingsFrame)
        self.tonifiedPinyinTonesRadio.setObjectName("tonifiedPinyinTonesRadio")
        self.verticalLayout_7.addWidget(self.tonifiedPinyinTonesRadio)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.hanziLabel = QtGui.QLabel(self.hanziPinyinSettingsFrame)
        self.hanziLabel.setObjectName("hanziLabel")
        self.verticalLayout_5.addWidget(self.hanziLabel)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.simplifiedHanziRadio = QtGui.QRadioButton(self.hanziPinyinSettingsFrame)
        self.simplifiedHanziRadio.setChecked(True)
        self.simplifiedHanziRadio.setObjectName("simplifiedHanziRadio")
        self.verticalLayout_13.addWidget(self.simplifiedHanziRadio)
        self.traditionalHanziRadio = QtGui.QRadioButton(self.hanziPinyinSettingsFrame)
        self.traditionalHanziRadio.setObjectName("traditionalHanziRadio")
        self.verticalLayout_13.addWidget(self.traditionalHanziRadio)
        self.verticalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout.addWidget(self.hanziPinyinSettingsFrame)
        self.meaningsSettingsFrame = QtGui.QGroupBox(self.textTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meaningsSettingsFrame.sizePolicy().hasHeightForWidth())
        self.meaningsSettingsFrame.setSizePolicy(sizePolicy)
        self.meaningsSettingsFrame.setObjectName("meaningsSettingsFrame")
        self.gridLayout_2 = QtGui.QGridLayout(self.meaningsSettingsFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.languageLabel = QtGui.QLabel(self.meaningsSettingsFrame)
        self.languageLabel.setObjectName("languageLabel")
        self.gridLayout_2.addWidget(self.languageLabel, 3, 0, 1, 1)
        self.languageCombo = QtGui.QComboBox(self.meaningsSettingsFrame)
        self.languageCombo.setObjectName("languageCombo")
        self.gridLayout_2.addWidget(self.languageCombo, 4, 0, 1, 1)
        self.googleTranslateCheck = QtGui.QCheckBox(self.meaningsSettingsFrame)
        self.googleTranslateCheck.setObjectName("googleTranslateCheck")
        self.gridLayout_2.addWidget(self.googleTranslateCheck, 5, 0, 1, 1)
        self.seperateMeasureWordCheck = QtGui.QCheckBox(self.meaningsSettingsFrame)
        self.seperateMeasureWordCheck.setObjectName("seperateMeasureWordCheck")
        self.gridLayout_2.addWidget(self.seperateMeasureWordCheck, 1, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.numberingLabel = QtGui.QLabel(self.meaningsSettingsFrame)
        self.numberingLabel.setObjectName("numberingLabel")
        self.gridLayout_5.addWidget(self.numberingLabel, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.circledChineseNumberingRadio = QtGui.QRadioButton(self.meaningsSettingsFrame)
        self.circledChineseNumberingRadio.setChecked(True)
        self.circledChineseNumberingRadio.setObjectName("circledChineseNumberingRadio")
        self.verticalLayout_3.addWidget(self.circledChineseNumberingRadio)
        self.circledArabicNumberingRadio = QtGui.QRadioButton(self.meaningsSettingsFrame)
        self.circledArabicNumberingRadio.setObjectName("circledArabicNumberingRadio")
        self.verticalLayout_3.addWidget(self.circledArabicNumberingRadio)
        self.plainNumberingRadio = QtGui.QRadioButton(self.meaningsSettingsFrame)
        self.plainNumberingRadio.setObjectName("plainNumberingRadio")
        self.verticalLayout_3.addWidget(self.plainNumberingRadio)
        self.noNumberingRadio = QtGui.QRadioButton(self.meaningsSettingsFrame)
        self.noNumberingRadio.setObjectName("noNumberingRadio")
        self.verticalLayout_3.addWidget(self.noNumberingRadio)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.seperatorLabel = QtGui.QLabel(self.meaningsSettingsFrame)
        self.seperatorLabel.setObjectName("seperatorLabel")
        self.gridLayout_5.addWidget(self.seperatorLabel, 0, 1, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.linesSeperatorRadio = QtGui.QRadioButton(self.meaningsSettingsFrame)
        self.linesSeperatorRadio.setChecked(True)
        self.linesSeperatorRadio.setObjectName("linesSeperatorRadio")
        self.verticalLayout_4.addWidget(self.linesSeperatorRadio)
        self.commasSeperatorRadio = QtGui.QRadioButton(self.meaningsSettingsFrame)
        self.commasSeperatorRadio.setObjectName("commasSeperatorRadio")
        self.verticalLayout_4.addWidget(self.commasSeperatorRadio)
        self.customSeperatorRadio = QtGui.QRadioButton(self.meaningsSettingsFrame)
        self.customSeperatorRadio.setObjectName("customSeperatorRadio")
        self.verticalLayout_4.addWidget(self.customSeperatorRadio)
        self.customSeperatorLineEdit = QtGui.QLineEdit(self.meaningsSettingsFrame)
        self.customSeperatorLineEdit.setObjectName("customSeperatorLineEdit")
        self.verticalLayout_4.addWidget(self.customSeperatorLineEdit)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 6, 0, 1, 1)
        self.hanziMaskingCheck = QtGui.QCheckBox(self.meaningsSettingsFrame)
        self.hanziMaskingCheck.setObjectName("hanziMaskingCheck")
        self.gridLayout_2.addWidget(self.hanziMaskingCheck, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.meaningsSettingsFrame)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.textTab, "")
        self.colorsTab = QtGui.QWidget()
        self.colorsTab.setObjectName("colorsTab")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.colorsTab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.toneColorsSettingsFrame = QtGui.QGroupBox(self.colorsTab)
        self.toneColorsSettingsFrame.setObjectName("toneColorsSettingsFrame")
        self.gridLayout_3 = QtGui.QGridLayout(self.toneColorsSettingsFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.colorizePinyinCheck = QtGui.QCheckBox(self.toneColorsSettingsFrame)
        self.colorizePinyinCheck.setObjectName("colorizePinyinCheck")
        self.gridLayout_3.addWidget(self.colorizePinyinCheck, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tone1Button = QtGui.QPushButton(self.toneColorsSettingsFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.tone1Button.setFont(font)
        self.tone1Button.setObjectName("tone1Button")
        self.horizontalLayout_2.addWidget(self.tone1Button)
        self.tone2Button = QtGui.QPushButton(self.toneColorsSettingsFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.tone2Button.setFont(font)
        self.tone2Button.setObjectName("tone2Button")
        self.horizontalLayout_2.addWidget(self.tone2Button)
        self.tone3Button = QtGui.QPushButton(self.toneColorsSettingsFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.tone3Button.setFont(font)
        self.tone3Button.setObjectName("tone3Button")
        self.horizontalLayout_2.addWidget(self.tone3Button)
        self.tone4Button = QtGui.QPushButton(self.toneColorsSettingsFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.tone4Button.setFont(font)
        self.tone4Button.setObjectName("tone4Button")
        self.horizontalLayout_2.addWidget(self.tone4Button)
        self.tone5Button = QtGui.QPushButton(self.toneColorsSettingsFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.tone5Button.setFont(font)
        self.tone5Button.setObjectName("tone5Button")
        self.horizontalLayout_2.addWidget(self.tone5Button)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.verticalLayout_11.addWidget(self.toneColorsSettingsFrame)
        self.quickAccessColorsSettingsFrame = QtGui.QGroupBox(self.colorsTab)
        self.quickAccessColorsSettingsFrame.setObjectName("quickAccessColorsSettingsFrame")
        self.gridLayout_4 = QtGui.QGridLayout(self.quickAccessColorsSettingsFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.quickAccess1Button = QtGui.QPushButton(self.quickAccessColorsSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickAccess1Button.sizePolicy().hasHeightForWidth())
        self.quickAccess1Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.quickAccess1Button.setFont(font)
        self.quickAccess1Button.setObjectName("quickAccess1Button")
        self.horizontalLayout_4.addWidget(self.quickAccess1Button)
        self.quickAccess2Button = QtGui.QPushButton(self.quickAccessColorsSettingsFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.quickAccess2Button.setFont(font)
        self.quickAccess2Button.setObjectName("quickAccess2Button")
        self.horizontalLayout_4.addWidget(self.quickAccess2Button)
        self.quickAccess3Button = QtGui.QPushButton(self.quickAccessColorsSettingsFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.quickAccess3Button.setFont(font)
        self.quickAccess3Button.setObjectName("quickAccess3Button")
        self.horizontalLayout_4.addWidget(self.quickAccess3Button)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.quickAccessLabel = QtGui.QLabel(self.quickAccessColorsSettingsFrame)
        self.quickAccessLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.quickAccessLabel.setWordWrap(True)
        self.quickAccessLabel.setObjectName("quickAccessLabel")
        self.gridLayout_4.addWidget(self.quickAccessLabel, 0, 0, 1, 1)
        self.verticalLayout_11.addWidget(self.quickAccessColorsSettingsFrame)
        self.meaningNumberingSettingsFrame = QtGui.QGroupBox(self.colorsTab)
        self.meaningNumberingSettingsFrame.setObjectName("meaningNumberingSettingsFrame")
        self.gridLayout_6 = QtGui.QGridLayout(self.meaningNumberingSettingsFrame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.meaningNumberingColorButton = QtGui.QPushButton(self.meaningNumberingSettingsFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.meaningNumberingColorButton.setFont(font)
        self.meaningNumberingColorButton.setObjectName("meaningNumberingColorButton")
        self.gridLayout_6.addWidget(self.meaningNumberingColorButton, 1, 1, 1, 1)
        self.colorizeMeaningNumberingCheck = QtGui.QCheckBox(self.meaningNumberingSettingsFrame)
        self.colorizeMeaningNumberingCheck.setObjectName("colorizeMeaningNumberingCheck")
        self.gridLayout_6.addWidget(self.colorizeMeaningNumberingCheck, 0, 1, 1, 1)
        self.verticalLayout_11.addWidget(self.meaningNumberingSettingsFrame)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.tabWidget.addTab(self.colorsTab, "")
        self.audioTab = QtGui.QWidget()
        self.audioTab.setObjectName("audioTab")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.audioTab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox = QtGui.QGroupBox(self.audioTab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.enableAudioCheck = QtGui.QCheckBox(self.groupBox)
        self.enableAudioCheck.setObjectName("enableAudioCheck")
        self.verticalLayout_10.addWidget(self.enableAudioCheck)
        self.installedAudioPacksLabel = QtGui.QLabel(self.groupBox)
        self.installedAudioPacksLabel.setObjectName("installedAudioPacksLabel")
        self.verticalLayout_10.addWidget(self.installedAudioPacksLabel)
        self.audioPacksList = QtGui.QListWidget(self.groupBox)
        self.audioPacksList.setObjectName("audioPacksList")
        self.verticalLayout_10.addWidget(self.audioPacksList)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.installMandarinSoundsButton = QtGui.QPushButton(self.groupBox)
        self.installMandarinSoundsButton.setObjectName("installMandarinSoundsButton")
        self.verticalLayout_2.addWidget(self.installMandarinSoundsButton)
        self.openAudioPackDirectoryButton = QtGui.QPushButton(self.groupBox)
        self.openAudioPackDirectoryButton.setObjectName("openAudioPackDirectoryButton")
        self.verticalLayout_2.addWidget(self.openAudioPackDirectoryButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.tabWidget.addTab(self.audioTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Preferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QtGui.QApplication.translate("Preferences", "Pinyin Toolkit Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.livePreviewGroupBox.setTitle(QtGui.QApplication.translate("Preferences", "Live Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.hanziPinyinSettingsFrame.setTitle(QtGui.QApplication.translate("Preferences", "Hanzi And Pinyin", None, QtGui.QApplication.UnicodeUTF8))
        self.pinyinTonesLabel.setText(QtGui.QApplication.translate("Preferences", "Pinyin tone display method:", None, QtGui.QApplication.UnicodeUTF8))
        self.numericPinyinTonesRadio.setText(QtGui.QApplication.translate("Preferences", "Numeric tones", None, QtGui.QApplication.UnicodeUTF8))
        self.tonifiedPinyinTonesRadio.setText(QtGui.QApplication.translate("Preferences", "Tones as accents", None, QtGui.QApplication.UnicodeUTF8))
        self.hanziLabel.setText(QtGui.QApplication.translate("Preferences", "Preferred Hanzi character system:", None, QtGui.QApplication.UnicodeUTF8))
        self.simplifiedHanziRadio.setText(QtGui.QApplication.translate("Preferences", "Simplified (Mainland China, Singapore, Malaysia)", None, QtGui.QApplication.UnicodeUTF8))
        self.traditionalHanziRadio.setText(QtGui.QApplication.translate("Preferences", "Traditional (Taiwan, Hong Kong)", None, QtGui.QApplication.UnicodeUTF8))
        self.meaningsSettingsFrame.setTitle(QtGui.QApplication.translate("Preferences", "Meanings", None, QtGui.QApplication.UnicodeUTF8))
        self.languageLabel.setText(QtGui.QApplication.translate("Preferences", "Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.googleTranslateCheck.setText(QtGui.QApplication.translate("Preferences", "Fall back on Google Translate for unknown words", None, QtGui.QApplication.UnicodeUTF8))
        self.seperateMeasureWordCheck.setText(QtGui.QApplication.translate("Preferences", "Seperate measure word out into its own field", None, QtGui.QApplication.UnicodeUTF8))
        self.numberingLabel.setText(QtGui.QApplication.translate("Preferences", "Meaning numbering:", None, QtGui.QApplication.UnicodeUTF8))
        self.circledChineseNumberingRadio.setText(QtGui.QApplication.translate("Preferences", "Circled Chinese numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.circledArabicNumberingRadio.setText(QtGui.QApplication.translate("Preferences", "Circled Arabic numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.plainNumberingRadio.setText(QtGui.QApplication.translate("Preferences", "Plain numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.noNumberingRadio.setText(QtGui.QApplication.translate("Preferences", "No numbering", None, QtGui.QApplication.UnicodeUTF8))
        self.seperatorLabel.setText(QtGui.QApplication.translate("Preferences", "Meaning seperator:", None, QtGui.QApplication.UnicodeUTF8))
        self.linesSeperatorRadio.setText(QtGui.QApplication.translate("Preferences", "Lines", None, QtGui.QApplication.UnicodeUTF8))
        self.commasSeperatorRadio.setText(QtGui.QApplication.translate("Preferences", "Commas", None, QtGui.QApplication.UnicodeUTF8))
        self.customSeperatorRadio.setText(QtGui.QApplication.translate("Preferences", "Custom:", None, QtGui.QApplication.UnicodeUTF8))
        self.hanziMaskingCheck.setText(QtGui.QApplication.translate("Preferences", "Mask occurrences of the expression in the meaning", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.textTab), QtGui.QApplication.translate("Preferences", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.toneColorsSettingsFrame.setTitle(QtGui.QApplication.translate("Preferences", "Tone Colors", None, QtGui.QApplication.UnicodeUTF8))
        self.colorizePinyinCheck.setText(QtGui.QApplication.translate("Preferences", "Colorize Pinyin and Hanzi with tones", None, QtGui.QApplication.UnicodeUTF8))
        self.tone1Button.setText(QtGui.QApplication.translate("Preferences", "1 (ū)", None, QtGui.QApplication.UnicodeUTF8))
        self.tone2Button.setText(QtGui.QApplication.translate("Preferences", "2 (ú)", None, QtGui.QApplication.UnicodeUTF8))
        self.tone3Button.setText(QtGui.QApplication.translate("Preferences", "3 (ǔ)", None, QtGui.QApplication.UnicodeUTF8))
        self.tone4Button.setText(QtGui.QApplication.translate("Preferences", "4 (ù)", None, QtGui.QApplication.UnicodeUTF8))
        self.tone5Button.setText(QtGui.QApplication.translate("Preferences", "5 (u)", None, QtGui.QApplication.UnicodeUTF8))
        self.quickAccessColorsSettingsFrame.setTitle(QtGui.QApplication.translate("Preferences", "Quick Access Colors", None, QtGui.QApplication.UnicodeUTF8))
        self.quickAccess1Button.setText(QtGui.QApplication.translate("Preferences", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.quickAccess2Button.setText(QtGui.QApplication.translate("Preferences", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.quickAccess3Button.setText(QtGui.QApplication.translate("Preferences", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.quickAccessLabel.setText(QtGui.QApplication.translate("Preferences", "These colors, along with the tone colors, are available in the fact editor by pressing Ctrl+F1 to Ctrl+F8 while some text is selected:", None, QtGui.QApplication.UnicodeUTF8))
        self.meaningNumberingSettingsFrame.setTitle(QtGui.QApplication.translate("Preferences", "Meaning Numbering Color", None, QtGui.QApplication.UnicodeUTF8))
        self.meaningNumberingColorButton.setText(QtGui.QApplication.translate("Preferences", "Meaning Numbering Color", None, QtGui.QApplication.UnicodeUTF8))
        self.colorizeMeaningNumberingCheck.setText(QtGui.QApplication.translate("Preferences", "Colorize meaning numbering", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.colorsTab), QtGui.QApplication.translate("Preferences", "Colors", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Preferences", "Audio Packs", None, QtGui.QApplication.UnicodeUTF8))
        self.enableAudioCheck.setText(QtGui.QApplication.translate("Preferences", "Enable automatic text-to-speech generation", None, QtGui.QApplication.UnicodeUTF8))
        self.installedAudioPacksLabel.setText(QtGui.QApplication.translate("Preferences", "Installed text-to-speech audio packs:", None, QtGui.QApplication.UnicodeUTF8))
        self.installMandarinSoundsButton.setText(QtGui.QApplication.translate("Preferences", "Install Free Mandarin Sounds Pack", None, QtGui.QApplication.UnicodeUTF8))
        self.openAudioPackDirectoryButton.setText(QtGui.QApplication.translate("Preferences", "Open Audio Pack Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.audioTab), QtGui.QApplication.translate("Preferences", "Audio", None, QtGui.QApplication.UnicodeUTF8))

