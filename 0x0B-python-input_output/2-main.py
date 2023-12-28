#!/usr/bin/python3
"""2-main"""

append_write = __import__('2-append_write').append_write

nb_characters = append_write("file_append.txt", "This school is so cool!\n")
print(nb_characters)
