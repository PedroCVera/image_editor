from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

img = None
window_size = (800,600)
img_size = (300,300)


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
    global img_size

    if img:
        img = img.crop((5,0,img_size[0],img_size[1]))
        img_size[0] -= 5
        display_image()

def crop_right():
    global img
    global img_size

    if img:
        img_size[0] -= 5
        img = img.crop((5,0,img_size[0],img_size[1]))
        display_image()

def crop_right():
    global img
    global img_size

    if img:
        img_size[1] -= 5
        img = img.crop((5,0,img_size[0],img_size[1]))
        display_image()


def crop_top():
    global img
    global img_size

    img_size[1] -= 5
    if img:
        img = img.crop((0,5,img_size[0],img_size[1]))
        display_image()


def crop_image():
    crop_button_frame = tk.Frame(root)
    crop_button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

    crop_left_button = tk.Button(button_frame, text="crop left ->", command=crop_left)
    crop_left_button.pack(pady=5)

def rotate_image():
    global img
    if img:
        img = img.rotate(90, expand=True)
        display_image()

def add_text():
    global img
    if img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 40)
        text = "Sample Text"
        draw.text((10, 10), text, fill="white", font=font)
        display_image()

def save_image():
    global img
    if img:
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            img.save(file_path)


def exit_program():
    exit()

def main():
    global img_label

    root = Tk()
    root.title("Image Editor")
    root.geometry("800x600")

    # Create a frame for the buttons
    button_frame = Frame(root)
    button_frame.pack(side=TOP, fill=X)

    # Create a frame for the image display
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

    save_button = Button(button_frame, text="Exit", command=exit_program)
    save_button.pack(side=RIGHT)

    img_label = Label(image_frame)
    img_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
