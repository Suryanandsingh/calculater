from Tkinter import *

def ical(source, side):
    storeObj=Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=NONE):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,justify='right', bd=30, bg='powder blue').pack(side=TOP, expand=YES, fill=BOTH)
        #RIDGE , RAISED ,SUNKEN and FLAT are use

        for clearBut in (["C"]):
            erase = ical(self,TOP)
            for ichar in clearBut:
                button(erase,LEFT,ichar, lambda storeObj=display,q=ichar: storeObj.set(' '))
        for NumBut in ("789/", "456*", "123-","0.+"):
            FunctionNum= ical(self,TOP)
            for iequal in NumBut:
                button(FunctionNum, LEFT,iequal,lambda storeObj=display,q=iequal: storeObj.set(storeObj.get()+q))

        EqualButton= ical(self,TOP)
        for iequal in "=":
            if(iequal=='='):
                btniEquals = button(EqualButton, LEFT, iequal)
                btniEquals.bind('<ButtonRelease-1>', lambda  e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals=button(EqualButton,LEFT ,iequal, lambda storeObj=display, s=' %s' %iequal: storeObj.set(storeObj.get()+s))
    def calc(self,display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("EROR")


if __name__=='__main__':
    app().mainloop()
