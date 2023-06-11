#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## B-MAT-200-BDX-2-1-106bombyx-elliot.masina
## File description:
## error
##

from sys import argv


def error_case():

    len_argv = int (len(argv))

    if (len_argv != 3 and len_argv != 4):
        exit(84)

    try:
        n   = int (argv[1])
    except ValueError : exit(84)

    if (n < 0):
        exit(84)

    if (len_argv == 3):
        try:
            k   = float (argv[2])
        except ValueError : exit(84)

        if (k < 1 or k > 4):
            exit(84)

    if (len_argv == 4):
        try:
            k   = int (argv[2])
            i   = int (argv[3])
        except ValueError : exit(84)

        if (i <= 0 or k > i):
            exit(84)
