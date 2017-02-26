# import numpy as np
import re


def getVocabList():
    fid = open('vocab.txt')

    vocabList = []
    pattern = re.compile(r'[A-Za-z]+')

    for line in fid:
        # print line[0]
        match = pattern.search(line)
        word = match.group()
        vocabList.append(word)
    return vocabList
    # print len(vocabList)


if __name__ == '__main__':
    print getVocabList()
