import psutil

battery = psutil.sensors_battery()

if battery is not None:
    print("Battery Percentage:", battery.percent, "%")

    print("Power Plugged in:", battery.power_plugged)

    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)
    
    print("Battery remaining Time:", convertTime(battery.secsleft))
else:
    print("No battery information available.")