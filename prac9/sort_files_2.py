"""Sort files in Files to sort Version 2"""

import os
import shutil


def main():
    """main"""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('FilesToSort')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    # dir_dict = {'xls': 'Spreadsheets', 'txt': 'Docs', 'xlsx': 'Spreadsheets', 'png': 'Images', 'jpg': 'Images',
    #             'doc': 'Docs', 'docx': 'Docs', 'gif': 'Images'}
    dir_dict = {}
    # dir_list = ['xls', 'txt', 'xlsx', 'png', 'jpg', 'doc', 'docx', 'gif']
    dir_list = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in dir_list:
            dir_list.append(extension)
            new_dir = input(f"What category would you like to sort {extension} files into? ")
            dir_dict[extension] = new_dir
        try:
            os.mkdir(dir_dict[extension])
        except FileExistsError:
            pass
        shutil.move(filename, f'{dir_dict[extension]}/')


main()
