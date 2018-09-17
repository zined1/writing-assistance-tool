import pickle
import language

def trigram(text, min_n, max_n):
    res = []
    for j in range(min_n, max_n + 1):
        l = []
        for i in range(len(text) - j + 1):
            l.append(text[i:i+j])
        res.append(l)
    return res


def distance_dl(s1, s2):
    d = {}
    len1 = len(s1)
    len2 = len(s2)
    for i in range(-1,len1+1):
        d[(i,-1)] = i+1
    for j in range(-1,len2+1):
        d[(-1,j)] = j+1
    for i in range(len1):
        for j in range(len2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(d[(i-1,j)] + 1, d[(i,j-1)] + 1, d[(i - 1,j - 1)] + cost)
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i - 2, j - 2] + cost)
    return d[len1-1,len2-1]

def found_all_ngram(map_word, word):
    ngram = trigram(word, 2, len(word))
    i = 0
    res = []
    for lists in ngram:
        for list in lists:
            #print('fart' in map_word[len(list)])
            if i < 4 and list in map_word[len(list)]:
                res += map_word[len(list)][list]
            i += 1
    return res

def auto_complete_char(sentence):
    lang = language.found_language(sentence)
    #print(lang)
    # create_pickle_occurences(language)
    full_trigram = open("ngram_map_full.pickle", "rb")  # Si t'as pas le pickle active cette ligne
    map_word = pickle.load(full_trigram)[lang]
    occurences = get_occurence_by_language(lang)
    word = sentence.split()[-1]
    dico = {}
    near_words = found_all_ngram(map_word, word)
    for ngram in near_words:
        distance = distance_dl(ngram, word)
        if distance == 0:
            return ngram
        dico[ngram] = distance
    dico = sorted(dico.items(), key=lambda x: x[1])
    min_dist = dico[0][1]
    word_to_choose = dico[0][0]
    occ_to_choose = 0
    i = 0
    while i < len(dico) and dico[i][1] == min_dist:
        if dico[i][0] in occurences and occurences[dico[i][0]] > occ_to_choose:
            occ_to_choose = occurences[dico[i][0]]
            word_to_choose = dico[i][0]
        i += 1
    return word_to_choose

def create_pickle_occurences(language):
    counts = {}
    f = open("sentences.csv", "r", encoding="utf-8")
    for line in f:
        tab = line.replace("\n", "").split("\t")
        if tab[1] in language:
            words = tab[2].split()
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
    file = open("occurences_"+language+".pickle", "wb")
    pickle.dump(counts, file, protocol=pickle.HIGHEST_PROTOCOL)

def get_occurence_by_language(language):
    return pickle.load(open("occurences_"+language+".pickle", "rb"))