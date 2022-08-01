from video_tiktok_to_gif import core as tiktok
import sys
import re
import os
import shutil


def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f"{filename} deleted.")
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def check_argv():

    if len(sys.argv) != 2:
        print(f'Must be only one argument(ULR). Given {len(sys.argv[1:])}')
        exit()

    url_check = re.match('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', sys.argv[-1])
    if url_check is not None:
        print('Incorrect URL')
        exit()


check_argv()
clear_folder('./gif')
clear_folder('./video')
url = sys.argv[-1]

if __name__ == '__main__':
    response = tiktok.get_video(url)
    file_extension = tiktok.get_extension(response.headers)
    filename = tiktok.write_video_to_file(response.content, file_extension)
    tiktok.convert_to_gif(filename)
