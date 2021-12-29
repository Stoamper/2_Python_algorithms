'''
2.	Закодировать любую строку по алгоритму Хаффмана.

Алгоритм Хаффмана предполагает, что наиболее часто встречающийся символ получает очень маленький код,
а наиболее редко встречающийся - очень длинный код
'''
from collections import Counter

# связной список (используем начальную структуру класса Node)
class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(head, codes=dict(), code=''):
    if head is None:
        return
    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    get_code(head.left, codes, code + '0')
    get_code(head.right, codes, code + '1')

    return codes

# Получение дерева, по которому будем проходиться при кодировании
def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)
        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]

        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]

# Кодирование элементов строки
def coding(string, codes):
    result = ''

    for el in string:
        result += codes[el]
        result += ' '
    return result

# Декодирование закодированной строки
def decoding(string, codes):
    result = ''
    i = 0
    string = ''.join(string.split())
    while i < len(string):

        for j in codes:
            if string[i:].find(codes[j]) == 0:
                result += j
                i += len(codes[j])
    return result

string = input('Введите строку, которую необходимо закодировать по алгоритму Хаффмана: ')

tree = get_tree(string)
codes = get_code(tree)

print('Коды символов, полученные по алгоритму Хаффмана, имеют вид: ')
print(f'{codes}\n')

codings_str = coding(string, codes)

print(f'Закодированная строка имеет вид: {codings_str}\n')

decodings_str = decoding(codings_str, codes)

print(f'Изначальная строка имеет вид: {decodings_str}\n')

