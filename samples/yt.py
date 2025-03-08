# Download the file sysadminx/YtAudioDownloader.py
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
