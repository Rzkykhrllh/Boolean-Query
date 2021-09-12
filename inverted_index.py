from tokenizing_articles import SplitInput,terms_list,aon_list
from data_preparation import article_title,artikel_content,banyak_artikel

def InvertedIndex(query):
  SplitInput(query)

  #Create Linked List
  query_result = []

  i=0
  j=0
  for i in range(0, len(terms_list)):
    temp = set() 
    query_result.insert(len(query_result),temp)

  j=0 # query word

  while (j<len(terms_list)):
    print(j," : ",terms_list[j])
    i=0 #artikel

    while (i<=banyak_artikel):
      search = artikel_content[i].find(' '+terms_list[j]+' ')
      
      if (search != -1):

        query_result[j].add(i)
      
      i+=1
    j+=1


  print(*query_result, sep = "\n")
  print()




  #Opearsi Query
  output_list = query_result[0]
  print(output_list)

  for i in range(0,len(aon_list)):
    if (aon_list[i]=="and"):
      # print("AND")
      output_list = InvertedAnd(output_list, query_result[i+1])
    elif (aon_list[i]=="or"):
      # print("OR")
      output_list = InvertedOr(output_list, query_result[i+1])
    else:
      # print("NOT")
      output_list = InvertedNot(output_list, query_result[i+1])
    
    print(output_list)
  
  print()
  print(printTitleInverted(output_list)) #jangan di method
  
# And Function
def InvertedAnd(set1, set2):
  set1 = set1.intersection(set2)
  return set1

# Or Function
def InvertedOr(set1, set2):
  set1 = set1.union(set2)
  return set1

def InvertedNot(set1,set2):
  set1 = set1.difference(set2)
  return set1

def printTitleInverted(myList):
  title=""
  output_list = sorted(myList)
  for x in output_list:
    title = title + article_title[x] +"\n"
    
  
  return title

InvertedIndex("jogja") # PANGGIL FUNGSI INI ENTAR BUAT INVERTED MATRIX

