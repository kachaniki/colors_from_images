import tkinter
from tkinter import filedialog, Tk, ttk

import clipboard
from PIL import ImageTk, Image
import colorgram


class App(Tk):
    def __init__(self):
        # main window setup
        super().__init__()
        self.title = "Colours picker"
        self.config(background='white')
        self.screen_width = int(self.winfo_screenwidth() / 3)
        self.screen_height = int(self.winfo_screenheight() * 0.75)
        self.geometry(f'{self.screen_width}x{self.screen_height}')
        print(f"width: {self.screen_width}, height:{self.screen_height}")
        self.minsize(width=400, height=600)

        # pass dependencies between classes
        self.set_picture = SetPicture(self)
        self.extract_colors = ExtractColors(self)
        self.create_color_labels = CreateColorsLabels(self)

        # dependency injection
        self.set_picture.extract_colors = self.extract_colors

        # run app
        self.mainloop()


class SetPicture(ttk.Frame):
    def __init__(self, app_reference):
        super().__init__(app_reference)
        self.app_reference = app_reference
        self.image_path = "images/empty.jpg"
        self.img = None

        self.pack()
        self.create_input_widget()

    def create_input_widget(self):
        # set image
        self.img = Image.open(self.image_path)
        self.img = self.img.resize(size=(int(self.winfo_screenwidth() / 4), int(self.winfo_screenheight() / 4)))
        self.img = ImageTk.PhotoImage(self.img)

        self.image_label = tkinter.Label(self, image=self.img)
        self.image_label.image = self.img

        # button for choosing picture
        self.button_choose_file = tkinter.Button(self)
        self.button_choose_file.config(text="choose picture",
                                       background='white',
                                       font=12,
                                       pady=1,
                                       command=self.display_image)

        # how many colors user want
        self.label_number_of_colors = tkinter.Label(self, text="How many colors do you need? ", font=14)
        self.entry_number_of_colors = tkinter.Entry(self, width=6, font=20)
        self.button_submit_number_of_colors = tkinter.Button(self, text="submit", font=14, command=self.submit)

        # grid widget
        self.image_label.grid(row=0, column=0, columnspan=3)
        self.button_choose_file.grid(row=1, column=1, pady=4)
        self.label_number_of_colors.grid(row=2, column=0, columnspan=3, pady=4)
        self.entry_number_of_colors.grid(row=3, column=1, pady=4)
        self.button_submit_number_of_colors.grid(row=3, column=2, pady=4)

    def choose_image(self):
        image_path = filedialog.askopenfile(title="Select image",
                                            filetypes=[("image files", "*.jpeg *.jpg *.png")],
                                            initialdir='/home/katarzyna/')

        self.image_path = image_path.name
        return self.image_path

    def display_image(self):
        print("set picture activated")
        self.img = Image.open(self.choose_image())
        self.img = self.img.resize(size=(int(self.winfo_screenwidth() / 4), int(self.winfo_screenheight() / 4)))
        self.img = ImageTk.PhotoImage(self.img)

        self.image_label.config(image=self.img)
        self.image_label.image = self.img

    def submit(self):
        amount_of_colors = int(self.entry_number_of_colors.get())
        return self.app_reference.extract_colors.send_colors_to_labels(amount_of_colors, self.image_path)


class ExtractColors():
    def __init__(self, app_reference):
        self.app_reference = app_reference

    def send_colors_to_labels(self, amount, path):
        colors: list = self.get_colors(path, amount)
        self.app_reference.create_color_labels.display_colors(colors)

    def get_colors(self, path, amount):
        colors = colorgram.extract(path, amount)
        # change format to list of tuples
        list_of_colors = [[(color.rgb.r, color.rgb.g, color.rgb.b)] for color in colors]
        return list_of_colors


class CreateColorsLabels(ttk.Frame):
    def __init__(self, app_reference):
        super().__init__(app_reference)
        self.app_reference = app_reference

        self.pack()
        self.color_labels = []

    def display_colors(self, colors):
        for colour_label, hexa_label in self.color_labels:
            colour_label.destroy()
            hexa_label.destroy()

        self.color_labels = []

        for num, color in enumerate(colors):
            color_hex = self._from_rgb(color[0])

            # create coloured square
            label = tkinter.Label(self, bg=color_hex, width=7, height=1)

            # create label with printed hexa code
            self.label_hexa_code = tkinter.Label(self, text=color_hex, font=('Times 14'), bg='white')
            self.label_hexa_code.bind("<Button-1>", self.copy_to_clipboard)

            # gridding

            if 0 <= num < 10:
                label.grid(row=num + 1, column=0, padx=10, pady=7, )
                self.label_hexa_code.grid(row=num + 1, column=1, padx=10, pady=7)
            elif 10 <= num < 20:
                num = num - 10
                label.grid(row=num + 1, column=3, padx=10, pady=7)
                self.label_hexa_code.grid(row=num + 1, column=4, padx=10, pady=7)
            elif 20 <= num < 30:
                num = num - 20
                label.grid(row=num + 1, column=6, padx=10, pady=7)
                self.label_hexa_code.grid(row=num + 1, column=7, padx=10, pady=7)

            # list append
            self.color_labels.append((label, self.label_hexa_code))

    def copy_to_clipboard(self, event):
        text = self.label_hexa_code.cget("text")
        clipboard.copy(text)
        print("Copied to clipboard:", text)

    def _from_rgb(self, rgb):
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'


app = App()
