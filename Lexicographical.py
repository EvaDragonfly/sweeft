def bigger_is_greater(w):
    
    if sorted(w, reverse = True) == list(w):
        return 'no answer'

    w = list(w[::-1])
    
    i = 0
    while w[i]<w[i+1] and i<len(w)-2:
        i+=1
        
    num = w[i]
    for j in w[:i]:
        if j < num and j > w[i+1]:
            num = j
            

    ind = w.index(num)
    w[ind], w[i+1] = w[i+1], w[ind]

    w = sorted(w[:i+1], reverse = True)+w[i+1:]
    w = ''.join(w[::-1])
    
    return w


if __name__ == '__main__':
    print(bigger_is_greater('lmno'))
    print(bigger_is_greater('dcba'))
    print(bigger_is_greater('dcbb'))
    print(bigger_is_greater('abdc'))
    print(bigger_is_greater('abcd'))
    print(bigger_is_greater('fedcbabcd'))
