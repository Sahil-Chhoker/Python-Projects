import os
import cv2 as cv
from tkinter import Tk, Button, Label, Entry, filedialog, messagebox

class ImageSlitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Slitter")
        self.root.geometry("300x300")

        self.step_label = Label(root, text="Step Size:")
        self.step_label.grid(row=0, column=0, padx=10, pady=10)

        self.step_entry = Entry(root)
        self.step_entry.grid(row=0, column=1, padx=10, pady=10)

        self.select_image_button = Button(root, text="Select Image", command=self.select_image)
        self.select_image_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.save_path_label = Label(root, text="Save Path:")
        self.save_path_label.grid(row=2, column=0, padx=10, pady=10)

        self.save_path_entry = Entry(root)
        self.save_path_entry.grid(row=2, column=1, padx=10, pady=10)

        self.select_save_path_button = Button(root, text="Select Save Path", command=self.select_save_path)
        self.select_save_path_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.split_button = Button(root, text="Split Image", command=self.split_image, state='disabled')
        self.split_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if file_path:
            self.image_path = file_path
            self.split_button.config(state='normal')

    def select_save_path(self):
        save_path = filedialog.askdirectory()
        if save_path:
            self.save_path_entry.delete(0, 'end')
            self.save_path_entry.insert(0, save_path)

    def split_image(self):
        step = self.step_entry.get()
        save_path = self.save_path_entry.get()

        if step.isdigit():
            if save_path:
                filename = os.path.basename(self.image_path)
                sprite = cv.imread(self.image_path)
                im_length, im_width, im_channel = sprite.shape

                step = int(step)

                if step == 0:
                    i = 0
                    try:
                        while os.path.exists(os.path.join(save_path, f"{i}.png")):
                            os.remove(os.path.join(save_path, f"{i}.png"))
                            i += 1
                    except:
                        messagebox.showinfo("Info", "All files are successfully deleted")
                else:
                    sprite_list = []
                    for i in range(0, im_width, step):
                        crop_sprite = sprite[0:im_length, i:i+step]
                        sprite_list.append(crop_sprite)

                    os.chdir(save_path)
                    for i in range(len(sprite_list)):
                        cv.imwrite(f"{i}.png", sprite_list[i])
                    messagebox.showinfo("Info", "Image successfully splitted")
            else:
                messagebox.showerror("Error", "Please select a save path")
        else:
            messagebox.showerror("Error", "Please enter a valid step size (integer)")

if __name__ == "__main__":
    root = Tk()
    app = ImageSlitterApp(root)
    root.mainloop()
