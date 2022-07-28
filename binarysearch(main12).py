# Binary Search Algorithm
# Version 1.1 7/27/22 11:58AM
import tkinter as tk
import random
from tkinter import *

algorithm = tk.Tk()

canvas1 = tk.Canvas(algorithm, width=400, height=300)
canvas1.pack()

label1 = tk.Label(algorithm, text='Binary Search Algorithm')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(algorithm, text='Type a number between 10-99: ')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 110, window=label2)

Entry = tk.Entry(algorithm, width=2)
canvas1.create_window(200, 140, window=Entry)
'''
def checkEntry():

	if entry1.get() < 10:
		entry1.get() = "Please check your code: Number must be higher than 10"
	elif c > 99:
		j = "Please check your code: Number must be less than 99"
	label4 = tk.Label(algorithm, text=j)
	label4.config(font=('halvetica', 10))
	canvas1.create_window(200, 225, window=label4)

'''

def clear_text():
   Entry.delete(0, END)

def clear_text():
   Entry.delete(0, END)

def typeInteger():
    j = ("You typed:", Entry.get())
    label3 = tk.Label(algorithm, text=j)
    label3.config(font=('halvetica', 10))
    canvas1.create_window(200, 200, window=label3)
    entered_number = int(Entry.get())
    if entered_number < 10:
        label4 = tk.Label(algorithm, fg="red", text="Please check your entry.")
        label4.config(font=('helvetica', 10))
        canvas1.create_window(200, 160, window=label4)
        clear_text()
    elif entered_number > 99:
            label4 = tk.Label(algorithm, fg="red", text="Please check your entry.")
            label4.config(font=('helvetica', 10))
            canvas1.create_window(200, 160, window=label4)
            clear_text()
    else:
        RNG()
        #print("RNG has been run")


# print(type((entered_number)))
# print(Entry)

'''
def randomnumbergenerator():
    ran = int(random.randrange())
'''

def RNG():
    for x in range (int(Entry.get())):
        (random.randrange(1000,9999))

        #print(random.randrange(1000, 9999)) # random number generator
        # randomNumLabel = tk.Label(algorithm, text= str(random.randrange(1000,9999)) * (int(Entry.get())), font=('helvetica', 10))
        #randomNumLabel = tk.Label(algorithm, text= RNG())
        # canvas1.create_window(200, 250, window=randomNumLabel)

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    res = ("Element is present at index", str(result))
else:
    res = "Element is not present in array"

button1 = tk.Button(text='Enter', command=typeInteger)
canvas1.create_window(200, 180, window=button1)

result1 = tk.Label(algorithm, text=res, font=('helvetica', 10))
canvas1.create_window(200, 80, window=result1)

algorithm.mainloop()
