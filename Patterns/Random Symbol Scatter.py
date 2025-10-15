import tkinter as tk, random

root  = tk.Tk()
root.title('AI Symbol Particles')
canvas = tk.Canvas(root, width=500, height=500, bg='black')
canvas.pack()
symbols = ['#','@','$','%','&','*']
particles = [[random.randint(0,500), random.randint(0,500),
              random.randint(-2,2),
              random.randint(-2,2)] for _ in range(50)]
def update():
    canvas.delete('all')
    for p in particles:
        p[0] += p[2]
        p[1] += p[3]
        if p[0]<0 or p[0]>500: p[2]*=-1
        if p[1]<0 or p[1]>500: p[3]*=-1
        canvas.create_text(p[0],p[1],text=random.choice(symbols),fill='cyan',font=('Courier',16,'bold'))
    root.after(50, update)

update()
root.mainloop()