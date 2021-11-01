import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTabWidget
from PyQt5.QtWidgets import QWidget, QLabel, QRadioButton, QFormLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QFrame, QGraphicsDropShadowEffect

from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout

from PyQt5.QtWidgets import (
    QCheckBox, QComboBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt5.QtGui import QPixmap


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class MainApp(QWidget):
    def __init__(self):
        #QtWidgets.QMainWindow.__init__(self)
        super().__init__()
        self.setWindowTitle("DeepLabCut")
        self.resize(1500, 750)

        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.welcomeTabUI(), "Welcome")
        tabs.addTab(self.manage_projectTabUI(), "Manage Project")
        layout.addWidget(tabs)

        #self.set_window_layout()


    def welcomeTabUI(self):
        """Create the General page UI."""
        welcomeTab = QWidget()
        layout = QVBoxLayout()

        pixmap = QPixmap("C:/Users/User/PycharmProjects/pyProject1/pitures/Welcome.png") #C:\Users\User\PycharmProjects
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.setAlignment(Qt.AlignTop)
        layout.addWidget(lbl)

        welcomeTab.setLayout(layout)
        return welcomeTab

    def create_or_load(self):

        self.separatorLine = QFrame()
        self.separatorLine.setFrameShape(QFrame.HLine)
        self.separatorLine.setFrameShadow(QFrame.Raised)

        self.separatorLine.setLineWidth(0)
        self.separatorLine.setMidLineWidth(1)

        self.inLayout = QVBoxLayout()
        l1_step1 = QLabel("DeepLabCut - step 1. Create New Project or Load a Project")
        self.inLayout.setSpacing(40)
        self.inLayout.setContentsMargins(0,20,0,40)
        self.inLayout.addWidget(l1_step1)
        self.inLayout.addWidget(self.separatorLine)

    def create_RadioButton(self):
        self.create_layout = QVBoxLayout()
        self.create_layout.setSpacing(20)
        self.create_layout.setContentsMargins(0, 0, 0, 50)
        label = QLabel('Please choose an option:')
        label.setAlignment(Qt.AlignTop)
        self.create_layout.addWidget(label)
        self.create_layout.setAlignment(Qt.AlignTop)

        # Create a layout for the RadioButton
        optionsLayout = QHBoxLayout()
        optionsLayout.setSpacing(100)
        #self.optionsLayout.addWidget(label)
        optionsLayout.addWidget(QRadioButton('Create new project'))
        optionsLayout.addWidget(QRadioButton('Load existing project'))
        optionsLayout.setAlignment(Qt.AlignLeft )
        self.create_layout.addLayout(optionsLayout)

    def names_videos(self):
        self.names_loadvideos_layout = QVBoxLayout()
        self.names_loadvideos_layout.setSpacing(30)
        form_layout = QFormLayout()
        # Add widgets to the layout
        form_layout.addRow("Name of the Project:", QLineEdit())
        form_layout.addRow("Name of the experimenter:", QLineEdit())

        self.names_loadvideos_layout.addLayout(form_layout)

        videosLayout = QHBoxLayout()
        videosLayout.setSpacing(110)

        label = QLabel('Choose Videos:')
        videosLayout.addWidget(label)
        videosLayout.addWidget(QPushButton('Load Videos'))
        videosLayout.setAlignment(Qt.AlignLeft)

        self.names_loadvideos_layout.addLayout(videosLayout)

    def manage_projectTabUI(self):
        """Create the Manage project page UI."""
        manage_projectTab = QWidget()
        main_layout = QVBoxLayout()

        self.create_or_load()
        self.create_RadioButton()
        self.names_videos()

        main_layout.addLayout(self.inLayout)
        main_layout.addLayout(self.create_layout)
        main_layout.addLayout(self.names_loadvideos_layout)

        main_layout.setAlignment(Qt.AlignTop)
        manage_projectTab.setLayout(main_layout)
        return manage_projectTab

    def set_window_layout(self):
        main_vertical_layout = QVBoxLayout(self.centralwidget)
        main_vertical_layout.addLayout(self.inLayout)
        main_vertical_layout.addLayout(self.create_layout)
        main_vertical_layout.setAlignment(Qt.AlignTop)

        return main_vertical_layout



