from ..lib import tetsing, normalize, tokenize, top_n, count_freq


def stats(text: str):

    t = text

    tok = tokenize(normalize(t))
    fr = count_freq(tok)
    tp = top_n(fr)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    for a, b in tp:
        print(f"{a}: {b}")



# TEST CASES

