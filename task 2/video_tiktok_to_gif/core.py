import requests
from moviepy.editor import VideoFileClip
from time import time


def get_video(url: str) -> requests:
    response = requests.get(url, allow_redirects=True, stream=True)
    print(f'File downloaded')
    return response


def get_extension(headers: requests) -> str:
    result = 'mp4'

    for header in headers:
        if 'Content-Type' in header:
            result = headers[header].split('/')[-1]

    return result


def write_video_to_file(content: bytes, extension: str) -> str:
    filename = "file-{}.{}".format(int(time() * 1000), extension)

    with open(f"video/{filename}", "wb") as file:
        file.write(content)

    print(f'Finished to write video file video/{filename}')
    return filename


def convert_to_gif(filename: str) -> None:
    video_clip = VideoFileClip(f'./video/{filename}')
    video_clip.write_gif(f"gif/{filename.split('.')[0]}.gif")
    video_clip.close()
    print(f'Gif complete written to file .gif/{filename.split(".")[0]}.gif')
