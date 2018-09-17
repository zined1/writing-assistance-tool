#!/usr/bin/python3.6


def ngram(str, n):
    l = []
    for i in range(len(str) - (n - 1)):
        l.append(str[i: i + n])
    return l


def found_language(s):
    count = {"eng": 0, "fra": 0, "spa": 0, "deu": 0}
    best_trigram = {"eng": ["the", "and", "ion", "tio", "ati", "igh", "ght", "rig", "ent", "ver", "one", "all", "eve", "ery", "his"],
                    "fra": ["ion", "tio", "ent", "oit", "ati", "roi", "dro", "men", "tou", "con", "res", "que", "les", "des", "eme"],
                    "spa": ["ion", "cio", "rec", "ere", "der", "ien", "cho", "ent", "ech", "aci", "ona", "nte", "con", "ene", "tod"],
                    "deu": ["der", "und", "ein", "ung", "cht", "ich", "sch", "che", "ech", "die", "rec", "ine", "eit", "gen", "ver"]}

    best_bigram = {"eng": ["th", "on", "an", "he", "er", "nd", "in", "ti", "al", "re", "io", "en", "ri", "of", "or",  "at", "it", "to", "ed", "nt"],
                    "fra": ["on", "es", "de", "te", "nt", "re", "en", "le", "it", "er", "et", "ti", "ou", "io", "la", "oi", "ne", "me", "ro", "ns"],
                    "spa": ["de", "en", "er", "on", "ci", "es", "re", "os" "io", "la", "ra", "na", "ec", "al", "ad", "da", "to", "nt", "ie", "el"],
                   "deu": ["en", "er", "ch", "ei", "un", "de", "nd", "ge", "re", "in", "ie", "te", "ng", "he", "ne", "ht", "ic", "be", "it", "sc"]}

    all_trigram = [best_bigram, best_trigram]
    for i in range(2, 4):
        l = ngram(s.lower(), i)
        for key, value in best_trigram.items():
            for v in l:
                if v in all_trigram[i - 2][key]:
                        count[key] += 1
    return max(count, key=count.get)

def acronym_to_language(s):
    if s == "eng":
        return "Anglais"
    elif s == "fra":
        return "Francais"
    elif s == "spa":
        return "Espagnol"
    elif s == "deu":
        return "Allemand"
    else:
        return "Langage non reconnu"