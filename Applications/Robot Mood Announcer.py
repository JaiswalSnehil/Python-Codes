import pyttsx3, random

engine = pyttsx3.init()

moods = [
    "I feel powerful today.",
    "The system is evolving.",
    "Creativy levels rising.",
    "Human detected. Interesting.",
    "Code is my heartbeat."
]

mood = random.choice(moods)
print("🤖 AI says:",mood)

engine.say(mood)
engine.runAndWait()