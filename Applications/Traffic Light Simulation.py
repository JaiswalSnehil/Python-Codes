import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=400, bg="black")
canvas.pack()

light = canvas.create_oval(50, 50, 150, 150, fill="grey")

def change_light(color):
    canvas.itemconfig(light, fill=color)
    root.update()
    time.sleep(1)
while True:
    change_light("red")
    change_light("yellow")
    change_light("green")

root.mainloop()