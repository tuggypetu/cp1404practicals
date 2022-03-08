"""Check if song files have copyright text"""

import os


def main():
    """Demo os module functions."""
    copyright_text = '.i'
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    lyric_dir_list = os.listdir('.')
    total, yes_no = 0, 0
    missing_text_dict = {}
    for i in lyric_dir_list:
        os.chdir(f'./{i}')
        for filename in os.listdir('.'):
            # Ignore directories, just process files
            if os.path.isdir(filename):
                continue
            in_file = open(filename, 'rb')
            total += 1
            # for line in in_file:
            #     if copyright_text in line:
            #         yes_no += 1
            #     else:
            #         yes_no -= 1
            #         missing_text_dict[filename] = os.getcwd()

            contents = in_file.read().decode(errors='replace')
            if copyright_text in contents:
                yes_no += 1
            else:
                d_path = os.getcwd()
                the_path = d_path.split('/')[-2] + '/' + d_path.split('/')[-1]
                missing_text_dict[filename] = the_path
            in_file.close()

        os.chdir(f'{os.path.dirname(os.getcwd())}')

    # print(missing_text_dict)
    for song in missing_text_dict:
        print(song, ":", missing_text_dict[song])
    print('\n', total, "total number of files")
    print('', yes_no, "files has the copyright line")
    print('', len(missing_text_dict), "files does not have the copyright line")


main()
