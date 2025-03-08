#Download the file sysadminx/FormatChanger.py
from sysadminx.FormatChanger import FormatChanger
h = """ 
photo_extensions = ["jpg", "jpeg", "png", "bmp", "gif", "webp"]
video_extensions = ["mp4", "avi", "mov", "mkv", "webm"]
audio_extensions = ["mp3", "wav", "ogg", "flac", "aac", "m4a"]"""
print(h)

print("Entering the path you should add the extension also")
print()
input_file = input("Enter the path of the file to change the format: ")
output_file = input("Enter the path to save the file: ")


r = FormatChanger()

input_file = input_file.strip('"')
output_file = output_file.strip('"')

result = r.convert_format(input_path=input_file , output_path=output_file)

if result:
    print(f"File copied successfully: {input_file} -> {output_file}")
