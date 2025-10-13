'''
    s = aaba
    k = aa
    verifica s[i], se for igual a k[i] (start = i)
    verifica o proximo s[i + 1] == k[i + 1] até o fim de s ou k

'''

def findIndex(s, k):
    tuples = [] 

    for i in range(len(s)):
        for j in range(len(k)):
            if s[i] == k[j]:
                start = i
            else:
                continue
        end = i
        tuples.append([start, end])
    
    
    return tuples

s = input()
k = input()

result = findIndex(s, k)
print(result)