import tkinter as tk
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

root = tk.Tk()
canvas1 = tk.Canvas(root, width= 600,height= 400)
canvas1.pack()

label = tk.Label(root, text='Password Generator')
canvas1.create_window(300,250, window= label)

entry1 = tk.Entry(root)
canvas1.create_window(200, 100, window= entry1)
label1 = tk.Label(root, text='How many letters')
canvas1.create_window(350,100, window= label1)
entry2 = tk.Entry(root)
canvas1.create_window(200, 150, window= entry2)
label2 = tk.Label(root, text='How many numbers')
canvas1.create_window(350,150, window= label2)
entry3 = tk.Entry(root)
canvas1.create_window(200, 200, window= entry3)
label3 = tk.Label(root, text='How many symbols')
canvas1.create_window(350,200, window= label3)

def press_me():
    letters_num = int(entry1.get())
    numbers_num = int(entry2.get())
    symbols_num = int(entry3.get())
    lett = ''
    numbs = ''
    symbl = ''
    random.shuffle(letters)
    for i in range(len(letters)):
        if i < letters_num:
            lett += letters[i]

    random.shuffle(numbers)
    for j in range(len(numbers)):
        if j < numbers_num:
            numbs += numbers[j]

    random.shuffle(symbols)
    for k in range(len(symbols)):
        if k < symbols_num:
            symbl += symbols[k]

    password = lett + str(numbs) + str(symbl)
    label1 = tk.Label(root, text = password)
    canvas1.create_window(300, 300, window=label1)
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")

button = tk.Button(text = 'generate!', command = press_me)
canvas1.create_window(400,250, window= button)

root.mainloop()

