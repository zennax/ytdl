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

if __name__ == "__main__":
    url = input("Enter the URL of a YouTube video: ")
    output_directory = input("Enter the output directory (press Enter for current directory): ") or "."
    filename = download(url, output_directory)
    print(f"Download complete. Audio saved as {filename}.")
    print(" /\_/\ ")
    print("( o o )")
    print(" > ^ < ")