#!/usr/bin/python3
""" text_identation module """


def text_indentation(text):
    """
    text_indentation - change ".:?" for two new line

    Args:
        text: string to process. Must be a string

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = text
    new_text = " ".join(new_text.split())
    new_text = new_text.replace('.', '.\n\n')
    new_text = new_text.replace(':', ':\n\n')
    new_text = new_text.replace('?', '?\n\n')
    new_text = new_text.replace('\n\n ', '\n\n')
    print("{}".format(new_text), end="")
