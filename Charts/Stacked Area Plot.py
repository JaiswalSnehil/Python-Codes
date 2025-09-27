import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sleep = [7, 8, 6, 11, 7]
work = [8, 7, 7, 8, 6]
play = [9, 9, 11, 5, 11]

plt.stackplot(days, sleep, 
              work, play,
labels=['Sleep','Work','Play'])
plt.legend(loc='upper left')
plt.title('Stacked Area Chart')
plt.show()