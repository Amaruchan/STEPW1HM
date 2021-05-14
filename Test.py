def readfile(filename):
  with open(filename) as f:
    l_strip = [s.strip() for s in f.readlines()]
    return l_strip
    f = open(filename, 'r')
    x = f.readlines()
    f.close()
    return x
    
dictionary = readfile("words.txt")
print("new_dictionary start")

new_dictionary=[]
for word in dictionary:
    new_dictionary.append((''.join(sorted(word)), word))
new_dictionary = sorted(new_dictionary, key=lambda x:x[0])

print(new_dictionary)
