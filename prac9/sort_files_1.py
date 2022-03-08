"""Sort files in Files to sort Version 1"""

import os
import shutil


def main():
    """main"""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('FilesToSort')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    extension_list = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(filename, f'{extension}/')
        extension_list.append(extension)
    print(extension_list)


main()
