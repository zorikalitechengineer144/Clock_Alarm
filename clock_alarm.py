from tkinter import *
import datetime
import time
from threading import Thread
import winsound  # Windows only

# Play a beep sound
def play_sound():
    # Frequency=1000Hz, Duration=1 second (1000ms)
    for _ in range(5):  # Beep 5 times
        winsound.Beep(1000, 1000)

# Alarm checking function
def alarm():
    while True:
        alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current: {current_time} | Alarm: {alarm_time}")
        if current_time == alarm_time:
            print("⏰ Time to Wake Up!")
            play_sound()
            break
        time.sleep(1)

def start_alarm():
    Thread(target=alarm).start()

# GUI setup
root = Tk()
root.title("Alarm Clock")
root.geometry("400x200")

Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hour.set("00")
OptionMenu(frame, hour, *[f"{i:02d}" for i in range(24)]).pack(side=LEFT)

minute = StringVar(root)
minute.set("00")
OptionMenu(frame, minute, *[f"{i:02d}" for i in range(60)]).pack(side=LEFT)

second = StringVar(root)
second.set("00")
OptionMenu(frame, second, *[f"{i:02d}" for i in range(60)]).pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica", 15), command=start_alarm).pack(pady=20)

root.mainloop()
