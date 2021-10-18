word1 = input('Addjon meg egy szavat: ')
word2 = input('Addjon meg egy másik szavat: ')

word1_length = len(word1)
word2_length = len(word2)

if (word1_length > word2_length):
    print('A hosszabb szó: ' +word1)

elif(word1_length < word2_length):
    print('A hosszabb szó: ' +word2)

else:
    print('A két szó egyenlő hosszú.')