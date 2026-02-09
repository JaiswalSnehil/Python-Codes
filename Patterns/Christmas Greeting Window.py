import tkinter as tk

root = tk.Tk()
root.title("🌲 Merry Christmas")
root.geometry("400x200")
root.configure(bg="#b30000")
msg = tk.Label(
    root, text="🎅🏻 Merry Christmas!\nMAy your holidays be bright ✨",
    fg="white", bg="#b30000", font=("Arial", 16, "bold")
)
msg.pack(expand=True)
root.mainloop()