def operation(op):
    x = float(xText.get())
    y = float(yText.get())
    result.delete(0, 'end')
    if op == "":
        result.insert(0, x*y)
    elif op == "-":
        result.insert(0, x - y)
    elif op == "+":
        result.insert(0, x + y)

from tkinter import *
root = Tk()
root.title('Wow calculator')
root.geometry('600x200+600+600')
xLabel = Label(root, text='x')
xLabel.grid(row=0,column=0)

xText = Entry(root)
xText.grid(row=0,column=1)

yLabel = Label(root, text='y')
yLabel.grid(row=1,column=0)

yText = Entry(root)
yText.grid(row=1,column=1)

pScale =Scale(root,orient=HORIZONTAL)
pScale.grid(row=2, column=1)

pLabel = Label(root, text="")
pLabel.grid(row=4, column=0)

nButton = Button(root, text="XY",  command=lambda : operation(""))
nButton.grid(row=3,column=1, sticky=N+S+E+W)

pLabel = Label(root, text="")
pLabel.grid(row=4, column=0)

aButton = Button(root, text="X+Y", command=lambda : operation("+"))
aButton.grid(row=4,column=1, sticky=N+S+E+W)

pLabel = Label(root, text="")
pLabel.grid(row=5, column=0)

sButton = Button(root, text="X-Y",  command=lambda : operation("-"))
sButton.grid(row=5,column=1, sticky=N+S+E+W)

pLabel = Label(root, text="Result")
pLabel.grid(row=6, column=0)

result = Entry(root, text="Result")
result.grid(row =6, column=1, sticky=N+S+E+W)


mainloop()