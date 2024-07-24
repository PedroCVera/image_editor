from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

img = None

def exit_program():
	exit()

def main():
	global img_label

	root = Tk()
	root.title("Image Editor")
	root.geometry("1200x800")

	# Create a frame for the buttons
	button_frame = Frame(root)
	button_frame.pack(side=TOP, fill=X)

	# Create a frame for the image display
	image_frame = Frame(root)
	image_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

	save_button = Button(button_frame, text="Load Image", command=load_image)
	save_button.pack(side=LEFT)

	save_button = Button(button_frame, text="Exit", command=exit_program)
	save_button.pack(side=RIGHT)

	img_label = Label(image_frame)
	img_label.pack()

	root.mainloop()

if __name__ == "__main__":
	main()
