"""Urdu Character to Image Converter"""

from PIL import Image, ImageDraw, ImageFont


class CharToImg:
    """
    Convert character to img
    """
    def __init__(self, font_style_path, font_size, img_width, img_height, img_output_path):
        self.font_style_path = font_style_path
        self.font_size = font_size
        self.img_width = img_width
        self.img_height = img_height
        self.img_output_path = img_output_path

    def generate_2d_img(self, character, background_color, character_color, xy):
        """

        :param character: A single character string
        :param background_color: Scalar-Value (0-255)
        :param character_color: Scalar-Value (0-255)
        :param xy: Top left corner of the text. (110, 50)
        """
        img = Image.new('L', (self.img_width, self.img_height), color=background_color)
        fnt = ImageFont.truetype(self.font_style_path, self.font_size)
        d = ImageDraw.Draw(img)
        d.text(xy, character, character_color, font=fnt)
        img.save(self.img_output_path)

    def generate_3d_img(self, character, background_color, character_color, xy):
        """

        :param character: A single character string
        :param background_color: List of RGB, e.g: (255, 255, 0)
        :param character_color: List of RGB, e.g: (255, 255, 0)
        :param xy: Top left corner of the text. (110, 50)
        """
        img = Image.new('RGB', (self.img_width, self.img_height), color=background_color)
        fnt = ImageFont.truetype(self.font_style_path, self.font_size)
        d = ImageDraw.Draw(img)
        d.text(xy, character, character_color, font=fnt)
        img.save(self.img_output_path)
