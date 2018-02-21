

def brainfuck(src, aris, dex, data, idx):
    
    if len(src) == 0: return
    if aris < 0: aris = 0
    if aris >= len(src): aris = len(src) - 1
    if dex < 0: dex = 0
    if dex >= len(src): dex = len(src) - 1
    
    arr = [0] * 30000
    ptr = 0
    i = aris
    while i <= dex:
        s = src[i]
        if s == '>':
            ptr += 1
            
            if ptr >= len(arr):
                ptr = 0
        elif s == '<':
            ptr -= 1
            
            if ptr < 0:
                ptr = len(arr) - 1
        elif s == '+':
            arr[ptr] += 1
        elif s == '-':
            arr[ptr] -= 1
        elif s == '.':
            print(chr(arr[ptr]), end=="")
        elif s == ',':
            if idx >= 0 and idx < len(data):
                arr[ptr] = ord(data[idx])
                idx += 1
            else:
                arr[ptr] = 0
        elif s =='[':
            if arr[ptr] == 0:
                loop = 1
                while loop > 0:
                    i += 1
                    c = src[i]
                    if c == '[':
                        loop += 1
                    elif c == ']':
                        loop -= 1
        elif s == ']':
            loop = 1
            while loop > 0:
                i -= 1
                c = src[i]
                if c == '[':
                    loop -= 1
                elif c == ']':
                    loop += 1
            i -= 1
        i += 1

if __name__ == "__main__":
    src = raw_input()
    brainfuck(src, 0, len(src) - 1, "sdfsdf", 0)
