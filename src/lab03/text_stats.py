from ..lib import testing
from ..lib.text import normalize, tokenize, top_n, count_freq

def stats(text: str):

    t = text

    tok = tokenize(normalize(t))
    fr = count_freq(tok)
    tp = top_n(fr)

    print(f"Всего слов: {len(tok)}")
    print(f"Уникальных слов: {len(fr)}")
    print("Топ-5:")

    for a, b in tp:
        print(f"{a}: {b}")



# TEST CASES
test_normalize=[
    "ПрИвЕт\nМИр\t",
    "ёжик, Ёлка",
    "Hello\r\nWorld",
    "  двойные   пробелы  ",
]

test_tokenize=[
    "привет мир",
    "hello,world!!!",
    "по-настоящему круто" ,
    "2025 год" ,
    "emoji 😀 не слово",

]

test_count_freq=[
    ["a","b","a","c","b","a"],
    ["bb","aa","bb","aa","cc"]
]

test_top_n=[
    ({"a":3, "b":2, "c":1},2),
    (["bb","aa","bb","aa","cc"],2)
]

## NORMALIZE
print()
print("NORMALIZE")
testing(normalize,test_normalize)
print()


## TOKENIZE
print()
print("TOKENIZE")
testing(tokenize,test_tokenize)
print()

## COUNT_FREQ
print()
print("COUNT_FREQ")
testing(count_freq,test_count_freq)
print()

## TOP_N
print()
print("TOP_N")
print("({'a': 3, 'b': 2, 'c': 1},2)","->",top_n({'a': 3, 'b': 2, 'c': 1},2))
print("({'bb': 2, 'aa': 2, 'cc': 1}, 2)","->",top_n({'bb': 2, 'aa': 2, 'cc': 1},2))
print()

## stats
print()
print("STATS")
print()
print("Привет, мир! Привет!!!")
print()
stats("Привет, мир! Привет!!!")
print()