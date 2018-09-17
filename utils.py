def trigram(text, min_n, max_n):
    res = []
    for j in range(min_n, max_n + 1):
        l = []
        for i in range(len(text) - j + 1):
            l.append(text[i:i+j])
        res.append(l)
    return res


def word_trigram(text):
    splitted_text = splitter(text)
    print(splitted_text)
    return trigram(splitted_text, 3, 3)


def splitter(text) :
    replaced_text = text.replace(",", " ").replace(".", " ").replace(";", " ")
    splitted_text = replaced_text.split(" ")
    return list(filter(None, splitted_text))


def trigram_map(text, min_n, max_n):
    split_text = splitter(text)
    res_n = {}
    for n in range(min_n, max_n + 1):
        res = {}
        for i in range(len(split_text)):
            for j in range(len(split_text[i]) - n + 1):
                if split_text[i][j:j+n] not in res.keys():
                    res[split_text[i][j:j+n]] = []
                if (split_text[i]) not in res[split_text[i][j:j+n]]:
                    res[split_text[i][j:j+n]].append(split_text[i])
        res_n[n] = res
    return res_n
