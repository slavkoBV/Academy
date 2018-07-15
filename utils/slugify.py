def slugify(sequence):
    translit_table = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y',
        'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
        'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ю': 'Yu', 'Я': 'Ya',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y',
        'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's',
        'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'iu', 'я': 'ia',
        'ь': '', '\'': ''
    }
    replace_combinations = {'Zh': 'Zgh', 'zh': 'zgh'}
    forbidden_symbols = ('!', '?', '+', '*', '/', '=', '%', '^', '&', '$', '@', '(', ')', '[', ']', '{', '}', ',', '.', '"')

    def translit(w):
        result = ''
        for i in w:
            if i in translit_table.keys():
                result += translit_table[i]
            elif i in forbidden_symbols:
                result += ''
            else:
                result += i
        if ('Зг' in w) or ('зг' in w):
            for i in replace_combinations.keys():
                if i in result:
                    result = result.replace(i, replace_combinations[i])
        return result

    words = sequence.strip().split(' ')
    return '-'.join(translit(word) for word in words).lower()
