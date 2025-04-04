# Finite State Machine

# 编写一个函数 isNumber(s: str) -> bool，判断给定字符串 s 是否是有效的数字表示。

def isNumber(s: str) -> bool:
    def char_type(c):
        if c in '0123456789':
            return 'digit'
        elif c in '+-':
            return 'sign'
        elif c == '.':
            return 'dot'
        elif c in 'eE':
            return 'e'
        elif c == ' ':
            return 'blank'
        else:
            return 'other'

    # 状态转移图
    states = {
        0: {'blank': 0, 'sign': 1, 'digit': 2, 'dot': 3},
        1: {'digit': 2, 'dot': 3},
        2: {'digit': 2, 'dot': 4, 'e': 5, 'blank': 8},
        3: {'digit': 4},
        4: {'digit': 4, 'e': 5, 'blank': 8},
        5: {'sign': 6, 'digit': 7},
        6: {'digit': 7},
        7: {'digit': 7, 'blank': 8},
        8: {'blank': 8}
    }

    state = 0
    for c in s:
        typ = char_type(c)
        if typ not in states[state]:
            return False
        state = states[state][typ]

    return state in [2, 4, 7, 8]


# isNumber("0") → True
# isNumber(" 0.1 ") → True
# isNumber("abc") → False
# isNumber("1 a") → False
# isNumber("2e10") → True
# isNumber(" -90e3 ") → True
# isNumber(" 1e") → False