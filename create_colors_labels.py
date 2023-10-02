import tkinter
from tkinter import ttk

import clipboard


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
