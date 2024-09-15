def single_root_words(root_word, *other_words):
    result=[]
    for i in other_words:
        if root_word.lower() in i.lower():
            result.append(i)
        elif i.lower() in root_word.lower():
            result.append(i)
    return result


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)