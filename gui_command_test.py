from Tkinter import *

class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "Input:"
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=6)

        self.outputText = Label(self)
        self.outputText["text"] = "Output:"
        self.outputText.grid(row=1, column=0)
        self.outputField = Entry(self)
        self.outputField["width"] = 50
        self.outputField.grid(row=1, column=1, columnspan=6)

        self.new = Button(self)
        self.new["text"] = "New"
        self.new.grid(row=2, column=0)
        self.new["command"] = self.newMethod
        self.load = Button(self)
        self.load["text"] = "Load"
        self.load.grid(row=2, column=1)
        self.load["command"] = self.loadMethod
        self.save = Button(self)
        self.save["text"] = "Save"
        self.save.grid(row=2, column=2)
        self.save["command"] = self.saveMethod
        self.encode = Button(self)
        self.encode["text"] = "Encode"
        self.encode.grid(row=2, column=3)
        self.encode["command"] = self.encodeMethod
        self.decode = Button(self)
        self.decode["text"] = "Decode"
        self.decode.grid(row=2, column=4)
        self.decode["command"] = self.decodeMethod
        self.clear = Button(self)
        self.clear["text"] = "Clear"
        self.clear.grid(row=2, column=5)
        self.clear["command"] = self.clearMethod
        self.copy = Button(self)
        self.copy["text"] = "Copy"
        self.copy.grid(row=2, column=6)
        self.copy["command"] = self.copyMethod

        self.displayText = Label(self)
        self.displayText["text"] = "something happened"
        self.displayText.grid(row=3, column=0, columnspan=7)

    def newMethod(self):
        self.displayText["text"] = "This is New Button."

    def loadMethod(self):
        self.displayText["text"] = "This is Load Button."

    def saveMethod(self):
        self.displayText["text"] = "This is Save Button."

    def encodeMethod(self):
        self.displayText["text"] = "This is Encode Button."

    def decodeMethod(self):
        self.displayText["text"] = "This is Decode Button."

    def clearMethod(self):
        self.displayText["text"] = "This is Clear Button."

    def copyMethod(self):
        self.displayText["text"] = "This is Copy Button."
        

if __name__ == '__main__':
    root = Tk()
    app = GUIDemo(master=root)
    app.mainloop()
