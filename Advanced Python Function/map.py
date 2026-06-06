#Map Function

def myfunction(a , b):
    return a + ':' + b

result = map(myfunction, ('dog', 'cat', 'cherry'), ('barks', 'meows', 'blossom'))

print(list(result))