def swap_case(s):
    n = ""
    for i in range(len(s)):
        if s[i].isupper():
            n = n + s[i].lower()
        elif s[i].islower():
            n = n + s[i].upper()
        else:
            n = n + s[i]
    return(n)

