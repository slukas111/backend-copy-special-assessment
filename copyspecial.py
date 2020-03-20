# !/usr/bin/env python
# -*- coding: utf-8 - *-

import re
import os
import shutil
import argparse


"""Copyspecial Assignment"""

__author__ = "Chris Wilson, Koren, Sean, Julita"
__helped__ = "geeterista"


def get_spec_paths(dir):
    """ given dir name returns the appended
    results of the search for special files"""
    result = []
    file_directory = os.listdir(dir)
    for file_name in file_directory:
        if re.search(r'__\w+__', file_name):
            result.append(file_name)
    return result


def copy_to_dir(path, files):
    cwd = os.getcwd()
    if not os.path.exists(path):
        create_dir = 'mkdir -p {0}'.format(path)
        os.system(create_dir)
    else:
        print("Path exists")
    for file in files:
        os.chdir(cwd)
        shutil.copy(file, path)


def zip_to_file(paths, zippath):
    paths = list(paths)
    command = "zip -j {} {}".format(zippath, ' '.join(paths))
    print("Command I'm going to do: ")
    print(command)
    os.system(command)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='dir to look for local files')
    args = parser.parse_args()
    all_paths = get_spec_paths(args.fromdir)
    if args.todir:
        copy_to_dir(args.todir, all_paths)
    if args.tozip:
        zip_to_file(all_paths, os.path.join(os.getcwd(), args.tozip))

    if not args.todir and not args.tozip:
        for file in all_paths:
            print(os.path.abspath(file))


if __name__ == "__main__":
    main()
