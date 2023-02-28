import tkinter
from tkinter import *
from tkinter import ttk
import PIL.ImageTk
import PIL.Image
import math


root = Tk()
root.title("title")
root.geometry("1024x768")
OSNR = '32'


# def choose():
#     selection = combo.get()
#     if selection == 'ou':
#         createOU()
#     if selection == 'dwdm':
#         DWDM.createDWDM(1)
#     if selection == '100GC':
#         Muxponder.createMUX(1)
#     # if selection == 'roadm': ## Ожидание руководства от Машиsd  
#     #     createMUX()
#     # if selection == '10G':
#     #     createMUX()
#     if selection == 'line':
#         createline()


def chanelchoose():
    global countchanel
    selection1 = combo1.get()
    if selection1 == '1':
        countchanel = 1
    if selection1 == '2':
        countchanel = 2
    if selection1 == '3':
        countchanel = 17
    if selection1 == '4':
        countchanel = 4
    if selection1 == '5':
        countchanel = 5
    if selection1 == '6':
        countchanel = 6
    if selection1 == '7':
        countchanel = 7
    if selection1 == '8':
        countchanel = 8
    if selection1 == '9':
        countchanel = 9


class CreateSE:

    def __init__(self):
        self.selection = combo.get()
        selection = self.selection
        print(type(selection))

    def createMUX(self):
        canvasMUX = Canvas(root, width=200, height=320, background='green')
        canvasMUX.bind('<B1-Motion>', drag)
        canvasMUX.grid()
        # ttk.Button(canvasMUX, text='MUX ', command=lambda: Calculations.createMUXKK(0)).place(x=47, y=27, anchor=CENTER)            ## Для Кросс коннектов
        canvasMUXUI = Canvas(canvasMUX, width=180, height=250, background="grey")
        canvasMUXUI.place(x=100, y=175, anchor=CENTER)
        ttk.Label(canvasMUXUI, text='Введите выходную \nмощность, дБ').place(x=67, y=50, anchor=CENTER)
        pwrMUXEntry = tkinter.Entry(canvasMUXUI)
        pwrMUXEntry.insert(0, -1)
        pwrMUXEntry.place(x=75, y=80, anchor=CENTER)
        muxDESTR = ttk.Button(canvasMUX, text='x', command=lambda: Calculations.destroyMUX(1, canvasMUX))
        muxDESTR.place(x=230, y=12, anchor=CENTER)
        ttk.Label(canvasMUXUI, text='OSNR= ' + OSNR).place(x=67, y=105, anchor=CENTER)
        pwrlabel = ttk.Label(canvasMUXUI)
        pwrlabel.place(x=100, y=100, anchor=CENTER)
        saveMUX = ttk.Button(canvasMUXUI, text='с', command=lambda: Calculations.valueb_labelMUX(1, canvasMUXUI, pwrMUXEntry.get()), width=1)
        saveMUX.place(x=144, y=88, anchor=CENTER)

    def createDWDM(self):
        global muxvalue
        global countchanel
        canvasCRDWDM = Canvas(root, width=200, height=320, background='purple')
        canvasCRDWDM.bind('<B1-Motion>', drag)
        canvasCRDWDM.grid()
        ttk.Button(canvasCRDWDM, text='DWDM', command=lambda: Calculations.valueb_labelDWDM(1)).place(x=47, y=27, anchor=CENTER)
        canvasCRDWDMUI = Canvas(canvasCRDWDM, width=180, height=250, background="grey")
        canvasCRDWDMUI.place(x=100, y=175, anchor=CENTER)
        ttk.Label(canvasCRDWDMUI, text='Выходная мощность\n в канале равна, дБ').place(x=20, y=40, anchor=W)
        ttk.Label(canvasCRDWDMUI, text='Коэф. передачи, разы').place(x=20, y=70, anchor=W)
        ttk.Label(canvasCRDWDMUI, text='F, разы').place(x=20, y=90, anchor=W)
        ttk.Label(canvasCRDWDMUI, text='F равна, дБ').place(x=20, y=110, anchor=W)
        ttk.Label(canvasCRDWDMUI, text='Cуммарная мощность, дБ').place(x=20, y=130, anchor=W)
        ttk.Label(canvasCRDWDMUI, text='F равна, дБ').place(x=20, y=150, anchor=W)
        ttk.Label(canvasCRDWDMUI, text='OSNR= ' + OSNR).place(x=20, y=170, anchor=W)
        ttk.Button(canvasCRDWDMUI, text='с', command=lambda: Calculations.valueb_labelDWDM(1, countchanel, muxvalue), width=1).place(x=170, y=150, anchor=W)
        ttk.Button(canvasCRDWDMUI, text='X', command=lambda: Calculations.destroyDWDM(1, canvasCRDWDMUI), width=1).place(x=170, y=12, anchor=CENTER)

    def createOU(self):
        print(1)
        pass


