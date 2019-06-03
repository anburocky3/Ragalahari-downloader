#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import urllib.request
import sys
import traceback

import requests
import subprocess as sp

idLists = []

# author: Anbuselvan Rocky
# Facebook: fb.me/anburocky3
# Github: github.com/anburocky3

class bcolors:
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


def checkFileExist(filePath, fileName, cycle):
    i = 1
    print(bcolors.WARNING + "Searching files. . . . .")
    while i < cycle:
        print(bcolors.OKGREEN +
              "-----------------------------------------------------------------------")
        if(exists(filePath, fileName % (i))):
            ids = fileName % (i)
            idLists.append(ids)
            print(bcolors.OKBLUE + " INFO: " + bcolors.OKGREEN + "File exists: " + fileName % (i))
            i += 1
        else:
            print(
                bcolors.FAIL + "-----------------------------------------------------------------------")
            print(bcolors.FAIL + " INFO: " + bcolors.FAIL + "File not exist: " + fileName % (i))
            print(
                bcolors.FAIL + "-----------------------------------------------------------------------")
            print(bcolors.WARNING + " Skipping. . .")
            break


def createFolder(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)


def welcomeBanner():
    tmp = sp.call('cls', shell=True)
    tmp = sp.call('clear', shell=True)

    print(bcolors.OKGREEN + """
--------------------------------------------------------------------------------
|         _____                   _       _                _                   |
|        |  __ \                 | |     | |              (_)                  |
|        | |__) |__ _  __ _  __ _| | __ _| |__   __ _ _ __ _                   |
|        |  _  // _` |/ _` |/ _` | |/ _` | '_ \ / _` | '__| |                  |
|        | | \ \ (_| | (_| | (_| | | (_| | | | | (_| | |  | |   V1.O           |
|        |_|  \_\__,_|\__, |\__,_|_|\__,_|_| |_|\__,_|_|  |_|                  |
|                      __/ |                                                   |
|                     |___/                                                    |""" + bcolors.OKGREEN + """
|                                                                              |
|  Description: This tool will help you to download automatic High Quality(HQ) |
|               images from ragalahari site.                                   |
--------------------------------------------------------------------------------""")

    print("|=============================================================================|")
    print(bcolors.OKBLUE + "|          Programmer: Anbuselvan Rocky   | fb.me/anburocky3                  |" + bcolors.ENDC)
    print("|=============================================================================| \n")


def downloadImg(filePath, folderName):
    print(bcolors.OKGREEN +
          "-----------------------------------------------------------------------")
    for x in idLists:
        urllib.request.urlretrieve(filePath + x, folderName + "/" + x)
        print(bcolors.OKGREEN + x + " - Saved successfully!")
    print(bcolors.OKGREEN +
          "-----------------------------------------------------------------------")




def main():
    try:

        # For testing purpose
            # filePath = "https://starzoneaz.ragalahari.com/july2018/starzone/trisha-mohini-pre-release/"
            # fileName = "trisha-mohini-pre-release%d.jpg"
            # folderName = "Trisha"
            # cycle = 2
            # idLists = []

        # Displaying welcome banner
        welcomeBanner()

        # Getting filepath info from user
        filePath = input(bcolors.BOLD + "Enter your URL Path of the images: ")

        # Getting filename info from user
        fileName = input(bcolors.BOLD + "Enter your filename: ")
        
        # Getting folder info from user for structured storings
        folderName = input(bcolors.BOLD + "Folder name: ").title()

        # Getting cycle loop info from user
        cycle = input(
            bcolors.BOLD + "How much image you want me to download? (Default: 100): ")

        try:
            if cycle == '':
                cycle = 100
            else:
                cycle = int(cycle)+1
        except ValueError:
            print(bcolors.FAIL +
                  "This is not a valid number. Please enter correct integer")

        # Creating folder, if doesn't exist
        createFolder(folderName)

        # Checking automatically, does the file exist or not
        checkFileExist(filePath, fileName, cycle)

        # Finally downloading the file and saving to the folder, you have specified earlier
        downloadImg(filePath, folderName)

    except KeyboardInterrupt:
        print("\n " + bcolors.WARNING + "Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
