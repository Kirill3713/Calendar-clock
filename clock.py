import ttkbootstrap as ttk
import time

class Clock(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.primary_font = ('Gabriola', 15)
        self.secondary_font = ('Gabriola', 40)

        self.time_label = ttk.Label(self, text="12.00", font=self.secondary_font, style="success", width=7-1, justify="center")
        self.time_label.grid(column=0, row=0, sticky="we", columnspan=2)

        self.day = ttk.Label(self, text="Суббота", font=self.primary_font, style="primary")
        self.day.grid(column=0, row=1)
        
        self.date = ttk.Label(self, text="01.01.01", font=self.primary_font, style="info")
        self.date.grid(column=1, row=1)
        self.update()

    def update(self):
        self.time_label.configure(text=time.strftime("%H:%M:%S"))
        self.day.configure(text = time.strftime("%A"))
        self.date.configure(text=time.strftime("%d.%m.%Y"))
        self.after(1000, self.update)

class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configure(padx=20, pady=20)
        self.resizable(0, 0)
        self.clock = Clock(self)
        self.clock.grid(column=0, row=0)

if __name__ == "__main__":
    app1 = App(title = "Clock", themename = "superhero")
    app1.mainloop()