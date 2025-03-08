import instaloader
import re
import os
class InstaMediaDownloader:
    def __init__(self):
        pass

    def download_instagram_media(self,media_link: str , output_path: str , download_thumbnail: bool = False ,
                                 download_caption: bool = False , delete_txt_files: bool = True) -> None:

        L = instaloader.Instaloader(dirname_pattern=output_path , download_videos=True , download_pictures=True ,
                                    download_video_thumbnails=download_thumbnail , save_metadata=download_caption ,
                                    compress_json=False , )

        try:
            if "stories" in media_link:
                match = re.search(r"/stories/([^/]+)/(\d+)" , media_link)
                if match:
                    username = match.group(1)
                    story_id = int(match.group(2))
                    L.download_stories([story_id] , user=username)

            elif "reel" in media_link or "tv" in media_link:
                post_shortcode = media_link.split("/reel/")[1].split("/")[0] if "/reel/" in media_link else \
                media_link.split("/tv/")[1].split("/")[0] if "/tv/" in media_link else None

                if post_shortcode:
                    L.download_post(instaloader.Post.from_shortcode(L.context , post_shortcode) , target=output_path)
                else:
                    print("Invalid reel/tv link.")

            elif "/p/" in media_link:
                post_shortcode = media_link.split("/p/")[1].split("/")[0]
                if post_shortcode:
                    L.download_post(instaloader.Post.from_shortcode(L.context , post_shortcode) , target=output_path)
                else:
                    print("Invalid post link.")
            else:
                print("Invalid Instagram link.")

            if delete_txt_files:
                for filename in os.listdir(output_path):
                    if filename.lower().endswith(".txt"):
                        file_path = os.path.join(output_path , filename)
                        try:
                            os.remove(file_path)
                        except Exception as delete_error:
                            print(f"Error deleting {filename}: {delete_error}")

        except instaloader.exceptions.ProfileNotExistsException:
            print("Profile not found or is private.")
        except instaloader.exceptions.StoryNotFoundException:
            print("Story not found.")
        except instaloader.exceptions.PostNotFoundException:
            print("Post/Reel not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


