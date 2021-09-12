from term_document_matrix import TermDocumentMatrix
from inverted_index import InvertedIndex
import tkinter as tk

FONT = ("Helvetica",16) 
INVERTED_INDEX_CODE= 1
TDM_CODE = 2

class KompasArticleFinderApp:    
    
    def __init__(self,root):
        self.root = root
        self.root.minsize(600,600)
      
    def ui_search_result(self):
        var = tk.IntVar()
        var.set(1)
        tk.Radiobutton(self.root,text="Inverted Index",variable = var,value=INVERTED_INDEX_CODE).place(x=20,y=20)
        tk.Radiobutton(self.root,text="Term document Matrix",variable = var,value=TDM_CODE).place(x=120,y=20)
               
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack( side = tk.RIGHT, fill = 'y' )

        list_result = tk.Text(self.root, yscrollcommand = scrollbar.set )
        list_result.place(x=20,y=90,relwidth=0.9,relheight=0.9 )  
        #list_result.pack(fill='x',expand=True,padx=10)
        
        search_entry = tk.Entry(self.root,width=50,name="search_box")
        search_entry.place(x=20,y=50)
        
        #search_result = tk.Label(self.root,text="",justify=tk.LEFT)
        #search_result.place(x=20,y=90)       
       
        btn_search = tk.Button(self.root,text="Search",command= lambda: (
            #search_result.config(text= InvertedIndex(str(search_entry.get()).lower()) if var.get()==INVERTED_INDEX_CODE else TermDocumentMatrix(str(search_entry.get()).lower()))
            list_result.insert(tk.END,InvertedIndex(str(search_entry.get()).lower()) if var.get()==INVERTED_INDEX_CODE else TermDocumentMatrix(str(search_entry.get()).lower()))                
        ))
        btn_search.place(x=330,y=45)
        
        self.root.mainloop()  

app = KompasArticleFinderApp(tk.Tk(screenName=None,baseName=None,className='Kelompok 1 - Boolean Retrieval',useTk=1))
app.ui_search_result()


