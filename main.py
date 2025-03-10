from colorama import Fore, Style, init
import time
import os
from Helpmsg import m_call

init(autoreset=True)


text = """
 │███████╗██╗   ██╗███████╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗  ██╗
 │██╔════╝╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║╚██╗██╔╝
 │███████╗ ╚████╔╝ ███████╗███████║██║  ██║██╔████╔██║██║██╔██╗ ██║ ╚███╔╝
 │╚════██║  ╚██╔╝  ╚════██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║ ██╔██╗
 │███████║   ██║   ███████║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██╔╝ ██╗
 │╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
 code by: https://github.com/MrTG-CodeBot
 1 Video To Audio
 2 Instagram Media Downloader
 3 Youtube Audio Downloader
 4 Format Changer
 5 Docx To Pdf converter
 6 Help Message
 0 Exit
"""
h = """ 
photo_extensions = ["jpg", "jpeg", "png", "bmp", "gif", "webp"]
video_extensions = ["mp4", "avi", "mov", "mkv", "webm"]
audio_extensions = ["mp3", "wav", "ogg", "flac", "aac", "m4a"]"""

for line in text.splitlines():
    print(Fore.RED + line, end='\r', flush=True)
    time.sleep(0.1)
    print(Fore.RED + line, flush=True)

while True:
    print()
    choice = input("Enter your choice(To exit: 0): ")
    if choice == "0":
        print(Fore.RED + "Terminated")
        break
    elif choice == "1":
        from sysadminx.VideoToAudioConverter import VideoToAudioConverter
        converter = VideoToAudioConverter()

        video_path = input("Enter the path to the video file: ")
        audio_path = input("Enter the path to save the audio file: ")

        video_path = video_path.strip('"')
        audio_path = audio_path.strip('"')

        audio_file, success, error_message = converter.convert_to_audio(video_path, audio_path)

        if success:
            print(Fore.RED + f"Audio file saved to: {audio_file}")
        else:
            print(Fore.RED + f"Conversion failed: {error_message}")
    elif choice == "2":
        from sysadminx.InstaMediaDownloader import InstaMediaDownloader
        i = InstaMediaDownloader()
        media_link = input("Enter Instagram media link: ")
        output_path = input("Enter output directory: ")

        output_path = output_path.strip('"')

        if not os.path.exists(output_path):
            try:
                os.makedirs(output_path)
            except OSError as e:
                print(Fore.RED + f"Error creating directory: {e}")
                continue

        i.download_instagram_media(media_link, output_path)

    elif choice == "3":
        from sysadminx.YtAudioDownloader import YtAudioDownloader
        yt = YtAudioDownloader()  
        video_link = input("Enter YouTube video link: ")
        output_path = input("Enter output directory: ")
        audio_format = input("Enter output audio format (mp3 or wav): ")

        output_path = output_path.strip('"')

        if not os.path.exists(output_path):
            try:
                os.makedirs(output_path)
            except OSError as e:
                print(Fore.RED + f"Error creating directory: {e}")
                continue

        yt.download_youtube_audio(video_link, output_path, audio_format)

    elif choice == "4":
        from sysadminx.FormatChanger import FormatChanger
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
    elif choice == "5":
        from sysadminx.Docs2pdf import Docs2pdf
        g = Docs2pdf()
        ipath = input("Enter the path of the Docx file to change the format to pdf: ")
        opath = input("Enter the path to save the file: ")

        ipath = ipath.strip('"')
        opath = output_file.strip('"') 
        success = g.convert2pdf(ipath, opath)
        if success:
           print("Done")
        else:
           print("Error occured")
    elif choice == "6":
        m_call()
    else:
        print(Fore.RED + "Invalid choice")
