import argparse, os
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(description='image watermarking')
parser.add_argument("path", help="path of input file or directory",
                    type=str)
parser.add_argument("-opacity", "--opacity", type=int, default = 40, help="opacity value of text")
parser.add_argument("-text", "--text", type=str, default = "@ARPAN", help="watermark text")
parser.add_argument("-size", "--size", type=int, default = 30, help="watermark text size")
parser.add_argument("-hspace", "--horizontalSpace", type=int, default = 70, help="Horizontal space")
parser.add_argument("-vspace", "--verticalSpace", type=int, default = 90, help="Vertical space")
parser.add_argument("-fpath", "--fontPath", type=str, default = r"C:\Windows\Fonts\Proxima Nova Bold.otf", help="font file path")

args = parser.parse_args()

# Use // for file names if you are facing issues
INPUT_IMAGE_FILE = args.path
OUTPUT_IMAGE_FILE = args.path+".watermarked.png"
FONT_LOCATION  = args.fontPath
FONT_SIZE = args.size
H_SPACING = args.horizontalSpace
V_SPACING = args.verticalSpace
FONT_OPACITY = args.opacity
WATERMARK_TEXT = args.text

# the following function reads an image stream from PIL and outputs the same image stream with watermarks

def put_watermark(im, WATERMARK_TEXT, FONT_LOCATION, FONT_SIZE, H_SPACING, V_SPACING, FONT_OPACITY):
    
    font = ImageFont.truetype(FONT_LOCATION, FONT_SIZE)
    watermark_text = WATERMARK_TEXT
    im_width, im_height = im.size
    
    drawing = ImageDraw.Draw(im)
    text_width, text_height = drawing.textsize(watermark_text, font)
    
    im_text = Image.new('RGBA', (text_width, (text_height)), (255, 255, 255, 0)) 
    drawing = ImageDraw.Draw(im_text)
    drawing.text((0,0), watermark_text, fill=(203,205,213, FONT_OPACITY), font=font)
    
    current_width = im_width
    current_height = im_height

    up_down = +1

    while current_width > text_width + H_SPACING:
        new_position = (current_width - text_width) - H_SPACING , current_height + (up_down * (V_SPACING//2))
        im.paste(im_text, new_position, im_text)
        current_width, current_height = new_position

        repeat_current_width, repeat_current_height = new_position

        while repeat_current_height > text_height + V_SPACING:
            repeat_new_position = repeat_current_width , (repeat_current_height - text_height - V_SPACING)
            im.paste(im_text, repeat_new_position, im_text)
            repeat_current_width, repeat_current_height = repeat_new_position

        up_down *= -1
        
    return im

# Usage

if os.path.isdir(INPUT_IMAGE_FILE):

    onlyfiles = [os.path.join(INPUT_IMAGE_FILE, f) for f in os.listdir(INPUT_IMAGE_FILE) if os.path.isfile(os.path.join(INPUT_IMAGE_FILE, f))]
    only_image_files = filter(lambda filename : filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')), onlyfiles)
    for file_path in only_image_files:
        try:
            im = Image.open(file_path) # opening image
            output = put_watermark(im, WATERMARK_TEXT, FONT_LOCATION, FONT_SIZE, H_SPACING, V_SPACING, FONT_OPACITY) # Getting watermarked outfile stream
            output.save(file_path+".watermarked.png") # saving file
        except Exception as e:
            print(e)

else:
    im = Image.open(INPUT_IMAGE_FILE) # opening image

    output = put_watermark(im, WATERMARK_TEXT, FONT_LOCATION, FONT_SIZE, H_SPACING, V_SPACING, FONT_OPACITY) # Getting watermarked outfile stream

    output.save(OUTPUT_IMAGE_FILE) # saving file