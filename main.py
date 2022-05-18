# Import required Image library
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import Tk, Canvas, Button, PhotoImage, Entry, filedialog as fd


class Photo:

    def __init__(self):
        self.im = ""

    def set_im(self, im):
        self.im = im


photo = Photo()


def open_image():
    file = fd.askopenfilename(initialdir="/Pictures", title="Select a file", filetypes=(
        ("JPEG (*.jpg)", "*.jpg"), ("PNG (*.png)", "*.png"), ("All files", "*.*")))
    # im = Image.open(file)
    im = Image.open(file)
    photo.set_im(im)
    # width, height = im.size
    # print(width, height)


def save_image():
    im = photo.im
    draw = ImageDraw.Draw(im)
    text = "sample watermark"
    font = ImageFont.load_default()
    textwidth, textheight = draw.textsize(text, font)
# # calculate the x,y coordinates of the text
    margin = 10
    # x = width - textwidth - margin
    # y = height - textheight - margin
    x = margin
    y = margin

# # draw watermark in the upper left corner
    draw.text((x, y), text, font=font)
    im.save('watermark.jpg')
    im.show()


# Create an Image Object from an Image
# im = Image.open(file)

# draw = ImageDraw.Draw(im)
# text = "sample watermark"
#
# font = ImageFont.load_default()
# textwidth, textheight = draw.textsize(text, font)
#
# # calculate the x,y coordinates of the text
# margin = 10
# x = width - textwidth - margin
# y = height - textheight - margin
#
# # draw watermark in the bottom right corner
# draw.text((x, y), text, font=font)
# im.show()

# Save watermarked image
# im.save('watermark.jpg')

window = Tk()
window.title("Water Marker")
window.config(padx=100, pady=100)

load_button = Button(text="Load Image", command=open_image)
load_button.grid(row=2, column=1)

entry = Entry(width=30)
entry.insert(0, string="Watermark text")
entry.grid(row=3, column=1)

apply_button = Button(text="Apply", command=save_image)
apply_button.grid(row=4, column=1)

window.mainloop()
