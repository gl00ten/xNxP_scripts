#!/usr/bin/env python3
# Sieve of Eratosthenes - interactive step-by-step GUI
# Crivo de Eratóstenes
# gl00ten 2018
#
# Requires: PyQt5
#   pip install PyQt5
#
# Run: python sieve_of_eratosthenes_gui.py


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import math, time

class App(QWidget):

    n = 1337
    nonPrimesL = []
    primesL = []
    toTestL = list(range(2,n+1))
    showL = list(range(2,n+1))
    limit = math.sqrt(n)

    def __init__(self):
        super().__init__()
        self.title = 'crivo 0.1 - press step'
        self.left = 0
        self.top = 0
        self.width = 900
        self.height = 900
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QGridLayout()

        self.fillLayout()

        self.setLayout(self.layout)

        #print(help(self.layout))

        
        self.show()

        
    def fillLayout(self):
        r = 0
        c = 0
        limit = math.sqrt(len(self.showL))
        for n in self.showL:
          label1 = QLabel(str(n))
          if n in self.primesL:
              label1.setStyleSheet("background-color: teal")
          elif n not in self.toTestL:
              label1.setStyleSheet("background-color: yellow")
          self.layout.addWidget(label1, r, c)
          c = c + 1
          if c > limit:
            r = r + 1
            c = 0

        self.text1 = QLineEdit(str(self.n))
        self.button1 = QPushButton("set")
        self.button1.clicked.connect(self.pressedButton1)
        self.button1.setStyleSheet("background-color: red")
        self.button2 = QPushButton("step")
        self.button2.setStyleSheet("background-color: green")
        self.button2.clicked.connect(self.pressedButton2)
        self.layout.addWidget(self.text1,r+1,0,1,4)
        self.layout.addWidget(self.button1,r+1,4,1,2)
        self.layout.addWidget(self.button2,r+1,6,1,2)


    @pyqtSlot()
    def pressedButton1(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

        self.n = int(self.text1.text())
        self.numbersL = list(range(2,self.n+1))
        self.showL = list(range(2,self.n+1))
        
        self.primesL = []
        self.limit = math.sqrt(self.n)
        self.fillLayout()

    @pyqtSlot()
    def pressedButton2(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

        self.step1()
        self.fillLayout()
        

    def step1(self):
      if len(self.toTestL) == 0:
          return
      if self.toTestL[0] > self.limit:
        self.primesL = self.primesL + self.toTestL
        self.toTestL = []
        print("finished")
        self.layout.addWidget(QLabel("finished"))
        return
      self.primesL.append(self.toTestL[0])
      self.toTestL = self.toTestL[1::]
      toRemoveL = []
      for n in self.toTestL:
          if n % self.primesL[-1] == 0:
              toRemoveL.append(n)
      for n in toRemoveL:
          self.toTestL.remove(n)
      print(self.toTestL)
      print(self.primesL)
    
              
              
      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
