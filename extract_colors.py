import colorgram


class ExtractColors():
    """This class got path of image and amount of colors from user input.
    Finally the class create list of rgb tuples like (r,g,b).
    Then invoke displays_colors method in create_color_labels class with the list as an argument"""

    def __init__(self, app_reference):
        self.app_reference = app_reference

    def get_colors(self, path: str, amount: int):
        colors = colorgram.extract(path, amount)
        # change format to list of tuples
        list_of_colors = [[(color.rgb.r, color.rgb.g, color.rgb.b)] for color in colors]
        return list_of_colors

    def send_colors_to_labels(self, amount: int, path: str):
        colors: list = self.get_colors(path, amount)
        self.app_reference.create_color_labels.display_colors(colors)
