import colorgram


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