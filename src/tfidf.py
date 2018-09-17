import pickle
import math
import language


def normalize(text):
    return text.lower().replace(",", " ").replace(".", " ").replace(";", " ").replace("!", " ").replace(":", " ").replace("\"", " ").replace("»", " ").replace("«"," ")


def tf_idf(list_doc, arr, nb_doc):
    max_tf = 0
    res = []
    for t in arr:
        for doc in list_doc:
            doc = normalize(doc)
            if t not in doc:
                continue
            trigram_count = doc.count(t)
            total_count = len(doc.split())
            tf = trigram_count / total_count
            idf = math.log10(nb_doc/len(list_doc))
            tfidf = tf * idf
            if tfidf > max_tf:
                res = []
                max_tf = tfidf
            if tfidf == max_tf:
                    res.append(t)
    return list(set(res))


def construct_list_doc(file, word, lang):
    list_doc = []
    count = 0
    f = open("word_trigram_full.pickle", "rb")
    arr = pickle.load(f)
    for line in file:
        count += 1
        tab = line.replace("\n", "").split("\t")
        if tab[1] == lang and word in tab[2]:
            list_doc.append(tab[2])
    trigram_list = []
    for l in arr[lang]:
        for trigram in l:
            if " " + word + " " in ' '.join(trigram) or trigram[0] == word:
                trigram_list.append(' '.join(trigram))
    trigram_list = list(set(trigram_list))
    f.close()
    return list_doc, trigram_list, count


def auto_complete_word(sentence):
    lang = language.found_language(sentence)
    word = sentence.split()[-1]
    file = open("sentences.csv", "r", encoding="utf-8")
    list_doc, trigram_list, count = construct_list_doc(file, word, lang)
    file.close()
    list = tf_idf(list_doc, trigram_list, count)
    return list