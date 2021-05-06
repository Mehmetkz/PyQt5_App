import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)

class sekme(QWidget):
    def __init__(self):
        super().__init__()
        #self.GridWidget()
        #self.YatayWidget()
        #self.DikeyWidget()
        #self.FormRow()
        self.NestedLayout()

    def YatayWidget(self):
        layout1 = QHBoxLayout()
        self.setWindowTitle("YatayLayout Uygulama")
        layout1.addWidget(QPushButton('Sol_Buton'),1)
        layout1.addWidget(QPushButton('Merkez_Buton'),2)
        layout1.addWidget(QPushButton('Sag_Buton'),3)
        self.setLayout(layout1)

    def DikeyWidget(self):
        layout2 = QVBoxLayout()
        self.setWindowTitle("DikeyLayout Uygulama")
        layout2.addWidget(QPushButton('Ust_Buton'),1)
        layout2.addWidget(QPushButton('Orta_Buton'),2)
        layout2.addWidget(QPushButton('Alt_Buton'),3)
        self.setLayout(layout2)

    def GridWidget(self):
        layout3 = QGridLayout()
        self.setWindowTitle("GridLayout Uygulama")
        layout3.addWidget(QPushButton("Buton (0,0)"),0,0)
        layout3.addWidget(QPushButton("Buton (0,2)"),0,1)
        layout3.addWidget(QPushButton("Buton (0,2)"),0,2)
        layout3.addWidget(QPushButton("Buton (1,0)"),1,0)
        layout3.addWidget(QPushButton("Buton (1,1)"),1,1)
        layout3.addWidget(QPushButton("Buton (1,2)"),1,2)
        layout3.addWidget(QPushButton("Buton (2,0)"),2,0)
        layout3.addWidget(QPushButton("Buton (2,1)"),2,1)
        layout3.addWidget(QPushButton("Buton (2,2)"),2,2)
        layout3.addWidget(QPushButton("Buton (3,0)"),3,0,2,3)
        self.setLayout(layout3)

    def FormRow(self):
        layout4 = QFormLayout()
        self.setWindowTitle("FormLayout Uygulama")
        layout4.addRow("Name: ",QLineEdit())
        layout4.addRow("Job: ",QLineEdit())
        layout4.addRow("e-mail: ",QLineEdit())
        self.setLayout(layout4)

    def NestedLayout(self):
        disLayout = QVBoxLayout()
        ustLayout = QFormLayout()
        dikeyLayout = QVBoxLayout()
        self.setWindowTitle("NestedLayout Uygulama")
        ustLayout.addRow("Name: ",QLineEdit())
        dikeyLayout.addWidget(QCheckBox("1.Satır"))
        dikeyLayout.addWidget(QCheckBox("2.Satır"))
        dikeyLayout.addWidget(QCheckBox("3.Satır"))
        disLayout.addLayout(ustLayout)
        disLayout.addLayout(dikeyLayout)
        self.setLayout(disLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sek = sekme()
    sek.show()
    sys.exit(app.exec_())
