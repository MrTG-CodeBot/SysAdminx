from colorama import Fore, Style, init
import time

init(autoreset=True)

text = """
 │█████╗██╗   ██╗███████╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗  ██╗
 │╔════╝╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║╚██╗██╔╝
 │█████╗ ╚████╔╝ ███████╗███████║██║  ██║██╔████╔██║██║██╔██╗ ██║ ╚███╔╝
 │═══██║  ╚██╔╝  ╚════██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║ ██╔██╗
 │█████║   ██║   ███████║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██╔╝ ██╗
 │═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
 code by: https://github.com/MrTG-CodeBot
 1 Video To Audio
 2 Instagram Media Downloader
 3 Youtube Audio Downloader
 4 Format Changer
 0 Exit
"""
VIDEO_TO_AUDIO_CONVERTER_HELP = """
VideoToAudioConverter Help:

This class provides functionality to convert video files to audio files.

Usage:
    1. Create an instance of VideoToAudioConverter:
        converter = VideoToAudioConverter()

    2. Use the convert_to_audio method:
        audio_path, success, error_message = converter.convert_to_audio(video_path, audio_path)

Parameters:
    vid_path (str): The path to the input video file. Supported extensions are .mp4 and .mkv.
    aud_path (str): The path where the output audio file should be saved. Supported extension is .mp3.

Returns:
    tuple[str or None, bool, str or None]:
        - The path to the created audio file if successful, otherwise None.
        - A boolean indicating whether the conversion was successful (True) or not (False).
        - An error message (str) if the conversion failed, otherwise None.

Examples:
    Convert a video to audio:
        converter = VideoToAudioConverter()
        audio_path, success, error_message = converter.convert_to_audio("video.mp4", "audio.mp3")

        if success:
            print(f"Audio file created at: {audio_path}")
        else:
            print(f"Error: {error_message}")

Error Handling:
    - Returns (None, False, "Video file not found.") if the input video file does not exist.
    - Returns (None, False, "Invalid video file extension. Supported extensions: .mp4, .mkv") if the input video file has an unsupported extension.
    - Returns (None, False, "Invalid audio file extension. Supported extensions: .mp3") if the output audio file has an unsupported extension.
    - Returns (None, False, "Failed to create audio file.") if the audio file could not be created.
    - Returns (None, False, str(e)) if any other exception occurs during the conversion process.

Dependencies:
    - moviepy: Install using pip: pip install moviepy

Note:
    - Ensure that the input video file exists and has a valid extension.
    - Ensure that the output audio file path has a valid .mp3 extension.
"""
INSTA_DOWNLOADER_HELP = """
InstaMediaDownloader Help:

This class provides functionality to download media from Instagram, including stories, reels, TV posts, and regular posts.

Usage:
    1. Create an instance of InstaMediaDownloader:
        downloader = InstaMediaDownloader()

    2. Use the download_instagram_media method:
        downloader.download_instagram_media(media_link, output_path, download_thumbnail=False, download_caption=False, delete_txt_files=True)

Parameters:
    media_link (str): The Instagram link to the media you want to download. Supported links include:
        - Stories: https://www.instagram.com/stories/[username]/[story_id]
        - Reels: https://www.instagram.com/reel/[shortcode]/
        - TV Posts: https://www.instagram.com/tv/[shortcode]/
        - Posts: https://www.instagram.com/p/[shortcode]/

    output_path (str): The directory where you want to save the downloaded media.

    download_thumbnail (bool, optional): If True, downloads the thumbnail of videos. Defaults to False.

    download_caption (bool, optional): If True, saves the caption of the post as a .txt file. Defaults to False.

    delete_txt_files (bool, optional): If True, deletes any .txt files (captions) after downloading. Defaults to True.

Examples:
    Download a reel:
        downloader.download_instagram_media("https://www.instagram.com/reel/your_reel_shortcode/", "/path/to/downloads")

    Download a story:
        downloader.download_instagram_media("https://www.instagram.com/stories/username/1234567890", "/path/to/downloads")

    Download a post with caption and thumbnail:
        downloader.download_instagram_media("https://www.instagram.com/p/your_post_shortcode/", "/path/to/downloads", download_thumbnail=True, download_caption=True)

Error Handling:
    - ProfileNotExistsException: If the specified profile does not exist or is private.
    - StoryNotFoundException: If the specified story does not exist.
    - PostNotFoundException: If the specified post/reel does not exist.
    - General Exception: For other errors that may occur during the download process.

Note:
    - This script uses the instaloader library. Ensure it is installed: pip install instaloader.
    - For private profiles, you must be logged in using instaloader.
"""
YT_AUDIO_DOWNLOADER_HELP = """
YtAudioDownloader Help:

This class provides functionality to download audio from YouTube videos.

Usage:
    1. Create an instance of YtAudioDownloader:
        downloader = YtAudioDownloader()

    2. Use the download_youtube_audio method:
        downloader.download_youtube_audio(video_link, output_path, audio_format="mp3")

Parameters:
    video_link (str): The YouTube video URL.
    output_path (str): The directory where the audio file should be saved.
    audio_format (str, optional): The desired audio format ("mp3" or "wav"). Defaults to "mp3".

Examples:
    Download audio from a YouTube video as MP3:
        downloader = YtAudioDownloader()
        downloader.download_youtube_audio("https://www.youtube.com/watch?v=your_video_id", "/path/to/downloads", "mp3")

    Download audio from a YouTube video as WAV:
        downloader = YtAudioDownloader()
        downloader.download_youtube_audio("https://www.youtube.com/watch?v=your_video_id", "/path/to/downloads", "wav")

Error Handling:
    - "Invalid YouTube link.": If the provided video link is not a valid YouTube URL.
    - "Invalid YouTube URL.": If the provided URL causes a pytubefix.exceptions.RegexMatchError.
    - "Video is unavailable.": If the video is unavailable (pytubefix.exceptions.VideoUnavailable).
    - "Could not find suitable audio stream.": If no audio stream is found in the video.
    - "Unsupported audio format: [format]": If the requested audio format is not supported.
    - "Conversion to [format] failed.": If the conversion to the requested format fails.
    - "Error removing original file: [error]": If the original m4a file cannot be removed after conversion.
    - "An error occurred: [error]": For other unexpected errors during the download or conversion process.

Dependencies:
    - pytubefix: Install using pip: pip install pytubefix

Notes:
    - The downloader first downloads the audio stream as an m4a file.
    - If the requested format is "mp3" or "wav", it attempts to convert the m4a file to the specified format.
    - The original m4a file is deleted after successful conversion.
    - Ensure the output path exists, or it will be created.
    - Filenames are sanitized to replace invalid characters.
"""
FORMAT_CHANGER_HELP = """
FormatChanger Help:

This class provides functionality to change the format of files by copying their content, limited to photo-to-photo, video-to-video, and audio-to-audio conversions.

Usage:
    1. Create an instance of FormatChanger:
        changer = FormatChanger()

    2. Use the convert_format method:
        success = changer.convert_format(input_path, output_path)

Parameters:
    input_path (str): The path to the input file.
    output_path (str): The path where the output file should be saved, with the desired extension.

Returns:
    bool: True if the conversion (copying) was successful, False otherwise.

Supported File Types:
    - Photos: jpg, jpeg, png, bmp, gif, webp
    - Videos: mp4, avi, mov, mkv, webm
    - Audio: mp3, wav, ogg, flac, aac, m4a

Examples:
    Convert a PNG to JPG:
        changer = FormatChanger()
        success = changer.convert_format("image.png", "image.jpg")

    Convert an MP4 to AVI:
        changer = FormatChanger()
        success = changer.convert_format("video.mp4", "video.avi")

    Convert a WAV to MP3:
        changer = FormatChanger()
        success = changer.convert_format("audio.wav", "audio.mp3")

Error Handling:
    - "Error: Input file not found: [input_path]": If the input file does not exist.
    - "An unexpected error occurred: [error]": For other unexpected errors during the file copying process.
    - "Error: Only photo-to-photo, video-to-video, or audio-to-audio conversions are allowed.": If the conversion is attempted between different file types (e.g., photo to audio).

Note:
    - This class simply copies the content of the input file to the output file. It does not perform any actual format conversion or transcoding.
    - Ensure that the file extensions are correct and that the files are compatible with the requested output format.
    - If the input file is large, the copying process may take some time.
"""

def m_call():
    for line in text.splitlines():
        print(Fore.RED + line , end='\r' , flush=True)
        time.sleep(0.1)
        print(Fore.RED + line , flush=True)

    while True:
        print()
        choice = input("Enter your choice(To exit: 0): ")
        if choice == "0":
            print(Fore.RED + "Back To Main Page")
            break
        elif choice == "1":
            print(VIDEO_TO_AUDIO_CONVERTER_HELP)
        elif choice == "2":
            print(INSTA_DOWNLOADER_HELP)
        elif choice == "3":
            print(YT_AUDIO_DOWNLOADER_HELP)
        elif choice == "4":
            print(FORMAT_CHANGER_HELP)
