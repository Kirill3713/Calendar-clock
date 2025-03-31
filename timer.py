import ttkbootstrap as ttk
import time
import threading
from playsound import playsound

class Timer(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.primary_font = ('Calibri Light', 15)
        self.secondary_font = ('Calibri Light', 30)

        self.value_input = ttk.Entry(self, style="light", font=self.primary_font)
        self.value_input.grid(column=0, row=0)

        self.start = ttk.Button(self, style="success", text="Start", command=self.start_thread)
        self.start.grid(column=1, row=0, padx=10)

        self.stop = ttk.Button(self, style="dangerous", text="Stop", command=self.stop_timer)
        self.stop.grid(column=1, row=1)

        self.time_left = ttk.Label(self, style="light", font=self.secondary_font, text="0:0:0")
        self.time_left.grid(column=0, row=1)
    def start_time(self):
        self.stop_loop = False
        self.time = self.value_input.get().split(":")
        try:
            if len(self.time) == 1:
                seconds = int(self.time[0])
                minutes = 0
                hours = 0
            elif len(self.time) == 2:
                seconds = int(self.time[1])
                minutes = int(self.time[0])
                hours = 0
            elif len(self.time) == 3:
                seconds = int(self.time[2])
                minutes = int(self.time[1])
                hours = int(self.time[0])
        except ValueError:
            hours = "Некор"
            minutes = "ректный"
            seconds = "ввод"
            return
        all_sec = hours*3600 + minutes*60 + seconds

        while all_sec != 0 and not self.stop_loop:
            all_sec -= 1
            hours = all_sec //3600
            minutes = all_sec%3600 //60
            seconds = all_sec - hours*3600 - minutes*60
            self.time_left.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.update()
            time.sleep(1)
        if not self.stop_loop:
            for _ in range(3):
                playsound(sound="alarm_sound.wav")
    def stop_timer(self):
        self.stop_loop = True
        self.time_left.configure(text="0:0:0")
    def start_thread(self):
        t = threading.Thread(target=self.start_time)
        t.start()
class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configure(padx=20, pady=20)
        self.resizable(0, 0)
        self.timer = Timer(self)
        self.timer.grid(column=0, row=0)

if __name__ == "__main__":
    a = App(title = "Timer", themename = "superhero")
    a.mainloop()