'''
P: given a string, capitalize every second character in every third word
E: 'a big pig' -> 'a big pIg'
D: list of word
A: iterate every third word using helper function, join into answer
C: below
'''

def alternating_capitalization(word):
    result = ''
    for i, char in enumerate(word):
        if i % 2 == 1:
            result += char.upper()
        else:
            result += char
    return result

def to_weird_case(string):
    word_list = string.split()
    for i in range(2, len(word_list), 3):
        word_list[i] = alternating_capitalization(word_list[i])

    return ' '.join(word_list)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)