#!pip install nltk
import nltk
nltk.download('punkt')

import os

directory_in_str = "Dataset kompas"
directory = os.fsencode(directory_in_str)
i=0

artikel_file_name = [None] * 2008

#dapatin artikel_file_name
for file in os.listdir(directory):
  filename = os.fsdecode(file)
  test_artikel = filename
  if filename.endswith(".txt"): 
    artikel_file_name[i] = filename
    i = i+1
    continue
  else:
    continue

#Menyimpan isi teks ke article_content

artikel_content = []

i=0

banyak_artikel = 500

for filename in artikel_file_name:
  path = "Dataset kompas/" + str(filename)

  if (i<=banyak_artikel):
    with open(path, 'r') as file:
      artikel_content.insert(len(artikel_content), file.read())
      # print(artikel_content[i])

  i+=1
# print(100)

# Simpan Judul Artikel
i=0
article_title = []
for i in range(0,banyak_artikel+1):
  article_title.insert(len(article_title),artikel_content[i].partition('\n')[0])

# print(*article_title, sep = "\n")