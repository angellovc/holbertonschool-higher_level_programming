#!/usr/bin/python3
""" print the ascii alphabet without e and q """
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    print("{}".format(chr(i)), end='')  # print ascii numbers
