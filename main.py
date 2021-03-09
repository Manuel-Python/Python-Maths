import math
from tkinter import *

# Based on Angela Yu's work

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

window = Tk()
window.title("Maths")
window.config(padx=200, pady=200, bg=GREEN)

pheta = 1 / (2 * math.sin(math.radians(18)))
print("18 - ", pheta)

pheta1 = 2 * math.cos(math.radians(36))
print("36 - ", pheta1)

pheta2 = 2 * math.sin(math.radians(54))
print("54 - ", pheta2)

pheta3 = 1 / (2 * math.cos(math.radians(72)))
print("72 - ", pheta3)

pheta4 = (1 / (math.sin(math.radians(18))) / 2)
print("18 - ", pheta4)

pheta5 = (1 / (math.cos(math.radians(72))) / 2)
print("72 - ", pheta5)

pheta6 = 2 / (1 / (math.sin(math.radians(54))))
print("54 - ", pheta6)

window.mainloop()
