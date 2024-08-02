from tkinter import *
from tkinter import filedialog, Tk, Label, Entry, Button, StringVar
from PIL import Image, ImageTk, ImageDraw, ImageFont


img = None
window_size = (800,600)
img_size = (300,300)


def ExitProgram():
	exit()

def CheckFont(file_path: str):
	if (file_path.endswith(".TTF") or file_path.endswith(".ttf")):
		return True
	return False

def CheckImage(file_path: str):
	if (file_path.endswith(".png") or file_path.endswith(".jpeg") or file_path.endswith(".jpg")):
		return True
	return False

def LoadImage():
	global img
	file_path = filedialog.askopenfilename()
	if file_path and CheckImage(file_path):
		img = Image.open(file_path)
		DisplayImage()


def DisplayImage():
	global img

	if img is None:
		return
	
	img = img.resize(img_size, Image.Resampling.LANCZOS)

	img_tk = ImageTk.PhotoImage(img)

	img_label.config(image=img_tk)
	img_label.image = img_tk

	x = (window_size[0] - img_size[0]) // 2
	y = (window_size[1] - img_size[1]) // 2

	img_label.place(x=x, y=y, width=img_size[0], height=img_size[1])



def CropLeft():
	global img
	if img:
		img = img.crop((5, 0, img.width, img.height))
		DisplayImage()

def CropRight():
	global img
	if img:
		img = img.crop((0, 0, img.width - 5, img.height))
		DisplayImage()

def CropTop():
	global img
	if img:
		img = img.crop((0, 5, img.width, img.height))
		DisplayImage()

def CropDown():
	global img
	if img:
		img = img.crop((0, 0, img.width, img.height - 5))
		DisplayImage()

def CropImage():
	global crop_menu

	crop_menu = Toplevel(root)
	crop_menu.title("Crop Editor")
	crop_menu.geometry("200x200")

	crop_button_frame = Frame(crop_menu)
	crop_button_frame.pack(side=LEFT, fill=Y)

	exit_top_button = Button(crop_button_frame, text="exit", command=crop_menu.destroy)
	exit_top_button.pack(side=TOP)

	crop_top_button = Button(crop_button_frame, text="crop top v", command=CropTop)
	crop_top_button.pack(side=TOP)

	crop_down_button = Button(crop_button_frame, text="crop up ^", command=CropDown)
	crop_down_button.pack(side=BOTTOM)

	crop_left_button = Button(crop_button_frame, text="crop left ->", command=CropLeft)
	crop_left_button.pack(side=LEFT)

	crop_right_button = Button(crop_button_frame, text="crop right <-", command=CropRight)
	crop_right_button.pack(side=RIGHT, pady=10)


def RotateImage():
	global img
	if img:
		img = img.rotate(90, expand=True)
		DisplayImage()


def AddTextMenu():
	global add_text_menu
	global text_var
	global font_size_var
	global font_path_var


	add_text_menu = Toplevel(root)
	add_text_menu.title("Text Editor")
	add_text_menu.geometry("250x200")

	text_menu_button_frame = Frame(add_text_menu)
	text_menu_button_frame.pack(side=TOP, fill=Y)

	text_var = StringVar()
	font_size_var = StringVar()
	font_path_var = StringVar()
	font_path_var.set("/msfonts/Arialbd.TTF")

	Label(text_menu_button_frame, text="Enter text to add:").pack(pady=0, padx=0)
	Entry(text_menu_button_frame, textvariable=text_var).pack(pady=0, padx=0)
	Label(text_menu_button_frame, text="Font Size:").pack(pady=0, padx=0)
	Entry(text_menu_button_frame, textvariable=font_size_var).pack(pady=0, padx=0)

	text_button = Button(text_menu_button_frame, text="Add Text", command=AddText)
	text_button.pack(side=TOP)

	font_button = Button(text_menu_button_frame, text="Change font", command=ChangeFont)
	font_button.pack(side=TOP)

	font_label = Label(text_menu_button_frame, textvariable=font_path_var)
	font_label.pack(pady=0, padx=0)

	add_text_exit_top_button = Button(text_menu_button_frame, text="exit", command=add_text_menu.destroy)
	add_text_exit_top_button.pack(side=TOP)

def ChangeFont():
	global font_path
	font_path = filedialog.askopenfilename()
	if CheckFont(font_path):
		font_path_var.set(font_path)  # update the font path

def AddText():
	global img

	if img:
		draw = ImageDraw.Draw(img)
		try:
			font_size = int(font_size_var.get())
		except ValueError:
			font_size = 40
		if font_size < 0:
			font_size = 40
		try:	
			font = ImageFont.truetype(font_path, font_size)
		except:
			print("BANANA")
			font = ImageFont.truetype("/msfonts/Arialbd.TTF", font_size)
		text = text_var.get()
		draw.text((img.size[0]/2 - ((len(text)/2) *font_size/1.7), (img.size[1] - ((img.size[1]/ 10) + font_size/2))), text, fill="white", font=font)
		DisplayImage()

def SaveImage():
	global img
	if img:
		save_path = filedialog.asksaveasfilename(defaultextension=".png")
		if save_path:
			img.save(save_path)


def main():
	global img_label
	global root

	root = Tk()
	root.title("Image Editor")
	root.geometry("800x600")

	button_frame = Frame(root)
	button_frame.pack(side=TOP, fill=X)

	

	image_frame = Frame(root)
	image_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

	load_button = Button(button_frame, text="Load Image", command=LoadImage)
	load_button.pack(side=LEFT)

	crop_button = Button(button_frame, text="Crop Image", command=CropImage)
	crop_button.pack(side=LEFT)

	rotate_button = Button(button_frame, text="Rotate Image", command=RotateImage)
	rotate_button.pack(side=LEFT)

	text_button = Button(button_frame, text="Add Text", command=AddTextMenu)
	text_button.pack(side=LEFT)

	save_button = Button(button_frame, text="Save Image", command=SaveImage)
	save_button.pack(side=LEFT)

	exit_button = Button(button_frame, text="Exit", command=ExitProgram)
	exit_button.pack(side=RIGHT)

	img_label = Label(image_frame)
	img_label.pack()

	root.mainloop()

if __name__ == "__main__":
	main()