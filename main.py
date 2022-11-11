from tkinter.filedialog import *
from PIL import Image

filepath = askopenfilename()
picture = Image.open(filepath)
savePath = asksaveasfilename()
picture.save(savePath+".jpg",
            optimize = True,
            quality = 10)
