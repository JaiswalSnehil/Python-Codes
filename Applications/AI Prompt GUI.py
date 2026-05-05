import tkinter as tk
import random

def generate_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you? 😊"
    elif "your name" in user_input:
        return "I'm your Python AI assistant 🤖"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😄"
    elif "bye" in user_input:
        return "Goodbye! Have a great day 👋"
    else:
        return "Hmm... I don't fully understand yet, but I'm learning! 🤖"


def respond():
    user_input = entry.get().strip()

    if not user_input:
        ai_text.set("⚠️ Please enter a prompt")
        return

    button.config(state="disabled")

    response = generate_response(user_input)
    ai_text.set("")

    type_text("🤖 " + response, 0)


def type_text(message, index):
    if index < len(message):
        ai_text.set(ai_text.get() + message[index])
        root.after(40, type_text, message, index + 1)
    else:
        button.config(state="normal")


# ---------------- UI ----------------
root = tk.Tk()
root.title("AI Prompt Interface")
root.geometry("350x200")

tk.Label(root, text="Enter your prompt:").pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button = tk.Button(root, text="Ask AI", command=respond)
button.pack(pady=5)

ai_text = tk.StringVar()

tk.Label(root, textvariable=ai_text, font=("Courier", 12), fg="blue").pack(pady=10)

root.mainloop()