class Calculations:
    global countchanel

    def destroyMUX(self, canvasMUX):
        canvasMUX.destroy()

    def valueb_labelMUX(self, canvas1, muxvalue):
        global countchanel
        muxvalue = int(muxvalue)
        ttk.Label(canvas1, ).place(x=50, y=12, anchor=CENTER)
        level = ttk.Label(canvas1)
        level.place(x=95, y=12, anchor=CENTER)
        Label.config(level, text='Текущий уровень мощности = ' + str(muxvalue))
        Calculations.sumpowerchanelMUX(1, countchanel, muxvalue)

    def sumpowerchanelMUX(self, countchanel, muxvalue):
        chanelpwrVat = (10 ** (muxvalue / 10)) / 1000
        sumpowerVat = chanelpwrVat * countchanel
        sumpowerDBM = 10 * math.log10(sumpowerVat * 1000)
        muxsavestat = [muxvalue, chanelpwrVat, sumpowerVat, sumpowerDBM]
        muxOSNRdb = 32                                                                  ##дб OSNR
        muxOSNR = 10 ** (muxOSNRdb / 10)                                                ##OSNR
        muxOSNR_1 = 1 / muxOSNR                                                         ##1/OSNR
        muxsaveOSNR = [muxOSNR, muxOSNRdb, muxOSNR_1]
        print(muxsavestat)
        txtMUX = open('MUX.txt', 'w')
        txtMUX.write(str(muxsavestat) + str(muxsaveOSNR))
        txtMUX.close()
        Calculations.valueb_labelDWDM(1, countchanel, muxvalue, muxOSNR_1, chanelpwrVat)

    def valueb_labelDWDM(self, countchanel, muxvalue, muxOSNR_1, chanelpwrVat1DWDM):
        dwdmvalue = muxvalue - 11
        chanelpwrVat = (10 ** (dwdmvalue / 10)) / 1000
        sumpowerVat = chanelpwrVat * countchanel
        sumpowerDBM = 10 * math.log10(sumpowerVat * 1000)
        dwdmsavestat = [dwdmvalue, chanelpwrVat, sumpowerVat, sumpowerDBM]
        dwdmOSNR_1 = muxOSNR_1 + (0.0000000015925 * ((1 / (10 ** (-11 / 10))) - 1)) / chanelpwrVat1DWDM
        dwdmOSNR = 1 / dwdmOSNR_1
        dwdmOSNRdb = 10 * math.log10(dwdmOSNR)
        dwdmsaveOSNR = [dwdmOSNR, dwdmOSNRdb, dwdmOSNR_1]
        print(dwdmsaveOSNR)
        txtDWDM = open('DWDM.txt', 'w')
        txtDWDM.write(str(dwdmsavestat) + str(dwdmsaveOSNR))
        txtDWDM.close()
        print(dwdmsavestat)


    def destroyDWDM(self, canvasCRDWDMUI):
        canvasCRDWDMUI.destroy()


class test:

    def ppp(self):
        z = open('MUX.txt', 'r')
        z = z.read()
        z = z + 'q'
        print(z)

    def createMUXKK(self):
        pass

    pass


def choose():
    selection = combo.get()
    if selection == 'ou':
        CreateSE.createOU(1)
    if selection == 'dwdm':
        CreateSE.createDWDM(1)
    if selection == '100GC':
        CreateSE.createMUX(1)
    # if selection == 'roadm': ## Ожидание руководства от Маши
    #     createMUX()
    # if selection == '10G':
    #     createMUX()
    if selection == 'line':
        createline()


pole = Canvas(width=600, height=600, highlightthickness=0)
pole.place(x=300, y=300, anchor=CENTER)
chanels = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
blocks = ('dwdm', 'ou', '100GC', 'roadm', '10G', 'line')
combo = ttk.Combobox(values=blocks)
combo.grid(row=0, column=0)
combo1 = ttk.Combobox(values=chanels)
combo1.grid(row=1, column=0)
print(combo.get())
combentr = ttk.Button(text='Создать СЭ', command=choose)
combentr.grid(row=0, column=1)
combentr1 = ttk.Button(text='Задать номер канала', command=chanelchoose)
combentr1.grid(row=1, column=1)


def drag(event):
    mouse_x = pole.winfo_pointerx() - pole.winfo_rootx()
    mouse_y = pole.winfo_pointery() - pole.winfo_rooty()
    event.widget.place(x=mouse_x, y=mouse_y, anchor=CENTER)


def check():
    print(222)


def createline():
    canvas4 = Canvas(root, width=80, height=80, bg='black')
    canvas4.grid()
    canvas4.bind('<B1-Motion>', drag)
    line_image = PIL.Image.open("kat.png")
    imagesline = PIL.ImageTk.PhotoImage(line_image)
    linebtn = Button(canvas4, width=60, image=imagesline, height=55, font='Arial', command=check)
    linebtn.place(x=42, y=40, anchor=CENTER)
    linebtn.image = imagesline


root.mainloop()
