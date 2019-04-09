"""Urdu Character to Image Converter"""

from PIL import Image, ImageDraw, ImageFont


class CharToImg:
    """
    Convert character to img
    """
    font_style_path = None
    font_size = None
    img_width = None
    img_height = None
    img_output_path = None

    @staticmethod
    def generate_2d_img(character, background_color, character_color, xy):
        """

        :param character: A single character string
        :param background_color: Scalar-Value (0-255)
        :param character_color: Scalar-Value (0-255)
        :param xy: Top left corner of the text. (110, 50)
        """
        img = Image.new('L', (CharToImg.img_width, CharToImg.img_height), color=background_color)
        fnt = ImageFont.truetype(CharToImg.font_style_path, CharToImg.font_size)
        d = ImageDraw.Draw(img)
        d.text(xy, character, character_color, font=fnt)
        img.save(CharToImg.img_output_path)

    @staticmethod
    def generate_3d_img(character, background_color, character_color, xy):
        """

        :param character: A single character string
        :param background_color: List of RGB, e.g: (255, 255, 0)
        :param character_color: List of RGB, e.g: (255, 255, 0)
        :param xy: Top left corner of the text. (110, 50)
        """
        img = Image.new('RGB', (CharToImg.img_width, CharToImg.img_height), color=background_color)
        fnt = ImageFont.truetype(CharToImg.font_style_path, CharToImg.font_size)
        d = ImageDraw.Draw(img)
        d.text(xy, character, character_color, font=fnt)
        img.save(CharToImg.img_output_path)
