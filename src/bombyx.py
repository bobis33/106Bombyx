#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## B-MAT-200-BDX-2-1-106bombyx-elliot.masina
## File description:
## 106bombyx
##

from sys import argv
from src.print_help import print_help
from src.error import error_case


def second_case(n, i0, i1):

    i   = int (1)
    j   = int (1)

    while j <= 4:
        while i < i0:
            n   = j * n * (1000 - n) / 1000
            i   += 1

        while i <= i1:
            print("%.2f %.2f" % (j, n))
            n   = j * n * (1000 - n) / 1000
            i   += 1

        n   = int (argv[1])
        i   = 1
        j   += 0.01


def first_case(n, k):

    i   = int (1)

    while (i <= 100):
        print("%i %.2f" % (i, n))
        n   = k * n * (1000 - n) / 1000
        i   += 1


def bombyx():

    len_argv    = int (len(argv))

    if (len_argv == 2 and argv[1] == "-h"):
        print_help()

    error_case()

    n   = int (argv[1])

    if (len_argv == 3):
        k   = float (argv[2])
        first_case(n, k)

    if (len_argv == 4):
        i0  = int (argv[2])
        i1  = int (argv[3])
        second_case(n, i0, i1)
