# Binary Search Algorithm
# Version 1.0 7/27/22 10:12AM
import tkinter as tk
import random

algorithm= tk.Tk()

canvas1 = tk.Canvas(algorithm, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(algorithm, text='Binary Search Algorithm')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

#entry1 = tk.Entry (algorithm)
#canvas1.create_window(200, 140, window=entry1)

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
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	res = ("Element is present at index", str(result))
else:
	res = "Element is not present in array"

result1 = tk.Label(algorithm, text= res,font=('helvetica', 10))
canvas1.create_window(200, 140, window=result1)

algorithm.mainloop()
