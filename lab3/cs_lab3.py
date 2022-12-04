import re


# task 1, 60 points

#isu = 367165
#task_option = 111
#smile = ";<)"

def quantity_smiles_in_s(s):
    return len(re.findall(r";<\)", s))


def test_count_smiles():
    test_strs = [
        ("hello world ;<)",          1),
        (";<)",                      1),
        (";<)" * 3,                  3),
        (";<) " * 3,                 3),
        (";<] not my type of smile", 0),
    ]

    print("task 1:")
    for s, k in test_strs:
        assert quantity_smiles_in_s(s) == k


# additional task 1, 18 points
str1 = "Довольно распространённая ошибка ошибка – это повтор слова. Вот в предыдущем предложении такая допущена. Необходимо исправить каждый такой повтор. Повтор это – слово, один или несколько пробельных символов, и снова то же слово."


def word_repeat(s):
    return re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', s)


def test_word_repeat():
    test_strs = [
        ("hello world world",                  "hello world"),
        ("hello wor world",                    "hello wor world"),
        ("hello hello hello world",            "hello world"),
        ("hellohelloworldworld",               "hellohelloworldworld"),
        ("hello hello helloworld world world", "hello helloworld world"),
    ]

    print("additioanal task 1:")
    for s, k in test_strs:
        assert word_repeat(s) == k


# additional task 2, 22 points
str2 = "Классное слово – обороноспособность, которое должно идти после слов: трава и молоко."


def one_vowels_words(s):
    words = re.findall(r"\b\w+\b", s)
    res = []

    for i in range(len(words)):
        x = re.findall(r"[АаУуОоЫыЭэЯяЮюЁёИиЕе]", words[i].lower())
        if (len(set(x)) == 1):
            res += [words[i]]
    res.sort(key=len)
    return res


def test_one_vowels_words():
    test_strs = [
        ("Классное слово – обороноспособность, которое должно идти после слов: трава и молоко.", [
         "и", "идти", "слов", "слово", "трава", "должно", "молоко", "обороноспособность"]),
        ("на завтрак я кушал кашу", ["я", "на", "завтрак"]),
        ("на обед я ел суп-пюре", ["я", "на", "ел", "суп"]),
        ("на ужин я ел барана и макароны", ['я', 'и', 'на', 'ел', 'барана']),
        ("есть ли повторяющиеся гласные буквы хотя бы в одном слове этого предложения?", [
         'ли', 'бы', 'есть', 'одном']),
    ]

    print("additioanal task 2:")
    for s, k in test_strs:
        assert one_vowels_words(s) == k


test_count_smiles()
test_word_repeat()
test_one_vowels_words()
