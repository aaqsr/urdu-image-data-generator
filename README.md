# Urdu Image Data Generator

The purpose of this module is to generate images of Urdu Language. Currently it generates images for Characters only.
In the output directory  a "data.csv" file will be created which maps image_path to its corresponding label.

## Instruction for Setup

### 1. Download and install python from python.org
    Version: minimum python version required 3.5

### 2. Get the Image Data Generator codebase

    git clone https://github.com/urduhack/urdu-image-data-generator.git <path-to-project-dir>


### 3. Create and Activate Virtual Environment

    cd <path-to-project-dir>
    python3 -m venv .python3_venv       # creates the virtual env
    source .python3_venv/bin/activate   # activates the virtual env

    After activating the virtual env. Any installed python packages would be installed here without affecting the main python binaries.
    To de-activate the virtual env, just type "deactivate"


### 4. Install the required packages

    pip install -r requirements.txt


## Running the Project:
    Currently only character to image module is available

### 1. Customize the configuration file:
    A config file is provided in the project "config/font_img_generator.yaml", customize it according to your requirement.
    You can tune the following parameters:

    image_width: width of the output image
    image_height: height of the output image

    fonts_directory: (String) Path to the font directory where urdu true type files are present
    output_directory: (String) Directory where you want to save your generated images


    characters: A list of characters that you want to generate images of. e.g. ['ق', 'ھ', 'غ', 'ص']
    font_sizes: A list of size of fonts you want to keep your character in output image. e.g. [10, 20, 30, 50]
    img_background_colors: A list of background color of output image. e.g. [0, 100, 150]
    character_colors: A list of colors for your character in output image. e.g. [200, 255]
    character_positions: A list of xy position of character in output image. e.g. [[110, 50]]


### 2. Run the Script:

    python generate_font_images.py
