import time
def sqcrypt(string):
    j = 0
    encoded = []
    length = len(string)
    for i in range(length):
        if not j % 8:
            for k in range(8):
                if i+k < length:
                    try:
                        encoded[k] = encoded[k]+string[i+k]
                    except IndexError:
                        encoded.insert(k,string[i+k])
                else:
                    pass
        j+=1
    print('Encrypted fragments:',encoded)
    return encoded

def sqdecrypt(encoded):
    for k in range(len(encoded[0])):
        for i,j in enumerate(encoded):
            try:
                if j[k] is '%':
                    print(" ",end="")
                else:
                    print(j[k],end="")
            except IndexError:
                print("",end="")


def main():
    string = input("Enter message")
    start = time.time()
    string = list(string.replace(' ', '%'))
    encode = sqcrypt(string)
    sqdecrypt(encode)

if __name__ == '__main__':
    main()
