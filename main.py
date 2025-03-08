from colorama import Fore , Style , init
import time

init(autoreset=True)

text = """

 │█████╗██╗   ██╗███████╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗  ██╗
 │██═══╝╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║╚██╗██╔╝
 │█████╗ ╚████╔╝ ███████╗███████║██║  ██║██╔████╔██║██║██╔██╗ ██║ ╚███╔╝
 │═══██║  ╚██╔╝  ╚════██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║ ██╔██╗
 │█████║   ██║   ███████║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██╔╝ ██╗
 │═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
 code by: https://github.com/MrTG-CodeBot

 
 1 Video To Audio
 2 Instagram Media Downloader
 3 Youtube Video Downloader
 4 Youtube Audio Downloader
 5 Format Changer
 6 Help Message
 7 Exit
"""
for line in text.splitlines():
    print(Fore.RED + line , end='\r' , flush=True)
    time.sleep(0.1)
    print(Fore.RED + line , flush=True)

choice = input("Enter your choice: ")
if choice == "1":
    from sysadminx import VideoToAudioConverter
    converter = VideoToAudioConverter()

    video_path = input("Enter the path to the video file: ")
    audio_path = input("Enter the path to save the audio file: ")

    if '"' in video_path or audio_path:
        video_path = video_path.replace('"' , '')
        audio_path = audio_path.replace('"' , '')

    audio_file , success , error_message = converter.convert_to_audio(video_path , audio_path)

    if success:
        print(Fore.RED + f"Audio file saved to: {audio_file}")
    else:
        print(Fore.RED + f"Conversion failed: {error_message}")
