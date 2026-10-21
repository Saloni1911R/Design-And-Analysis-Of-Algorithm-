def str_match_naiv(text, key):
    n = len(text)
    m = len(key)
    res = []
    
    for i in range(n - m + 1):
        match = True
        
        for j in range(m):
            if text[i + j] != key[j]:
                match = False
                break
        
        if match:
            return True
    return False


print(str_match_naiv("hello world", "world"))