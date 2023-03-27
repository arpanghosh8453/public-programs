#!/usr/bin/env python
# coding: utf-8

# <H2> Standalone function </H2>

from PIL import Image, ImageDraw, ImageFont

# Use // for file names if you are facing issues
INPUT_IMAGE_FILE = r'C:\Users\Arpan Ghosh\Desktop\image.jpg'
OUTPUT_IMAGE_FILE = r'C:\Users\Arpan Ghosh\Desktop\filename_out.jpg'
FONT_LOCATION  = r'C:\Users\Arpan Ghosh\Desktop\Raleway-SemiBold.ttf'
FONT_SIZE = 20
H_SPACING = 70
V_SPACING = 90
FONT_OPACITY = 25
WATERMARK_TEXT = "@ARPAN"

# the following function reads an image stream from PIL and outputs the same image stream with watermarks

def put_watermark(im, WATERMARK_TEXT, FONT_LOCATION, FONT_SIZE, H_SPACING, V_SPACING, FONT_OPACITY):
    
    font = ImageFont.truetype(FONT_LOCATION, FONT_SIZE)
    watermark_text = WATERMARK_TEXT
    im_width, im_height = im.size
    
    drawing = ImageDraw.Draw(im)
    text_width, text_height = drawing.textsize(watermark_text, font)
    
    im_text = Image.new('RGBA', (text_width, (text_height)), (255, 255, 255, 0)) 
    drawing = ImageDraw.Draw(im_text)
    drawing.text((0,0), watermark_text, fill=(255,255,255, FONT_OPACITY), font=font)
    
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

im = Image.open(INPUT_IMAGE_FILE) # opening image

output = put_watermark(im, WATERMARK_TEXT, FONT_LOCATION, FONT_SIZE, H_SPACING, V_SPACING, FONT_OPACITY) # Getting watermarked outfile stream

output.save(OUTPUT_IMAGE_FILE) # saving file

