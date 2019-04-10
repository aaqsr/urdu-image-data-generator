import yaml

from image_generator.font_img_generator import FontImgGenerator

with open("config/font_img_generator.yaml", 'r') as file:
    config = yaml.safe_load(file)


fnt_to_img = FontImgGenerator(img_width=config["image_width"], img_height=config["image_height"],
                              font_dir=config["fonts_directory"], output_dir=config["output_directory"])

fnt_to_img.generate_all_characters_images(characters=config["characters"], font_size_var=config["font_sizes"],
                                          background_color_var=config["img_background_colors"],
                                          chr_color_var=config["character_colors"],
                                          chr_starting_points=config["character_positions"])

