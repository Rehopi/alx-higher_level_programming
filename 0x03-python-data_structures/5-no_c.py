#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for ce in my_string:
        if ce is not "c" and ce is not "C":
            str = str + ce
    return str
