#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        return tuple([len(sentence), sentence[:1]])
    else:
        return tuple([0, None])
