def adder(s,e):
    try:
        if e==s:
            return s
        elif e<s:
            return "Error"
        else:
            print s,e
            return e + adder(s,e-1)
    except RuntimeError as r:
        print r
        return 0

print adder(1,1)
