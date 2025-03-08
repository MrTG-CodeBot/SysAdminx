import pytubefix
import os
import re

class YtAudioDownloader:
    def __init__(self):
        pass

    def __convert_format(self,input_path: str , output_path: str) -> tuple[bool , str] or tuple[bool , None]:
        try:
            with open(input_path , 'rb') as f:
                file = f.read()
            with open(output_path , 'wb') as fi:
                fi.write(file)
            return True , output_path
        except Exception as e:
            print(f"Error during conversion: {e}")
            return False , None

    def __sanitize_filename(self, filename: str) -> str:
        return re.sub(r'[<>:"/\\|?*]' , '_' , filename)

    def download_youtube_audio(self, video_link , output_path , audio_format="mp3"):

        if not re.search(r"youtube\.com|youtu\.be" , video_link):
            print("Invalid YouTube link.")
            return

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        try:
            yt = pytubefix.YouTube(video_link)
            audio_stream = yt.streams.filter(only_audio=True).first()

            if audio_stream:
                filename = self.__sanitize_filename(audio_stream.default_filename)
                filepath = os.path.join(output_path , filename)

                audio_stream.download(output_path , filename=filename)

                if audio_format.lower() in ("mp3" , "wav"):
                    input_file_path = filepath
                    if filename.endswith(".m4a"):
                        if audio_format.lower() == "mp3":
                            output_file_path = input_file_path.replace('.m4a' , '.mp3')
                            success , path = self.__convert_format(input_file_path , output_file_path)

                        elif audio_format.lower() == "wav":
                            output_file_path = input_file_path.replace('.m4a' , '.wav')
                            success , path = self.__convert_format(input_file_path , output_file_path)
                        else:
                            success = False
                            output_file_path = None

                        if success:
                            try:
                                os.remove(input_file_path)
                                print(f"The audio is saved to {path}, format: {path.split('.')[1]}")
                            except Exception as e:
                                print(f"Error removing original file: {e}")
                        else:
                            print(f"Conversion to {audio_format} failed.")

                    else:
                        print(f"Audio downloaded as m4a, but not converted as requested format {audio_format}")

                else:
                    print(f"Unsupported audio format: {audio_format}")

            else:
                print("Could not find suitable audio stream.")

        except pytubefix.exceptions.RegexMatchError:
            print("Invalid YouTube URL.")
        except pytubefix.exceptions.VideoUnavailable:
            print("Video is unavailable.")
        except Exception as e:
            print(f"An error occurred: {e}")

