import os

class FormatChanger:
    def __init__(self):
        pass

    def convert_format(self, input_path: str , output_path: str) -> bool:

        photo_extensions = ["jpg" , "jpeg" , "png" , "bmp" , "gif" , "webp"]
        video_extensions = ["mp4" , "avi" , "mov" , "mkv" , "webm"]
        audio_extensions = ["mp3" , "wav" , "ogg" , "flac" , "aac" , "m4a"]

        input_extension = input_path.split('.')[-1].lower()
        output_extension = output_path.split('.')[-1].lower()

        if input_extension in photo_extensions and output_extension in photo_extensions:
            try:
                with open(input_path , 'rb') as f_in:
                    with open(output_path , 'wb') as f_out:
                        f_out.write(f_in.read())
                return True
                print(f"File copied successfully: {input_path} -> {output_path}")
            except FileNotFoundError:
                print(f"Error: Input file not found: {input_path}")
                return False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return False

        elif input_extension in video_extensions and output_extension in video_extensions:
            try:
                with open(input_path , 'rb') as f_in:
                    with open(output_path , 'wb') as f_out:
                        f_out.write(f_in.read())
                return True
                print(f"File copied successfully: {input_path} -> {output_path}")
            except FileNotFoundError:
                print(f"Error: Input file not found: {input_path}")
                return False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return False

        elif input_extension in audio_extensions and output_extension in audio_extensions:
            try:
                with open(input_path , 'rb') as f_in:
                    with open(output_path , 'wb') as f_out:
                        f_out.write(f_in.read())
                return True
                print(f"File copied successfully: {input_path} -> {output_path}")
            except FileNotFoundError:
                print(f"Error: Input file not found: {input_path}")
                return False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return False

        else:
            print("Error: Only photo-to-photo, video-to-video, or audio-to-audio conversions are allowed.")
            return False
