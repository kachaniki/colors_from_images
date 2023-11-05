import tkinter
import clipboard


class CreateColorsLabels:
    """1.Make a frame for labels with colors
    2.If some labels already exist, they will be destroyed
    3.New labels with colors are created """

    def __init__(self):
        self.color_labels = []
        self.make_frame()

    def make_frame(self):
        self.frame = tkinter.Frame()
        self.frame.pack()
        self.frame.config(bg="white")

    def display_colors(self, colors_list: list) -> None:
        self.destroy_existing_labels()
        for num, color in enumerate(colors_list):
            print(f"{num}: {color}")

            # create coloured square
            label = tkinter.Label(self.frame, bg=color, width=7, height=1)

            # create label with printed hexa code
            self.label_hexa_code = tkinter.Label(self.frame, text=color, font='Times 14', bg='white')
            self.label_hexa_code.bind("<Button-1>", lambda event: self.copy_to_clipboard())

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

    def destroy_existing_labels(self):
        for colour_label, hexa_label in self.color_labels:
            colour_label.destroy()
            hexa_label.destroy()

    def copy_to_clipboard(self) -> None:
        text = self.label_hexa_code.cget("text")
        clipboard.copy(text)
        print("Copied to clipboard:", text)
