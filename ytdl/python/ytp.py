#Simple tool to download music
import os
import pytube
import threading

def on_progress(stream, chunk, remaining):
    """
    Show the download progress as a percentage.
    """
    downloaded = stream.filesize - remaining
    percent = (downloaded / stream.filesize) * 100
    print(f"Downloading... {percent:.2f}% complete")

def download(url, output_dir="."):
    """
    Download the audio from a YouTube video using PyTube and return the filename.
    """
    try:
        yt = pytube.YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=output_dir)
        filename = os.path.join(output_dir, stream.default_filename[:-4] + ".mp3")
        os.rename(os.path.join(output_dir, stream.default_filename), filename)
        return filename
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def download_playlist(playlist_url, output_dir="."):
    """
    Download all videos in a playlist and save as mp3.
    """
    playlist = pytube.Playlist(playlist_url)
    threads = []
    for url in playlist.video_urls:
        t = threading.Thread(target=download, args=(url, output_dir))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    playlist_url = input("Enter the URL of a YouTube playlist: ")
    output_directory = input("Enter the output directory (press Enter for current directory): ") or "."
    download_playlist(playlist_url, output_directory)
    print("Download complete.")
    print(" /\\_/\\ ")
    print("( o o )")
    print(" > ^ < ")