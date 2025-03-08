#Download the file sysadminx/VideoToAudioConverter.py
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
