if __name__ == '__main__':
    N = int(input())
    
    list = []
    
    for i in range(0, N):
        _input = input()
        
        if(_input[0:6] == "insert"):
            a = int(_input[7:9])
            b = int(_input[9:11])
            list.insert(a, b)
        elif(_input[0:6] == "remove"):
            c = int(_input[7:])
            list.remove(c)
        elif(_input[0:6] == "print"):
            print(list)
        elif(_input[0:6] == "append"):
            list.append(int(_input[7:]))
        elif(_input[0:4] == "sort"):
            list.sort()
        elif(_input[0:3] == "pop"):
            list.pop()
        elif(_input[0:7] == "reverse"):
            list.reverse()