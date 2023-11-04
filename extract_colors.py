import colorgram


class ExtractColors:
    """This class got path of image and amount of colors from user input.
    Finally the class create list of rgb tuples like (r,g,b) and return it"""
    def __init__(self, path, amount):
        self.path: str = path
        self.amount: int = amount
        self.list_of_colours:list = self.get_colors(self.path,self.amount)
        self.color_hex: list =[self._from_rgb(color[0]) for color in self.list_of_colours]
        print(self.color_hex)

    def get_colors(self, path: str, amount: int):
        colors = colorgram.extract(path, amount)
        # change format to list of tuples
        list_of_colors = [[(color.rgb.r, color.rgb.g, color.rgb.b)] for color in colors]
        return list_of_colors

    def _from_rgb(self, rgb: tuple) -> str:
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'

