#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import shutil
import subprocess as sp
import sys
import traceback

import requests

idLists = []


# Author: Anbuselvan Rocky
# Facebook: fb.me/anburocky3
# Github: github.com/anburocky3

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def exists(site, path):
    r = requests.head(site + path)
    return r.status_code == requests.codes.ok


def checkFileExist(file_path, file_name, cycle):
    i = 1
    print(BColors.WARNING + "Searching files. . . . .")
    while i < cycle:
        print(BColors.OKGREEN +
              "-----------------------------------------------------------------------")
        if exists(file_path, file_name % i):
            ids = file_name % i
            idLists.append(ids)
            print(BColors.OKBLUE + " INFO: " + BColors.OKGREEN + "File exists: " + file_name % i)
            i += 1
        else:
            print(
                BColors.FAIL + "-----------------------------------------------------------------------")
            print(BColors.FAIL + " INFO: " + BColors.FAIL + "File not exist: " + file_name % i)
            print(
                BColors.FAIL + "-----------------------------------------------------------------------")
            # print(BColors.WARNING + " Skipping. . .")
            i += 1


def createFolder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def welcomeBanner():
    sp.call('cls', shell=True)
    sp.call('clear', shell=True)

    print(BColors.OKGREEN + """
--------------------------------------------------------------------------------
|         _____                   _       _                _                   |
|        |  __ \                 | |     | |              (_)                  |
|        | |__) |__ _  __ _  __ _| | __ _| |__   __ _ _ __ _                   |
|        |  _  // _` |/ _` |/ _` | |/ _` | '_ \ / _` | '__| |                  |
|        | | \ \ (_| | (_| | (_| | | (_| | | | | (_| | |  | |   V1.O           |
|        |_|  \_\__,_|\__, |\__,_|_|\__,_|_| |_|\__,_|_|  |_|                  |
|                      __/ |                                                   |
|                     |___/                                                    |""" + BColors.OKGREEN + """
|                                                                              |
|  Description: This tool will help you to download automatic High Quality(HQ) |
|               images from ragalahari site.                                   |
--------------------------------------------------------------------------------""")

    print("|=============================================================================|")
    print(
        BColors.OKBLUE + "|          Programmer: Anbuselvan Rocky   | fb.me/anburocky3                  |" + BColors.ENDC)
    print("|=============================================================================| \n")


def downloadImg(file_path, folder_name):
    print(BColors.OKGREEN +
          "-----------------------------------------------------------------------")
    os.chdir(folder_name)
    for x in idLists:
        r = requests.get(file_path + x, stream=True)
        r.raw.decode_content = True

        """ Used shutil to download the image """
        with open(x, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print(BColors.OKGREEN + x + " - Saved successfully!")
    print(BColors.OKGREEN +
          "-----------------------------------------------------------------------" + BColors.ENDC)


def main():
    try:

        # For testing purpose
        # file_path = "https://starzoneaz.ragalahari.com/july2018/starzone/trisha-mohini-pre-release/"
        # file_name = "trisha-mohini-pre-release%d.jpg"
        # folder_name = "Trisha"
        # cycle = 2
        # idLists = []

        # Displaying welcome banner
        welcomeBanner()

        # Getting file_path info from user
        file_path = input(BColors.BOLD + "Enter your URL Path of the images: ")

        # Getting file_name info from user
        file_name = input(BColors.BOLD + "Enter your file_name: ")

        # Getting folder info from user for structured storing
        folder_name = input(BColors.BOLD + "Folder name: ").title()

        # Getting cycle loop info from user
        cycle = input(
            BColors.BOLD + "How much image you want me to download? (Default: 100): ")

        try:
            if cycle == '':
                cycle = 100
            else:
                cycle = int(cycle) + 1
        except ValueError:
            print(BColors.FAIL + "This is not a valid number. Please enter correct integer")

        # Creating folder, if doesn't exist
        createFolder(folder_name)

        # Checking automatically, does the file exist or not
        checkFileExist(file_path, file_name, cycle)

        # Finally downloading the file and saving to the folder, you have specified earlier
        downloadImg(file_path, folder_name)

    except KeyboardInterrupt:
        print("\n " + BColors.WARNING + "Shutdown requested...exiting")
    except (Exception,):
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
