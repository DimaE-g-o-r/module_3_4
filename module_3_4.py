def single_root_words(*other_words, root_words = 'вор'):
    same_words = []
    for i in other_words:
        if root_words.lower() in i.lower():
            same_words.append(i)

    return print(same_words)

single_root_words( 'воротник', 'своровать', 'воровство', 'круговорот', 'воришка')
single_root_words('вокруг', 'кружева', 'Михаил Круг', 'круговорот', 'крутой', root_words = 'круг')