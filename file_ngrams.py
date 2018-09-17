import os
import math
import utils
import tfidf


def fetch(path) :
    result = []
    filenames = []
    for root, subdirs, files in os.walk(path):
        for file in files:
            url = os.path.join(root, file)
            file = open(url)
            text = file.read()
            result.append(text)
            filenames.append(os.path.basename(file.name))
            file.close()
    return result, filenames

def full_tf_idf(list_doc, trigram_list):
    res = {}
    for word in trigram_list:
        result = []
        number_doc = []
        idf = 0
        for doc in list_doc:
            doc = tfidf.normalize(doc)
            total_size = len(doc.split())
            number_word = doc.count(word)
            if number_word == 0:
                number_doc.append(0)
            else:
                number_doc.append(1)
            result.append(number_word/total_size)
        if number_doc.count(1) != 0:
            idf = math.log10(len(number_doc)/number_doc.count(1))
        res[word] = [frequence*idf for frequence in result]
    return res


def select_ngrams(path, filename):
    list_doc, filenames = fetch(path)
    output = open(filename, "w")
    output.write("Trigram : [ " + ','.join(filenames) + "]\n")
    ngrams = []
    for doc in list_doc:
        ngrams.append(utils.word_trigram(tfidf.normalize(doc)))
    list_trigram = []
    for list in ngrams:
        for trigram in list[0]:
            list_trigram.append(' '.join(trigram))
    res = full_tf_idf(list_doc, list_trigram)
    for key in res.keys():
        output.write(key + " : [ ")
        for i in range(0, len(res[key]) - 1):
            output.write(str(res[key][i]))
            output.write(", ")
        output.write(str(res[key][-1]))
        output.write(" ]\n")
    output.close()

#path = os.path.join(os.getcwd(), "SEO")
#print(path)
#select_ngrams(path, "output.txt")
