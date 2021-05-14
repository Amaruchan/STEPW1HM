def count_alph(random_word):
  sorted_random_word = sorted(random_word)
  lst = []
  atr = sorted_random_word[0]
  count = 0
  for c in sorted_random_word:
    if atr != c:
      lst.append((atr, count))
      atr = c
      count = 1
    else: count += 1
  lst.append((atr, count))
  return lst

def count_to_words_rec(alph_count_tuple):
  lst = []
  chr = alph_count_tuple[0][0]
  length = alph_count_tuple[0][1] + 1
  s = ""
  if len(alph_count_tuple)==1:
    pre_lst = [""]
  else:
    pre_lst = count_to_words_rec(alph_count_tuple[1:])
  for _ in range(length):
    lst += [s+pre_s for pre_s in pre_lst]
    s += chr
  return lst

def score(word):
  score=0
  for alph in word:
    if alph in ['a','e','h','i','n','o','r','s','t']:
      score+=1
    elif alph in ['c','d','l','m','u']:
      score+=2
    elif alph in ['b','f','g','p','v','w','y']:
      score+=3
    elif alph in ['j','k','q','x','z']:
      score+=4
    else:
      pass
  return score

def scored_words(words):
  lst = []
  for word in words:
    lst.append((word, score(word)))
  lst = sorted(lst, key=lambda x:x[1], reverse=True)
  return lst

def binary_search(sorted_random_word, new_dictionary):
    left=0
    right=len(new_dictionary)-1
    while left<=right:
        mid=int((left+right)/2)
        if new_dictionary[mid][0]==sorted_random_word:
            return new_dictionary[mid][1]
        elif new_dictionary[mid][0]<sorted_random_word:
            left=mid+1
        else:
            right=mid-1
    return ''

def anagram_solution(random_word, dictionary):
  words = scored_words(count_to_words_rec(count_alph(random_word)))
  for word in words:
    anagram = binary_search(word[0], dictionary)
    if anagram != '':
      return anagram
  return 'do not exist'

def readfile(filename):
  with open(filename) as f:
    l_strip = [s.strip() for s in f.readlines()]
    return l_strip
    f = open(filename, 'r')
    x = f.readlines()
    f.close()
    return x

print("start")

dictionary = readfile("words.txt")
small_list = readfile("small.txt")
medium_list = readfile("medium.txt")
large_list = readfile("large.txt")

print("new_dictionary start")

new_dictionary=[]
for word in dictionary:
    new_dictionary.append((''.join(sorted(word)), word))
new_dictionary = sorted(new_dictionary, key=lambda x:x[0])

print("small start")
#small_anagram
file=open('small_answer.txt', 'w')
for word in small_list:
  file.write(anagram_solution(word, new_dictionary)+"\n")
file.close

print("medium start")
#medium_anagram
file=open('medium_answer.txt', 'w')
for word in medium_list:
  file.write(anagram_solution(word, new_dictionary)+"\n")
file.close

print("large start")
#large_anagram
file=open('large_answer.txt','w')
for word in large_list:
  file.write(anagram_solution(word, new_dictionary)+"\n")
file.close
