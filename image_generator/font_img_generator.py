import csv
import os

from font_to_image.chartoimg import CharToImg


class FontImgGenerator:
    """
    Generates Font Images
    """
    def __init__(self, img_width, img_height, font_dir, output_dir):
        self.img_width = img_width
        self.img_height = img_height
        self.font_dir = font_dir
        self.output_dir = output_dir

    def generate_char_images(self, character, font_size_var, background_color_var, chr_color_var, chr_starting_points):
        """
        Generates Character Images
        :param character: Urdu Alphabet e.g. 'ق'
        :param font_size_var: (list) of fonts. e.g. [10, 20, 50]
        :param background_color_var: (list) of background colours (for 2d Scalar, for 3d (R, G, B))
        :param chr_color_var: (list) of character color variations
        :param chr_starting_points: (list) [(x, y), (x1, y1)]

        """
        font_list = [fnt for fnt in os.listdir(self.font_dir) if ".ttf" in fnt]
        i = 0
        img_label_map_path = os.path.join(self.output_dir, "data.csv")
        with open(img_label_map_path, "a") as out:
            csv_writer = csv.writer(out)
            csv_writer.writerow(['image_path', 'img_width', 'img_height', 'font_style', 'font_size',
                                 'background_color', 'character_color', 'character_position', 'label'])
            for font_style in font_list:
                font_style_path = os.path.join(self.font_dir, font_style)
                for font_size in font_size_var:
                    CharToImg.font_size = font_size
                    for b_color in background_color_var:
                        for c_color in chr_color_var:
                            for c_start in chr_starting_points:
                                img_output_path = os.path.join(self.output_dir, character + "_" + str(i) + ".png")
                                chrtoimg = CharToImg(font_style_path, font_size, self.img_width,
                                                     self.img_height, img_output_path)
                                chrtoimg.generate_2d_img(character, b_color, c_color, c_start)
                                csv_writer.writerow([img_output_path, self.img_width, self.img_height, font_style,
                                                     font_size, b_color, c_color, c_start, character])
                                i += 1

    def generate_all_characters_images(self, characters, font_size_var, background_color_var,
                                       chr_color_var, chr_starting_points):
        """
        Generate images for all the given characters
        :param characters: (list) of characters ['ق', 'ھ', 'غ', 'ص']
        :param font_size_var: (list) of fonts. e.g. [10, 20, 50]
        :param background_color_var: (list) of background colours (for 2d Scalar, for 3d (R, G, B))
        :param chr_color_var: (list) of character color variations
        :param chr_starting_points: (list) [(x, y), (x1, y1)]
        """
        for character in characters:
            self.generate_char_images(character, font_size_var, background_color_var, chr_color_var, chr_starting_points)
