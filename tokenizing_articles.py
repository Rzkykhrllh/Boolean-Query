# Membuang tanda baca pada setiap artikel

import re
from nltk.tokenize import word_tokenize
from data_preparation import artikel_content,banyak_artikel 

i = 0
while (i<len(artikel_content)):
    temp = artikel_content[i]
    
    temp = temp.lower()
    # temp = re.sub(r"\d+", "", temp) #remove number
    temp = re.sub(r'[^\w\s]', '', temp) #remove punctuation
    temp = temp.strip().lstrip() #remove whitespacee
    temp = temp.replace("\n", " ")
    
    artikel_content[i] = temp
    i+=1

# print(t)

# Create list of all term in everydocument


token = set()

i=0
while (i<=banyak_artikel):
  token = token.union(set(word_tokenize(artikel_content[i])))
  i+=1

token = sorted(token)

print(token)


# Create Term-Document Matrix
matrix=[]
for kata in token : #loop ever term
  temp = []
  
  for artikel in artikel_content: #loop every artikel
    if (" "+kata+" " in artikel): #if term in artikel
      temp.append(1)
    else :
      temp.append(0)

  matrix.append(temp)

# print(*matrix, sep = "\n")

#Getting query word from input
aon_list = []
terms_list = []

def SplitInput(input_string):
  query_token = word_tokenize(input_string.lower())
  print (query_token)

  aon_list.clear()
  terms_list.clear()

  for q in query_token:
    if q == 'and':
      aon_list.append(q)
    elif q == 'or':
      aon_list.append(q)
    elif q == 'not':
      aon_list.append(q)
    else:
      terms_list.append(q)
    
  print (terms_list)
  print (aon_list)
  print()
