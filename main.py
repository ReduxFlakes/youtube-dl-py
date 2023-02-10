import youtube_dl

# set's the config for audio using ffmped


def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# user input
if __name__ == '__main__':
    youtube_link = input("Enter the youtube link: ")
    download_audio(youtube_link)
    print("Video downloaded and converted to mp3 successfully!")
