def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
     
    if not isinstance(text, str):
        raise TypeError("Введена не строка")

    if not text.strip():
        raise ValueError("Строка пуста")
   
   
    t = text

    if yo2e:
        t = t.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        t = t.casefold()

    t = ' '.join(t.split())
    return t




def tokenize(text: str) -> list[str]:
    
    if not isinstance(text, str):
        raise TypeError("Введена не строка")
    
    
    t = text
    t = normalize(t)
    an = ""
    count = 0

    for i in t:
        if i.isalnum() or (
            (i == "-" or i == '_')  # проверки для тире, подч.
            and count > 0 and count + 1 < len(t)
            and t[count - 1].isalnum() and t[count + 1].isalnum()
        ): result += i
        else:result += " "

        count += 1

    if not result.split():
        raise ValueError("В тексте нет слов")

    return result.split()


def count_freq(tokens: list[str]) -> dict[str, int]:
    
    if not isinstance(tokens, list):
        raise TypeError("Введен не список слов")

    if not tokens:
        raise ValueError("Список пуст")
    
    
    t = tokens
    result = {}
    for i in t:
        result[i] = t.count(i)
    return result


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    
    if not isinstance(freq, dict):
        raise TypeError("Введен не словарь")

    if not freq:
        raise ValueError("Словарь пуст")

    if n <= 0:
        raise ValueError("Количество слов не может быть 0")
    
    
    
    result = list(freq.items()) #словарь -> кортеж типа ("слово": кол-во раз)
    result.sort(key=lambda x: (-x[1], x[0])) # сортровка по кол-ву слов
    
    
    if not result:
        raise ValueError("error")
    
    return result[:n] 
