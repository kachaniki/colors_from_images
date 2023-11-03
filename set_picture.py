import tkinter
from tkinter import ttk, filedialog

from PIL import ImageTk, Image


class SetPicture(ttk.Frame):
    def __init__(self, app_reference):
        super().__init__(app_reference)
        self.app_reference = app_reference
        self.image_path = "images/empty.jpg"
        self.img = None

        self.pack()
        self.create_input_widget()

    def create_input_widget(self) -> None:
        frame=tkinter.Frame()
        frame.pack()
        frame.config(bg="white")

        # set image
        self.img = Image.open(self.image_path)
        self.img = self.img.resize(size=(int(self.winfo_screenwidth() / 4), int(self.winfo_screenheight() / 4)))
        self.img = ImageTk.PhotoImage(self.img)

        self.image_label = tkinter.Label(frame, image=self.img)
        self.image_label.image = self.img

        # button for choosing picture
        self.button_choose_file = tkinter.Button(frame)
        self.button_choose_file.config(text="choose picture",
                                       background='white',
                                       font=12,
                                       pady=1,
                                       command=self.display_image)

        # how many colors user want
        self.label_number_of_colors = tkinter.Label(frame, text="How many colors do you need? ", font=14, bg="white")
        self.entry_number_of_colors = tkinter.Entry(frame, width=6, font=20)
        self.button_submit_number_of_colors = tkinter.Button(frame, text="submit", font=14, command=self.submit, bg="white")

        # grid widget
        self.image_label.grid(row=0, column=0, columnspan=3)
        self.button_choose_file.grid(row=1, column=1, pady=4)
        self.label_number_of_colors.grid(row=2, column=0, columnspan=3, pady=4)
        self.entry_number_of_colors.grid(row=3, column=1, pady=4)
        self.button_submit_number_of_colors.grid(row=3, column=2, pady=4)

    def choose_image(self) -> str:
        image_path = filedialog.askopenfile(title="Select image",
                                            filetypes=[("image files", "*.jpeg *.jpg *.png")],
                                            initialdir='/home/katarzyna/')

        self.image_path = image_path.name
        return self.image_path

    def display_image(self) -> None:
        print("set picture activated")
        self.img = Image.open(self.choose_image())
        self.img = self.img.resize(size=(int(self.winfo_screenwidth() / 4), int(self.winfo_screenheight() / 4)))
        self.img = ImageTk.PhotoImage(self.img)

        self.image_label.config(image=self.img)
        self.image_label.image = self.img

    def submit(self):
        amount_of_colors = int(self.entry_number_of_colors.get())
        return self.app_reference.extract_colors.send_colors_to_labels(amount_of_colors, self.image_path)
