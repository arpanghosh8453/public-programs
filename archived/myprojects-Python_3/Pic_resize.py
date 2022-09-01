from PIL import Image
import glob
import io
import os
from pathlib import Path


def compress(original_file, max_size, save_file):
    save_opts = {'optimize': True, 'quality': 95, 'format': 'jpeg'}
    orig_image = Image.open(original_file)
    width, height = orig_image.size
    scales = [scale / 1000 for scale in range(1, 1001)]  # e.g. [0.001, 0.002 ... 1.0]

    lo = 0
    hi = len(scales)

    while lo < hi:
        mid = (lo + hi) // 2

        scaled_size = (int(width * scales[mid]), int(height * scales[mid]))
        resized_file = orig_image.resize(scaled_size, Image.ANTIALIAS)

        file_bytes = io.BytesIO()
        resized_file.save(file_bytes, **save_opts)
        size = file_bytes.tell()
        # print(size, scales[mid])

        if size < max_size: 
            lo = mid + 1
        else: 
            hi = mid

    scale = scales[max(0, lo-1)]
    print("Using scale:", scale, "to file", original_file)
    orig_image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS).save(save_file, **save_opts)


def get_output_path(original_path):
    p = Path(original_path)
    if not os.path.exists(str(p.parent)+"\\Resized_files"):
        os.makedirs(str(p.parent)+"\\Resized_files")
    return str(p.parent)+"\\Resized_files\\"+str(p.name)


# folder_path = r"C:\Users\Arpan Ghosh\Desktop\test"
folder_path = input("Enter the folder path : ")
if folder_path[0] == '"':
    folder_path = folder_path[1:-1]
file_list = glob.glob(folder_path+"\\*.*")
# print(file_list)
print("")
for file in file_list:
    try:
        im = Image.open(file)
        im.close()
        outpath = get_output_path(file)
        compress(file, 19900, outpath)
        print("Successfully saved as", outpath, "\n")
    except IOError:
        pass
