import numpy as np


def emailFeatures(word_indices):
    n = 1899
    x = np.zeros((n, 1))

    for word_indice in word_indices:
        x[word_indice] = 1

    return x.T


if __name__ == '__main__':
    f = open('emailSample1.txt')
    email_contents = f.read()
    from processEmail import processEmail
    word_indices = processEmail(email_contents)
    print word_indices
    print len(word_indices)
    features = emailFeatures(word_indices)
    print len(features)

    print np.sum(features)
