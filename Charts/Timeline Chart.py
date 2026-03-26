import matplotlib.pyplot as plt 
import datetime as dt

dates = [
    dt.date(2022, 1, 1),
    dt.date(2022, 6, 1),
    dt.date(2023, 1, 1),
    dt.date(2023, 6, 1)
]

events = [
    "Project Started",
    "First Release",
    "Major Update",
    "Project Completed"
]

y = [1, 1, 1, 1]

plt.scatter(dates, y)
for i, event in enumerate(events):
    plt.text(dates[i], 1.02, event, rotation=45, ha='right')

plt.yticks([])
plt.xlabel('Timeline')
plt.title('Project Timeline Chart')
plt.show() 