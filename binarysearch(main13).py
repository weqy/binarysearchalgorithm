# Binary Search Algorithm
# Version 1.3 7/27/22 12:47pm
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
        create_list()

        #get_closest_element_from_sorted_list()


random_number = random.randrange(1000,9999)



original_list = list()
sorted_list = list()


def create_list():
    for x in range(int(Entry.get())):
        original_list.append(random.randrange(1000,10000))
    #print(original_list)
    sorted_list = original_list
    sorted_list.sort()
    #print(sorted_list)
    result = binarySearch(sorted_list, random_number, 0, len(sorted_list) - 1)
    #print(result)
    #print("random_number = ", random_number)
    randomnumis = "The random number is", random_number

    tellrandomnum = tk.Label(algorithm, text=randomnumis)
    tellrandomnum.config(font=('helvetica', 10))
    canvas1.create_window(200, 230, window=tellrandomnum)

    labelresult = ("Position of random number is", result)

    position = tk.Label(algorithm, text=labelresult)
    position.config(font=('helvetica', 10))
    canvas1.create_window(200, 260, window=position)



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

label1 = tk.Label(algorithm, text='Binary Search Algorithm')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)





button1 = tk.Button(text='Enter', command=typeInteger)
canvas1.create_window(200, 180, window=button1)





algorithm.mainloop()
