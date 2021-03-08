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
print(pheta)

pheta1 = 2 * math.cos(math.radians(36))
print(pheta1)

pheta2 = 2 * math.sin(math.radians(54))
print(pheta2)

pheta3 = 1 / (2 * math.cos(math.radians(72)))
print(pheta3)

window.mainloop()
