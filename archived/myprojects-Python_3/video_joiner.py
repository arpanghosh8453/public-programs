from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
desktop = os.path.expanduser("~")+"\\Desktop\\"

file_list = []
file_path = 'something'
count = 1
while file_path:
    try:
        file_path = input("Enter the ["+str(count)+"] video file path : ")
        if not file_path:
            break
        part_file = VideoFileClip(file_path)
        file_list.append(part_file)
        count += 1
    except Exception as e:
        print("Error occured : ")
        print(e)
final_clip = concatenate_videoclips(file_list)
out_name = input("\n\nEnter the outfile name : ")
final_clip.write_videofile(desktop+out_name+'.mp4')