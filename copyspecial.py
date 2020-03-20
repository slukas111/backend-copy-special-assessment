#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Sasha Lukas"


def get_special_paths(dir):
    """manipulate file paths"""
    new_paths = []
    files = os.listdir(dir)     
    for file in files:
        if re.search(r'__\w+__', file):
            new_paths.append(file)
    return new_paths

def copy_to(path, files):
    """copy special files to a directory"""
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Path Exists")

    for file in files:
        shutil.copy(file, path)
    """mod to make a copy"""

def zip_to(paths, zipoath):
    """creates zip files from special files"""
    paths = list(paths)
    command = "zip -j {} {}".format(zippath, ' '.join(paths))
    print("I am going to do: ")
    print(command)
    os.system(command)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    all_paths = get_special_paths(args.fromdir)

    if args.todir:
        copy_to(args.todir, all_paths)
    

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
