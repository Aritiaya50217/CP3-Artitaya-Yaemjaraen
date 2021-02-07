import tkinter as tk
import math

def leftClickButton(event):
    height = float(textBoxHeight.get()) / 100
    powerHeight = height ** 2 
    weight = float(textBoxWeight.get())
    calculate = weight / powerHeight

    if calculate < 18.5 :
        print(labelResult2.configure(text="ผอมเกินไป"))
    elif calculate <= 18.6 or calculate <= 22.9:
        print(labelResult2.configure(text="น้ำหนักปกติ เหมาะสม"))
    elif calculate <= 23.0 or calculate <= 24.9:
            print(labelResult2.configure(text="น้ำหนักเกิน"))
    elif calculate <= 25.0 or calculate <= 29.9:
        print(labelResult2.configure(text="อ้วน"))
    else:
        print(labelResult2.configure(text="อ้วนมาก"))

    print(calculate)
    labelResult.configure(text=calculate)


'''หรือ def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
  labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)) '''
    
MainWindow = tk.Tk()
labelHeight = tk.Label(MainWindow,text="ส่วนสูง(cm.)").grid(row=0,column=0) # แยก grid ออก เพื่อให้นำค่าไปคำนวณ
textBoxHeight = tk.Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = tk.Label(MainWindow,text="น้ำหนัก(kg.)").grid(row=1,column=0)
textBoxWeight = tk.Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = tk.Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=3,column=1)

labelResult = tk.Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1) 

labelResult2 = tk.Label(MainWindow,text="ผล")
labelResult2.grid(row=4,column=1) 

MainWindow.mainloop()