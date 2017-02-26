# coding: utf=8
from getVocabList import getVocabList
import re


def processEmail(email_contents):
    vocabList = getVocabList()
    word_indices = []

    # 处理邮件内容
    email_contents = email_contents.lower()
    email_contents, _ = re.subn(r'<[^<>]+>', ' ', email_contents)
    email_contents, _ = re.subn(r'[0-9]+', 'number', email_contents)
    email_contents, _ = re.subn(
        r'(http|https)://[^\s]*', 'httpaddr', email_contents)
    email_contents, _ = re.subn(r'[^\s]+@[^\s]+', 'emailaddr', email_contents)
    email_contents, _ = re.subn(r'[$]+', 'dollar', email_contents)
    # print email_contents
    # 还需要提取单词主干，把双数，ing等去掉， 使用nltk模块即可
    from nltk.stem import PorterStemmer

    if email_contents != '':
        re_words = re.findall(r'[A-Za-z]+', email_contents)
        # print re_words
        for word in re_words:
            word = PorterStemmer().stem(word)
            # word, _ = re.subn(r'[^a-zA-Z0-9]', '', word)
            # print word
            for i in range(len(vocabList)):
                if vocabList[i] == word:
                    word_indices.append(i)
        # print len(word_indices)
        # print word_indices
    return word_indices


if __name__ == '__main__':
    f = open('emailSample1.txt')
    email_contents = f.read()
    print processEmail(email_contents)
