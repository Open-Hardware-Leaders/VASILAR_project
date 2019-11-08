import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    b = QPushButton()
    b.setText("How to use it")


    b.clicked.connect(showdialog)
    widget.setWindowTitle("SILAR Controller v1.0")

    label_main = QLabel("PhotoVoltaics Researchs Laboratory")
    label_position = QLabel("Beakers Positions:")
    label_initial = QLabel("Initial Position:")
    label_cycles = QLabel("Number of Cycles:")
    label_sample = QLabel("Sample Length (cm):")
    label_beaker = QLabel("Beaker Height (cm):")
    label_liquid = QLabel("Liquid Height (cm):")
    label_dip_length = QLabel("Dip Length (cm):")
    label_dip_sp = QLabel("Dip Speed (mm/s):")
    label_dip_dn = QLabel("Dip Duration (min):")
    label_dry_dn = QLabel("Dry Duration (min):")



    pos1 = QCheckBox("1")
    pos2 = QCheckBox("2")
    pos3 = QCheckBox("3")
    pos4 = QCheckBox("4")
    pos5 = QCheckBox("5")
    pos6 = QCheckBox("6")
    pos7 = QCheckBox("7")
    pos8 = QCheckBox("8")

    init = QComboBox()
    init.addItems(["1","2","3","4","5","6","7","8"])

    cycle = QSpinBox()

    sample = QDoubleSpinBox()

    start = QPushButton("Start Process")

    bk1 = QDoubleSpinBox()
    bk2 = QDoubleSpinBox()
    bk3 = QDoubleSpinBox()
    bk4 = QDoubleSpinBox()
    bk5 = QDoubleSpinBox()
    bk6 = QDoubleSpinBox()
    bk7 = QDoubleSpinBox()
    bk8 = QDoubleSpinBox()

    lq1 =  QDoubleSpinBox()
    lq2 =  QDoubleSpinBox()
    lq3 =  QDoubleSpinBox()
    lq4 =  QDoubleSpinBox()
    lq5 =  QDoubleSpinBox()
    lq6 =  QDoubleSpinBox()
    lq7 =  QDoubleSpinBox()
    lq8 =  QDoubleSpinBox()

    dl1 =  QDoubleSpinBox()
    dl2 =  QDoubleSpinBox()
    dl3 =  QDoubleSpinBox()
    dl4 =  QDoubleSpinBox()
    dl5 =  QDoubleSpinBox()
    dl6 =  QDoubleSpinBox()
    dl7 =  QDoubleSpinBox()
    dl8 =  QDoubleSpinBox()

    ds1 =  QDoubleSpinBox()
    ds2 =  QDoubleSpinBox()
    ds3 =  QDoubleSpinBox()
    ds4 =  QDoubleSpinBox()
    ds5 =  QDoubleSpinBox()
    ds6 =  QDoubleSpinBox()
    ds7 =  QDoubleSpinBox()
    ds8 =  QDoubleSpinBox()

    dd1 =  QTimeEdit()
    dd2 =  QTimeEdit()
    dd3 =  QTimeEdit()
    dd4 =  QTimeEdit()
    dd5 =  QTimeEdit()
    dd6 =  QTimeEdit()
    dd7 =  QTimeEdit()
    dd8 =  QTimeEdit()

    dyd1 =  QTimeEdit()
    dyd2 =  QTimeEdit()
    dyd3 =  QTimeEdit()
    dyd4 =  QTimeEdit()
    dyd5 =  QTimeEdit()
    dyd6 =  QTimeEdit()
    dyd7 =  QTimeEdit()
    dyd8 =  QTimeEdit()

    layout = QGridLayout()
    layout.addWidget(label_main,0,0)
    layout.addWidget(b,0,9)
    layout.addWidget(label_position,1,0)
    layout.addWidget(pos1,1,1)
    layout.addWidget(pos2,1,2)
    layout.addWidget(pos3,1,3)
    layout.addWidget(pos4,1,4)
    layout.addWidget(pos5,1,5)
    layout.addWidget(pos6,1,6)
    layout.addWidget(pos7,1,7)
    layout.addWidget(pos8,1,8)

    layout.addWidget(label_initial,2,0)
    layout.addWidget(init,2,1)

    layout.addWidget(label_cycles,3,0)
    layout.addWidget(cycle,3,1)

    layout.addWidget(label_sample,4,0)
    layout.addWidget(sample,4,1)

    layout.addWidget(label_beaker,5,0)
    layout.addWidget(bk1,5,1)
    layout.addWidget(bk2,5,2)
    layout.addWidget(bk3,5,3)
    layout.addWidget(bk4,5,4)
    layout.addWidget(bk5,5,5)
    layout.addWidget(bk6,5,6)
    layout.addWidget(bk7,5,7)
    layout.addWidget(bk8,5,8)

    layout.addWidget(label_liquid,6,0)
    layout.addWidget(lq1,6,1)
    layout.addWidget(lq2,6,2)
    layout.addWidget(lq3,6,3)
    layout.addWidget(lq4,6,4)
    layout.addWidget(lq5,6,5)
    layout.addWidget(lq6,6,6)
    layout.addWidget(lq7,6,7)
    layout.addWidget(lq8,6,8)

    layout.addWidget(label_dip_length,7,0)
    layout.addWidget(dl1,7,1)
    layout.addWidget(dl2,7,2)
    layout.addWidget(dl3,7,3)
    layout.addWidget(dl4,7,4)
    layout.addWidget(dl5,7,5)
    layout.addWidget(dl6,7,6)
    layout.addWidget(dl7,7,7)
    layout.addWidget(dl8,7,8)

    layout.addWidget(label_dip_sp,8,0)
    layout.addWidget(ds1,8,1)
    layout.addWidget(ds2,8,2)
    layout.addWidget(ds3,8,3)
    layout.addWidget(ds4,8,4)
    layout.addWidget(ds5,8,5)
    layout.addWidget(ds6,8,6)
    layout.addWidget(ds7,8,7)
    layout.addWidget(ds8,8,8)

    layout.addWidget(label_dip_dn,9,0)
    layout.addWidget(dd1,9,1)
    layout.addWidget(dd2,9,2)
    layout.addWidget(dd3,9,3)
    layout.addWidget(dd4,9,4)
    layout.addWidget(dd5,9,5)
    layout.addWidget(dd6,9,6)
    layout.addWidget(dd7,9,7)
    layout.addWidget(dd8,9,8)

    layout.addWidget(label_dry_dn,10,0)
    layout.addWidget(dyd1,10,1)
    layout.addWidget(dyd2,10,2)
    layout.addWidget(dyd3,10,3)
    layout.addWidget(dyd4,10,4)
    layout.addWidget(dyd5,10,5)
    layout.addWidget(dyd6,10,6)
    layout.addWidget(dyd7,10,7)
    layout.addWidget(dyd8,10,8)



    layout.addWidget(start,11,0)
    layout.addWidget(QProgressBar(),12,0,10,10)



    widget.setLayout(layout)
    widget.show()
    sys.exit(app.exec_())

def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("SILAR Controller Software")
    msg.setInformativeText("This is program has been develop by Jesús Alba. Click on the Show Details button for the info about how to use the software")
    msg.setWindowTitle("Help")
    msg.setDetailedText("1. Colocar la primera solucion en la posicion inicial del sistema.")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()
    print("value")

def msgbtn(i):
    print("button",i.text())

if __name__ == '__main__':
    window()
