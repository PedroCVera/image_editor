from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont4

#funtion to load image from pc

def pull_image()
	global img
	global img_backup
	max_size = (200,200)
	file_path = filedialog.askopenfilename()
	if file_path:
		img = Image.open(file_path)
		img.thumbnail(max_size)
		display_image(img)