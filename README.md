
### Media Downloader & Converter Toolkit

A comprehensive Python toolkit for downloading and converting various media types including YouTube audio, Instagram media, and video-to-audio conversion.

Thought for 1 second### Media Downloader & Converter Toolkit

A comprehensive Python toolkit for downloading and converting various media types including YouTube audio, Instagram media, and video-to-audio conversion.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Components](#components)

- [YouTube Audio Downloader](#youtube-audio-downloader)
- [Format Changer](#format-changer)
- [Instagram Media Downloader](#instagram-media-downloader)
- [Video to Audio Converter](#video-to-audio-converter)



- [Usage Examples](#usage-examples)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)


## Features

- Download audio from YouTube videos in MP3 or WAV format
- Convert between media formats (photos, videos, audio)
- Download Instagram posts, reels, stories, and IGTV videos
- Extract audio from video files
- Simple and easy-to-use API


## Installation

1. Clone the repository:
2. Thought for 1 second### Media Downloader & Converter Toolkit

A comprehensive Python toolkit for downloading and converting various media types including YouTube audio, Instagram media, and video-to-audio conversion.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Components](#components)

- [YouTube Audio Downloader](#youtube-audio-downloader)
- [Format Changer](#format-changer)
- [Instagram Media Downloader](#instagram-media-downloader)
- [Video to Audio Converter](#video-to-audio-converter)



- [Usage Examples](#usage-examples)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)


## Features

- Download audio from YouTube videos in MP3 or WAV format
- Convert between media formats (photos, videos, audio)
- Download Instagram posts, reels, stories, and IGTV videos
- Extract audio from video files
- Simple and easy-to-use API


## Installation

1. Clone the repository:


```shellscript
git clone https://github.com/yourusername/media-toolkit.git
cd media-toolkit
```

2. Install the required dependencies:


```shellscript
pip install pytubefix instaloader moviepy
```

## Components

### YouTube Audio Downloader

Downloads audio from YouTube videos and converts them to MP3 or WAV format.

```python
from YtAudioDownloader import YtAudioDownloader

# Initialize the downloader
downloader = YtAudioDownloader()

# Download audio from a YouTube video
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
output_directory = "./downloads"
audio_format = "mp3"  # or "wav"

# Download and convert
downloader.download_youtube_audio(video_url, output_directory, audio_format)
```

### Format Changer

Converts between media formats of the same type (photo-to-photo, video-to-video, audio-to-audio).

```python
from FormatChanger import FormatChanger

# Initialize the format changer
converter = FormatChanger()

# Convert an audio file from one format to another
input_file = "./downloads/audio.m4a"
output_file = "./downloads/audio.mp3"

# Perform the conversion
success = converter.convert_format(input_file, output_file)

if success:
    print(f"Successfully converted {input_file} to {output_file}")
else:
    print("Conversion failed")
```

### Instagram Media Downloader

Downloads media from Instagram posts, reels, stories, and IGTV.

```python
from InstaMediaDownloader import InstaMediaDownloader

# Initialize the downloader
insta_downloader = InstaMediaDownloader()

# Download a post
post_url = "https://www.instagram.com/p/EXAMPLE_POST_ID/"
output_directory = "./instagram_downloads"

# Download the post
insta_downloader.download_instagram_media(
    post_url, 
    output_directory,
    download_thumbnail=True,  # Download video thumbnails
    download_caption=False,   # Don't download captions
    delete_txt_files=True     # Delete text files after download
)

# Download a reel
reel_url = "https://www.instagram.com/reel/EXAMPLE_REEL_ID/"
insta_downloader.download_instagram_media(reel_url, output_directory)

# Download a story
story_url = "https://www.instagram.com/stories/username/EXAMPLE_STORY_ID/"
insta_downloader.download_instagram_media(story_url, output_directory)
```

### Video to Audio Converter

Extracts audio from video files.

```python
from VideoToAudioConverter import VideoToAudioConverter

# Initialize the converter
converter = VideoToAudioConverter()

# Convert a video file to audio
video_path = "./videos/example.mp4"
audio_path = "./audio/example.mp3"

# Perform the conversion
output_path, success, error_message = converter.convert_to_audio(video_path, audio_path)

if success:
    print(f"Audio extracted successfully to: {output_path}")
else:
    print(f"Error: {error_message}")
```
