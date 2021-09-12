from data_preparation import article_title
from tokenizing_articles import aon_list,SplitInput,terms_list,matrix,token

# End Function of TDM
def TDMAnd(list1, list2):
  result=[]
  for i in range(0, len(list1)):
    if(list1[i] == 1 and list2[i] == 1):
      result.append(1)
    else:
      result.append(0)

  return result

# OR Function of TDM

def TDMOr(list1, list2):
  result=[]
  for i in range(0, len(list1)):
    if(list1[i] == 1 or list2[i] == 1):
      result.append(1)
    else:
      result.append(0)

  return result

#Not Function of TDM
def TDMNot(list1, list2):
  result=[]
  for i in range(0, len(list1)):
    if(list1[i] == 1 and list2[i] == 0):
      result.append(1)
    else:
      result.append(0)

  return result

def printTitleTDM(list):
  title = ""
  for i in range(0, len(list)):
    if (list[i]==1):
      title = title + article_title[i] +"\n"

  return title

def TDMBooleanOperation(list):
  output_list = list[0]
  #print(output_list)

  for i in range(0,len(aon_list)):
    if (aon_list[i]=="and"):
      # print("AND")
      output_list = TDMAnd(output_list, list[i+1])
    elif (aon_list[i]=="or"):
      # print("OR")
      output_list = TDMOr(output_list, list[i+1])
    else:
      # print("NOT")
      output_list = TDMNot(output_list, list[i+1])
    
    #print(output_list)
  
  #print()
  return printTitleTDM(output_list) #jangan dikomen

def TermDocumentMatrix(query):
  SplitInput(query)

  # find index of each query token

  all_empty = [0]*len(matrix[0])

  term_index = [] #array menyimpan index term pada token list

  # find index of each query token
  for query_term in terms_list:
    i=0
    found=False
    print("query term : ", query_term)
    for term in token:

      if (term == query_term):
        found=True
        term_index.append(i)
        
      i+=1
    
    #apabila query word gada di token
    if (found==False):
      term_index.append(-1)


  #get list of each query token
  term_vector = [] 

  for indexOfTerm in term_index:
    if (indexOfTerm==-1):
      term_vector.append(all_empty)
    else:
      term_vector.append(matrix[indexOfTerm])

  #print(term_vector)
  return TDMBooleanOperation(term_vector)

#TermDocumentMatrix("Kota or jogjakarta")
