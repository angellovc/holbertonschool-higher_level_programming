#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return(len(sentence), None)
    return (len(sentence), sentence[0])
