import numpy as np
import matplotlib.pyplot as plt

clcoding = np.linspace(0, 1, 500)

ecg = (
    np.sin(2*np.pi*5*clcoding)*0.1 +
    np.exp(-((clcoding-0.3)*80)**2)*1.5 +
    np.exp(-((clcoding-0.32)*200)**2)*-2 +
    np.exp(-((clcoding-0.35)*60)**2)*0.8
)

plt.figure(figsize=(8,3))
plt.plot(clcoding, ecg)
plt.title("Simulated Heartbeat Signal (ECG)")
plt.xlabel("Time")
plt.ylabel("Voltage") 
plt.grid()
plt.show()   