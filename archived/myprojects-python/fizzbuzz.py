def main(yourrange,dictionary):
    keys = dictionary.keys()
    keys.sort()
    keys.reverse()
    for num in yourrange :
        for divisor in keys:
            if num%divisor ==  0:
                print dictionary[divisor]
                break
        else:
            print num



main(range(1,101),{3:'foo',5:'bar',15:'foobar'})

