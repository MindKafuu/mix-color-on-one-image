from tkinter import *
import math

window = Tk()
window.title("Photo Filter")
window.iconbitmap('pikachu.ico')

img = PhotoImage(file = "music.png")

size = "%sx%s"% (img.width(), img.height())
window.geometry(size)

displayImg = Label(window, image = img)
displayImg.pack()

for i in range(0, math.floor(img.width() / 2)):
    for j in range(0, math.floor(img.height()/2)):
        (r, g, b) = img.get(i, j)
        avg = int((r + b + g) / 3)

        img.put("#%02x%02x%02x"% (255, avg, avg), (i, j))

for i in range(math.floor(img.width() / 2), img.width()):
    for j in range(0, math.floor(img.height()/2)):
        (r, g, b) = img.get(i, j)
        avg = int((r + b + g) / 3)

        img.put("#%02x%02x%02x"% (avg, 255, avg), (i, j))

for i in range(0, math.floor(img.width() / 2)):
    for j in range(math.floor(img.height()/2), img.height()):
        (r, g, b) = img.get(i, j)
        avg = int((r + b + g) / 3)

        img.put("#%02x%02x%02x"% (avg, avg, 255), (i, j))

for i in range(math.floor(img.width() / 2), img.width()):
    for j in range(math.floor(img.height()/2), img.height()):
        (r, g, b) = img.get(i, j)
        avg = int((r + b + g) / 3)

        img.put("#%02x%02x%02x"% (avg, avg, avg), (i, j))



window.mainloop()