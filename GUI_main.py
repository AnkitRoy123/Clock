import tkinter as tk
from datetime import datetime
def update_clock():
  current_time = datetime.now().strftime("%H:%M:%S")
  clock_label.config(text=current_time)
  clock_label.after(1000, update_clock)  
root = tk.Tk()
root.title("Digital Clock")
root.config(bg="gray")
clock_label = tk.Label(root, font=("Arial", 45, "bold"), fg="red", bg="black")
clock_label.pack()
update_clock()
root.mainloop()
