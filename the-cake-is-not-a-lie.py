
def solution(str):
    """
    share a cake with all Minions, try your best to split it with equal colors,
    each character represent a kind of color [a-z].
    """

    repeated_len = 1
    total_len = len(str)
    
    while repeated_len < total_len:
        if total_len % repeated_len == 0 and verify(str, repeated_len):
            return int(total_len / repeated_len)
        repeated_len = repeated_len + 1
    
    return 1


def verify(str, repeated_len):
    s = str[0: repeated_len]
    
    idx = repeated_len
    
    while idx < len(str):
        if s != str[idx: idx + repeated_len]:
            return False
        idx = idx + repeated_len
    
    return True
      

a = solution("abccbaabccba") # 2
print(a)
a = solution("abcabcabcabc") # 4
print(a)