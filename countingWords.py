import string

def validateString(char):
    for i in char:
        if i in (string.punctuation+' '+string.digits):
            return False
    return True

def findNumberOfElements():
    n = input('Number of words: ')
    words = {}
    
    try:
        n = int(n)
    except:
        raise Exception('Please enter integer number ')
    else:
        for j in range(n):
            word = input('word number %d: ' %(j+1))
            if validateString(word):
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
            else:
                raise Exception('Please Type only one word')
    
    print(len(words))
    print(*words.values())
    
    
    
if __name__ == '__main__':
    
    findNumberOfElements()
