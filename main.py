from clock import Clock
from timer import Timer
import ttkbootstrap as ttk

main_window = ttk.Window(title="Календарь-часы", themename = "superhero", resizable=(0, 0))
clock1 = Clock(main_window)
clock1.grid(column=0, row=0, padx=10, pady=10)
timer1 = Timer(main_window)
timer1.grid(column=0, row=1, padx=10, pady=10)
timer2 = Timer(main_window)
timer2.grid(column=0, row=2, padx=10, pady=10)
main_window.mainloop()