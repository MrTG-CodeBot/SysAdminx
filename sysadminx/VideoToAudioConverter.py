import os
try:
    from moviepy import VideoFileClip
except ImportError:
    print("Run this command pip3 install -U -r requirements.txt")
    return None
        

class VideoToAudioConverter:
    def __init__(self):
        pass

    def convert_to_audio(self, vid_path: str, aud_path: str) -> tuple[str or None, bool, str or None]:
        if not os.path.exists(vid_path):
            print("Video file not found.")
            return None, False, "Video file not found."

        if not self.__video_check(vid_path):
            print("Invalid video file extension. Supported extensions: .mp4, .mkv")
            return None, False, "Invalid video file extension. Supported extensions: .mp4, .mkv"

        if not self.__audio_check(aud_path):
            print("Invalid audio file extension. Supported extensions: .mp3, .m4a")
            return None, False, "Invalid audio file extension. Supported extensions: .mp3, .m4a"

        try:
            video = VideoFileClip(vid_path)
            video.audio.write_audiofile(aud_path)
            video.close()
            if os.path.exists(aud_path):
                return aud_path, True, None
            else:
                print("Failed to create audio file.")
                return None, False, "Failed to create audio file."

        
        except Exception as e:
            print(f"Error converting video to audio: {e}")
            return None, False, str(e)

    def __video_check(self, vid_path: str) -> bool:
        return vid_path.lower().endswith((".mp4", ".mkv"))

    def __audio_check(self, aud_path: str) -> bool:
        return aud_path.lower().endswith((".mp3", ".m4a"))
