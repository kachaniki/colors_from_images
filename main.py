from tkinter import Tk
from set_picture import SetPicture
from extract_colors import ExtractColors
from create_colors_labels import CreateColorsLabels

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

if __name__ == '__main__':
    app = App()
