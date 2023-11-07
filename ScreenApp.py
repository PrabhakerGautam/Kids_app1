from tkinter import *
from PIL import Image, ImageDraw, ImageShow
import os
import streamlit as st
import time




class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.counter_filename = "sequence_counter.txt"
        self.counter = self.load_sequence_counter()
        
        self.root.title("Screen Capture App")

        # Create a label and entry for folder name
        self.folder_label = Label(self.root, text="Enter your digit & draw your digit below using the mouse")
        self.folder_label.pack()
        self.folder_entry = Entry(self.root)
        self.folder_entry.pack()
        self.init_gui()

    def load_sequence_counter(self):
        if os.path.exists(self.counter_filename):
            with open(self.counter_filename, "r") as file:
                return int(file.read())
        return 0

    def save_sequence_counter(self):
        with open(self.counter_filename, "w") as file:
            file.write(str(self.counter))

    def init_gui(self):
        self.width = 500
        self.height = 400
        self.center = self.height // 2
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.image1 = Image.new("RGB", (self.width, self.height), self.white)
        self.draw = ImageDraw.Draw(self.image1)

        self.cv = Canvas(self.root, width=self.width, height=self.height, bg='white')
        self.cv.pack()

        self.cv.bind("<B1-Motion>", self.paint)

        button = Button(text="Save", command=self.save)
        button.pack()
        button = Button(text="Clear", command=self.save)
        button.pack()
        close_button = Button(text="Close", command=self.close_window)
        close_button.pack()

    def paint(self, event):
        x1, y1 = (event.x + 1), (event.y + 1)
        x2, y2 = (event.x - 1), (event.y - 1)
        self.cv.create_oval(x1, y1, x2, y2, fill="black", width=5)
        self.draw.line([x1, y1, x2, y2], fill="black", width=5)

    def save(self):
        st.write("'save' button pressed")
        file_path = "./images_folder/"
        file_name = f"my_image_{self.counter}.png"
        self.image1.save(file_path + file_name)
        self.counter += 1
        self.save_sequence_counter()
        self.cv.delete(ALL)
        w = self.image1.width
        h = self.image1.height
        self.draw.rectangle([0, 0, w, h], fill="white", width=0)
        st.write("'save' button pressed")

    
    def close_window(self):
        self.save_sequence_counter()  # Save the sequence counter before closing
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = ScreenCaptureApp(root)
    root.mainloop()
