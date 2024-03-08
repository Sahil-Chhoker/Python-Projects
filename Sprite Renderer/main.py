import os
from tkinter import Tk, Button, Canvas
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

class SpriteRenderer(): 
    def __init__(self, root):
        self.root = root
        self.root.title("Sprite Renderer")

        self.selected_image = None
        self.image_label = Canvas(self.root)
        self.image_label.pack()

        self.selections = []
        self.current_selection = None
        self.resize_handle_radius = 5
        self.resizing = False

        self.select_button = Button(self.root, text="Select Image", command=self.select_image)
        self.select_button.pack()
        
        self.save_button = Button(self.root, text="Save Selections", command=self.save_selections)
        self.save_button.pack()

        self.image_label.bind("<Button-1>", self.start_selection)
        self.image_label.bind("<B1-Motion>", self.draw_selection)
        self.image_label.bind("<ButtonRelease-1>", self.end_selection)

    def select_image(self):
        file_path = askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if file_path:
            self.selected_image = Image.open(file_path)
            self.display_image(self.selected_image)

    def display_image(self, image):
        self.image_tk = ImageTk.PhotoImage(image)
        self.image_label.config(width=self.image_tk.width(), height=self.image_tk.height())
        self.image_label.create_image(0, 0, anchor="nw", image=self.image_tk)

    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.current_selection = self.is_overlapping_selection(event.x, event.y)
        if self.current_selection:
            self.resizing = True
            self.resizing_handle = self.get_resizing_handle(event.x, event.y)
        else:
            self.rect = self.image_label.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="green")

    def draw_selection(self, event):
        if self.resizing:
            self.resize_selection(event.x, event.y)
        else:
            self.image_label.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def end_selection(self, event):
        if not self.resizing:
            end_x = event.x
            end_y = event.y
            self.selections.append((min(self.start_x, end_x), min(self.start_y, end_y), max(self.start_x, end_x), max(self.start_y, end_y)))
        self.resizing = False

    def is_overlapping_selection(self, x, y):
        for i, sel in enumerate(self.selections):
            x1, y1, x2, y2 = sel
            if x1 <= x <= x2 and y1 <= y <= y2:
                return i
        return None

    def get_resizing_handle(self, x, y):
        handle_coords = []
        for i, sel in enumerate(self.selections):
            x1, y1, x2, y2 = sel
            if abs(x - x1) <= self.resize_handle_radius and abs(y - y1) <= self.resize_handle_radius:
                handle_coords.append((i, x1, y1))
            if abs(x - x2) <= self.resize_handle_radius and abs(y - y2) <= self.resize_handle_radius:
                handle_coords.append((i, x2, y2))
        if handle_coords:
            return handle_coords[0]
        return None

    def resize_selection(self, x, y):
        if self.resizing_handle:
            i, handle_x, handle_y = self.resizing_handle
            self.selections[i] = (min(handle_x, x), min(handle_y, y), max(handle_x, x), max(handle_y, y))
            self.display_image_with_selections()

    def display_image_with_selections(self):
        self.image_label.delete("all")
        self.display_image(self.selected_image)
        for sel in self.selections:
            self.image_label.create_rectangle(*sel, outline="red")

    def save_selections(self):
        if self.selected_image and self.selections:
            for i, sel in enumerate(self.selections):
                selection_img = self.selected_image.crop(sel)
                selection_img.save(f"selection_{i}.png")

if __name__ == "__main__":
    root = Tk()
    app = SpriteRenderer(root)
    root.mainloop()
