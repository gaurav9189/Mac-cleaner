import os
from pathlib import Path
import shutil


ext_doc = ['html', 'pdf', 'xml', 'xls',
           'xlsx', 'ppt', 'pptx', 'docx', 'doc', 'odt', 'rtf', 'Pdf', 'PDF']
ext_pkg = ['dmg', 'tar', 'zip', 'pkg']
ext_img = ['png', 'jpg', 'jpeg', 'JPG', 'HEIC', 'drawio']
ext_sec = ['csv', 'pem']
ext_misc = ['ica', 'ics', 'exe']

extension = {'Downloads_Documents': ext_doc,
             'Downloads_Images': ext_img,
             'Downloads_Pkgs': ext_pkg,
             'Downloads_Secrets': ext_sec,
             0: ext_misc}


class Cleanup:
    def __init__(self, cwd):
        if os.path.isdir(cwd) and os.path.exists(cwd):
            self.cwd = cwd
        # else:
        #     return None

    def contents(self):
        try:
            return os.listdir(path=self.cwd)
        except AttributeError as fn:
            return f'Check your path {fn}'

    def get_files(self):
        try:
            files = [os.path.join(self.cwd, file) for file in os.listdir(
                path=self.cwd) if os.path.isfile(os.path.join(self.cwd, file))]
            return files
        except AttributeError as er:
            return f'Check your filepath: {er}'

    def get_subdirs(self):
        try:
            dirs = [os.path.join(self.cwd, dr) for dr in os.listdir(
                path=self.cwd) if os.path.isdir(os.path.join(self.cwd, dr))]
            return dirs
        except AttributeError as er:
            return f'Check your filepath: {er}'

    def move(self, src, dest):
        try:
            if os.path.isdir(dest):
                shutil.move(src, dest)
                print(f'Moved {src} to {dest}')
        except:
            return 'Destination folder has issue, check'

    def remove_files(self, file):
        try:
            os.remove(file)
            # os.path.isfile(file)
        except FileNotFoundError as er:
            return f'Can not find this file: {er}'
        except OSError as er:
            return f'Can not be a Directory: {er}'


def type_finder(file, extension):
    file_ext = file.split(sep='.')[-1]
    for dest, v in extension.items():
        for ext in v:
            if file_ext == ext:
                return dest


def check_dest(dest_folder):
    if os.path.isdir(dest_folder):
        return dest_folder
    print('Destination not a folder')
    raise OSError


if __name__ == '__main__':
    def file_move(cleanup, dest_prefix):
        for file in cleanup.get_files():
            dest = type_finder(file, extension)
            if dest:
                dest_folder = check_dest(
                    dest_prefix + str(dest))
                cleanup.move(file, dest_folder)
            elif dest == 0:
                cleanup.remove_files(file)
                print(f'{file} removed')

    downloads = Cleanup('/Users/deepaliyadav/Downloads')
    file_move(downloads, '/Users/deepaliyadav/Documents/')
