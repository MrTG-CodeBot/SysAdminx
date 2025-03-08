#Download the file sysadminx/InstaMediaDownloader.py
from sysadminx.InstaMediaDownloader import InstaMediaDownloader

i = InstaMediaDownloader()
media_link = input("Enter Instagram media link: ")
output_path = input("Enter output directory: ")

output_path = output_path.strip('"')

if not os.path.exists(output_path):
    try:
        os.makedirs(output_path)
    except OSError as e:
        print(Fore.RED + f"Error creating directory: {e}")

i.download_instagram_media(media_link, output_path)
