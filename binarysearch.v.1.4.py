# Binary Search Algorithm
# Version 1.4 7/29/22 9:27AM
import tkinter as tk
import random
from tkinter import *
import playsound # must run: pip install playsound==1.2.2 . latest versions WILL NOT WORK

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

def clear_text():
   Entry.delete(0, END)

def typeInteger():
    #j = ("You typed:", Entry.get())
    label3 = tk.Label(algorithm, text="You typed: " + str(Entry.get()))
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
        create_list()



random_number = random.randrange(1000,10000)



original_list = list()
sorted_list = list()


def create_list():
    for x in range(int(Entry.get())):
        original_list.append(random.randrange(1000,10000))
    #print(original_list)
    sorted_list = original_list
    sorted_list.sort()
    print(sorted_list)
    result = binarySearch(sorted_list, random_number, 0, len(sorted_list) - 1)
    print("random number position =", result)
    print("random number =", random_number)

    tellrandomnum = tk.Label(algorithm, text="Random number is: " + str(random_number))
    tellrandomnum.config(font=('helvetica', 10))
    canvas1.create_window(200, 230, window=tellrandomnum)

    labelresult = ("Position of random number is " + str(result))
    print(labelresult)

    position = tk.Label(algorithm, text="Position of random number is: " + str(result))
    position.config(font=('helvetica', 10))
    canvas1.create_window(200, 260, window=position)
    playsound.playsound('monkeyscreech.mp3')



def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return low


button1 = tk.Button(text='Enter', command=typeInteger)
canvas1.create_window(200, 180, window=button1)

algorithm.mainloop()
