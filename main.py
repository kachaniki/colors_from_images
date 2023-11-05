from tkinter import Tk
from set_widget import SetWidget
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

        self.set_interface = SetWidget(self)
        self.create_labels = CreateColorsLabels()

        # run app
        self.mainloop()


if __name__ == '__main__':
    app = App()
