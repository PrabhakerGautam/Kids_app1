import os
from tkinter import *
from PIL import Image, ImageDraw

class ScreenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Capture App")

        self.init_gui()

    def init_gui(self):
        self.width = 500
        self.height = 400
        self.black = (0, 0, 0)  # Define black color for the background
        self.white = (255, 255, 255)  # Define white color for drawing
        self.image1 = Image.new("RGB", (self.width, self.height), self.white)  # Set the background color to black
        self.draw = ImageDraw.Draw(self.image1)

        self.cv = Canvas(self.root, width=self.width, height=self.height, bg='white')  # Set the canvas background to black
        self.cv.pack()

        self.cv.bind("<B1-Motion>", self.paint)

        button = Button(text="Save", command=self.save)
        button.pack()
        button = Button(text="Clear", command=self.clear)
        button.pack()
        close_button = Button(text="Close", command=self.close_window)
        close_button.pack()

    def paint(self, event):
        x1, y1 = (event.x + 1), (event.y + 1)
        x2, y2 = (event.x - 1), (event.y - 1)
        self.cv.create_oval(x1, y1, x2, y2, fill="white", width=5)
        self.draw.line([x1, y1, x2, y2], fill="red", width=5)

    def save(self):
        folder_path = "test_images"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_name = "my_image.png"
        file_path = os.path.join(folder_path, file_name)
        self.image1.save(file_path)

    def clear(self):
        self.cv.delete("all")
        w, h = self.image1.size
        self.draw.rectangle([0, 0, w, h], fill="white", width=0)

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = ScreenApp(root)
    root.mainloop()
