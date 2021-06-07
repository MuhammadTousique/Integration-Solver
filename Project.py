# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:14:06 2019

@author: muham
"""

from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox,QPushButton

app=QtWidgets.QApplication([])
dlg=uic.loadUi("gui.ui")

import math
from scipy.integrate import quad

def f(x):
    fx=eval(dlg.lineEdit_3.text())
    return fx
    

def Trapezoidal():
    
    a=float(dlg.lineEdit.text())
    b=float(dlg.lineEdit_2.text())
    fun=str(dlg.lineEdit_3.text())
    n=int(dlg.lineEdit_4.text())
    h=(b-a)/n
    x=a
    fxa=eval(fun)
    x=b
    fxb=eval(fun)
    final=0
    for i in range(1,n-1):
        x=a+(i*h)
        fxc=eval(fun)
        final=final+(fxc)
    final=(h*(fxa+(2*final)+fxb))/2
    an,err=quad(f,a,b)
    error=abs(((an-final)/an)*100)
    
    QMessageBox.information(None,"Message","The Definite Integral is %s"%final+"\n Direct Integration is %s"%an+"\nError is %s"%error)     
    dlg.lineEdit.clear()
    dlg.lineEdit_2.clear()
    dlg.lineEdit_3.clear()
    dlg.lineEdit_4.clear()
    
def Simpson1():
    
    a = float(dlg.lineEdit.text())
    b = float(dlg.lineEdit_2.text())
    fun = str(dlg.lineEdit_3.text())
    n=int(dlg.lineEdit_4.text())
    h=(b-a)/n
    x=a
    fxa=eval(fun)
    x=b
    fxb=eval(fun)
    ans=fxa+fxb
    fxlist=[]
    for i in range(0,n):
        if i==0:
            x=a
            fxlist.append(eval(fun))
        else:
            x=x+h
            fxlist.append(eval(fun))
    for i in range(1,n):
        if i%2!=0:
            ans=ans +4*fxlist[i]
        else:
            ans=ans+2*fxlist[i]
    ans=((b-a)/(3*n))*ans
    an,err=quad(f,a,b)
    error=abs(((an-ans)/an)*100)
           
    QMessageBox.information(None,"Message","The Definite Integral is %s"%ans+"\n Direct Integration is %s"%an+"\nError is %s"%error)
    dlg.lineEdit.clear()
    dlg.lineEdit_2.clear()
    dlg.lineEdit_3.clear()
    dlg.lineEdit_4.clear()            
    
def Simpson3():
    
    a = float(dlg.lineEdit.text())
    b = float(dlg.lineEdit_2.text())
    fun = str(dlg.lineEdit_3.text())
    n=int(dlg.lineEdit_4.text())
    h=(b-a)/n
    x=a
    fxa=eval(fun)
    x=b
    fxb=eval(fun)
    ans=fxa+fxb
    fxlist=[]
    for i in range(0,n+1):
        if i==0:
            x=a
            fxlist.append(eval(fun))
        else:
            x=a+(i*h)
            fxlist.append(eval(fun))
    for i in range(1,n-1,3):
        ans=ans +(3*fxlist[i])
        
    for i in range(2,n,3):
        ans=ans+(3*fxlist[i])
        
    for i in range(3,n-2,3):
        ans=ans+(2*fxlist[i])
        
    ans=((3/8)*(h))*(ans)
    an,err=quad(f,a,b)
    error=abs(((an-ans)/an)*100)
           
    QMessageBox.information(None,"Message","The Definite Integral is %s"%ans+"\n Direct Integration is %s"%an+"\nError is %s"%error)          
    dlg.lineEdit.clear()
    dlg.lineEdit_2.clear()
    dlg.lineEdit_3.clear()
    dlg.lineEdit_4.clear()
        
def Lagrange():
    a=dlg.lineEdit_5.text()
    X=a.split(',')
    b=dlg.lineEdit_6.text()
    Y=b.split(',')
    x = int(dlg.lineEdit_7.text())
    sum = 0
    for i in range(0,len(X)):
        prod = 1
        for j in range(0,len(X)):
            if i != j:
                prod =prod * (x-float(X[j])) / (float(X[i]) - float(X[j]))
        prod =prod * float(Y[i])
        sum = sum + prod
    
    QMessageBox.information(None,'Message',"%s"%sum)
    dlg.lineEdit.clear()
    dlg.lineEdit_2.clear()
    dlg.lineEdit_3.clear()
    
dlg.pushButton.clicked.connect(Trapezoidal)
dlg.pushButton_2.clicked.connect(Simpson1)
dlg.pushButton_3.clicked.connect(Simpson3)
dlg.pushButton_4.clicked.connect(Lagrange)

dlg.show()
app.exec()


