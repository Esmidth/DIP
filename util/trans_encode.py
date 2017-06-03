# this script is used to transform code from GB2312(Windows default) to UTF 8

import os
import sys
import codecs


def convert(file, in_enc="GB2312", out_enc="UTF-8"):
    if 'jpg' in file:
        pass
    elif 'DS' in file:
        pass
    else:
        try:
            print('convert' + file)
            f = codecs.open(file, 'r', in_enc)
            new_content = f.read()
            codecs.open(file, 'w', out_enc).write(new_content)
        except IOError as err:
            print('I/O error:{0}'.format(err))


def explore(para_dir):
    for root, dirs, files in os.walk(para_dir):
        for file in files:
            path = os.path.join(root, file)
            convert(path)


def main():
    path = input("Please input path: \n")
    if os.path.isfile(path):
        convert(path)
    elif os.path.isdir(path):
        explore(path)


if __name__ == "__main__":
    main()
