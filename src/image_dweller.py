from tkinter import *
from tkinter import filedialog, Tk, Label, Entry, Button, StringVar
from PIL import Image, ImageTk, ImageDraw, ImageFont

img = None
window_size = (800,600)
img_size = (300,300)


def exit_program():
	exit()

def load_image():
	global img
	file_path = filedialog.askopenfilename()
	if file_path:
		img = Image.open(file_path)
		display_image()


def display_image():
	global img
	if img is None:
		return
	img = img.resize(img_size, Image.Resampling.LANCZOS)

	img_tk = ImageTk.PhotoImage(img)

	img_label.config(image=img_tk)
	img_label.image = img_tk  # Keep a reference to avoid garbage collection

	x = (window_size[0] - img_size[0]) // 2
	y = (window_size[1] - img_size[1]) // 2

	img_label.place(x=x, y=y, width=img_size[0], height=img_size[1])

def crop_left():
	global img
	if img:
		img = img.crop((5, 0, img.width, img.height))
		display_image()

def crop_right():
	global img
	if img:
		img = img.crop((0, 0, img.width - 5, img.height))
		display_image()

def crop_top():
	global img
	if img:
		img = img.crop((0, 5, img.width, img.height))
		display_image()

def crop_down():
	global img
	if img:
		img = img.crop((0, 0, img.width, img.height - 5))
		display_image()

def crop_image():
	global crop_menu
	crop_menu = Toplevel(root)
	crop_menu.title("Crop Editor")
	crop_menu.geometry("250x200")

	crop_button_frame = Frame(crop_menu)
	crop_button_frame.pack(side=LEFT, fill=Y)

	crop_top_button = Button(crop_button_frame, text="crop top v", command=crop_top)
	crop_top_button.pack(side=TOP)

	exit_top_button = Button(crop_button_frame, text="exit", command=crop_menu.destroy)
	exit_top_button.pack(side=TOP)

	crop_down_button = Button(crop_button_frame, text="crop up ^", command=crop_down)
	crop_down_button.pack(side=BOTTOM)

	crop_left_button = Button(crop_button_frame, text="crop left ->", command=crop_left)
	crop_left_button.pack(side=LEFT)

	crop_right_button = Button(crop_button_frame, text="crop right <-", command=crop_right)
	crop_right_button.pack(side=RIGHT, pady=10)


def rotate_image():
	global img
	if img:
		img = img.rotate(90, expand=True)
		display_image()

def add_text():
	global img
	if img:
		draw = ImageDraw.Draw(img)
		font_path = "/msfonts/Arialbd.TTF"  # Change this to the actual path
		try:
			font_size = int(font_size_var.get())
		except ValueError:
			font_size = 40
		if font_size < 0:
			font_size = 40
		font = ImageFont.truetype(font_path, font_size)
		text = text_var.get()
		print(len(text))
		draw.text((img.size[0]/2 - ((len(text)/2) *font_size/1.7), (img.size[1] - ((img.size[1]/ 10) + font_size/2))), text, fill="white", font=font)
		display_image()

def save_image():
	global img
	if img:
		file_path = filedialog.asksaveasfilename(defaultextension=".png")
		if file_path:
			img.save(file_path)


def main():
	global img_label
	global root
	global text_var
	global font_size_var

	root = Tk()
	root.title("Image Editor")
	root.geometry("800x600")

	button_frame = Frame(root)
	button_frame.pack(side=TOP, fill=X)

	text_var = StringVar()
	font_size_var = StringVar()

	Label(root, text="Enter text to add:").pack(pady=0, padx=0)
	Entry(root, textvariable=text_var).pack(pady=0, padx=0)
	Label(root, text="Font Size:").pack(pady=0, padx=0)
	Entry(root, textvariable=font_size_var).pack(pady=0, padx=0)

	image_frame = Frame(root)
	image_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

	load_button = Button(button_frame, text="Load Image", command=load_image)
	load_button.pack(side=LEFT)

	crop_button = Button(button_frame, text="Crop Image", command=crop_image)
	crop_button.pack(side=LEFT)

	rotate_button = Button(button_frame, text="Rotate Image", command=rotate_image)
	rotate_button.pack(side=LEFT)

	text_button = Button(button_frame, text="Add Text", command=add_text)
	text_button.pack(side=LEFT)

	save_button = Button(button_frame, text="Save Image", command=save_image)
	save_button.pack(side=LEFT)

	exit_button = Button(button_frame, text="Exit", command=exit_program)
	exit_button.pack(side=RIGHT)

	img_label = Label(image_frame)
	img_label.pack()

	root.mainloop()

if __name__ == "__main__":
	main()