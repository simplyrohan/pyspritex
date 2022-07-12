import colormap
class PygameNotFound(ModuleNotFoundError):
    pass


class InvalidParameter(Exception):
    pass


colors = {"white": (255, 255, 255), "#ffffff": (255, 255, 255),
          "gray": (127, 127, 127), "grey": (127, 127, 127), "#7f7f7f": (127, 127, 127),
          "black": (0, 0, 0), "#000000": (0, 0, 0),
          "red": (255, 0, 0), "#ff0000": (255, 0, 0),
          "green": (0, 255, 0), "#00ff00": (0, 255, 0),
          "blue": (0, 0, 255), "#0000ff": (0, 0, 255)}

def get_color(value: str):
    try:
        return colormap.hex2rgb(value)
    except ValueError:
        try:
            return colors[value]
        except KeyError:
            raise InvalidParameter(f"{value} is not a valid type; Expected types: RGB Code(tuple/list), HEX Code(str), "
                                   f"or Color Name(str). If you are attempting to use a color name, it might not be "
                                   f"supported yet")


