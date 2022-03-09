"""Program to find certain kinds of files on your hard drive"""

import os


def over_certain_size():
    """Files over a certain size"""
    print("Starting directory is: {}\n".format(os.getcwd()))
    print()
    os.chdir('/Users/siddhanth/Documents')
    my_size = 100000000
    get_list = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for name in filenames:
            tug = os.path.join(directory_name, name)
            size = os.path.getsize(str(tug))
            if int(size) >= my_size:
                get_list.append(tug)
    print("List:")
    print(get_list)


def with_an_extension():
    """Files with a certain extension"""
    print("Starting directory is: {}\n".format(os.getcwd()))
    os.chdir('/Users/siddhanth/Documents')
    wanted_ex = 'mp4'
    get_list = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for name in filenames:
            extension = name.split('.')[-1]
            if extension == wanted_ex:
                get_list.append(os.path.join(directory_name, name))
    print("List:")
    print(get_list)


def certain_text():
    """Files containing certain text"""
    print("Starting directory is: {}\n".format(os.getcwd()))
    os.chdir('/Users/siddhanth/Documents/old stuff/Subjects')
    wanted_text = 'Introduction'
    get_list = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for name in filenames:
            dir_name = os.path.join(directory_name, name)
            in_file = open(dir_name, 'rb')
            contents = in_file.read().decode(errors='replace')
            if wanted_text in contents:
                get_list.append(dir_name)
            in_file.close()
    print("List:")
    print(get_list)


# over_certain_size()
# with_an_extension()
certain_text()
