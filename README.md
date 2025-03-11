```shellscript
 │███████╗██╗   ██╗███████╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗  ██╗
 │██╔════╝╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║╚██╗██╔╝
 │███████╗ ╚████╔╝ ███████╗███████║██║  ██║██╔████╔██║██║██╔██╗ ██║ ╚███╔╝
 │╚════██║  ╚██╔╝  ╚════██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║ ██╔██╗
 │███████║   ██║   ███████║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██╔╝ ██╗
 │╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
```

### Media Downloader & Converter Toolkit

A comprehensive Python toolkit for downloading and converting various media types including YouTube audio, Instagram media, and video-to-audio conversion.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Components](#components)

- [YouTube Audio Downloader](#youtube-audio-downloader)
- [Format Changer](#format-changer)
- [Instagram Media Downloader](#instagram-media-downloader)
- [Video to Audio Converter](#video-to-audio-converter)
- [Docx to Pdf converter](#docx-to-pdf-converter)



- [License](#license)


## Features

- Download audio from YouTube videos in MP3 or WAV format
- Convert between media formats (photos, videos, audio)
- Download Instagram posts, reels, stories, and IGTV videos
- Extract audio from video files

## Installation

1. Clone the repository:


```shellscript
git clone https://github.com/MrTG-CodeBot/SysAdminx.git
cd SysAdminx
pip3 install -U -r requirements.txt
python3 main.py
```

2. Install the required dependencies:


```shellscript
pip install pytubefix instaloader moviepy
```
or
```shellscript
pip3 install -U -r requirements.txt
```

## Components

### YouTube Audio Downloader

Downloads audio from YouTube videos and converts them to MP3 or WAV format.

```python
from sysadminx.YtAudioDownloader import YtAudioDownloader

downloader = YtAudioDownloader()

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
output_directory = "./downloads"
audio_format = "mp3"  # or "wav"

downloader.download_youtube_audio(video_url, output_directory, audio_format)
```

### Format Changer

Converts between media formats of the same type (photo-to-photo, video-to-video, audio-to-audio).

```python
from sysadminx.FormatChanger import FormatChanger

converter = FormatChanger()

input_file = "./downloads/audio.m4a"
output_file = "./downloads/audio.mp3"

success = converter.convert_format(input_file, output_file)

if success:
    print(f"Successfully converted {input_file} to {output_file}")
else:
    print("Conversion failed")
```

### Instagram Media Downloader

Downloads media from Instagram posts, reels, stories, and IGTV.

```python
from sysadminx.InstaMediaDownloader import InstaMediaDownloader

insta_downloader = InstaMediaDownloader()

post_url = "https://www.instagram.com/p/EXAMPLE_POST_ID/"
output_directory = "./instagram_downloads"

insta_downloader.download_instagram_media(
    post_url, 
    output_directory,
    download_thumbnail=True,  
    download_caption=False,   
    delete_txt_files=True    
)

reel_url = "https://www.instagram.com/reel/EXAMPLE_REEL_ID/"
insta_downloader.download_instagram_media(reel_url, output_directory)

story_url = "https://www.instagram.com/stories/username/EXAMPLE_STORY_ID/"
insta_downloader.download_instagram_media(story_url, output_directory)
```

### Video to Audio Converter

Extracts audio from video files.

```python
from sysadminx.VideoToAudioConverter import VideoToAudioConverter

converter = VideoToAudioConverter()

video_path = "./videos/example.mp4"
audio_path = "./audio/example.mp3"

output_path, success, error_message = converter.convert_to_audio(video_path, audio_path)

if success:
    print(f"Audio extracted successfully to: {output_path}")
else:
    print(f"Error: {error_message}")
```

### Docx to Pdf Converter

Convert the DOcx file to Pdf 

```python
from sysadminx.Docs2pdf import Docs2pdf

converter = Docs2pdf()

success = converter.convert2pdf(input_path, output_path)
if success:
   print("Done")
else:
   print("Error occured")
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/MrTG-CodeBot/SysAdminx/blob/main/LICENSE) file for details.
