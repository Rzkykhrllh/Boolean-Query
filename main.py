from term_document_matrix import TermDocumentMatrix
import tkinter as tk

FONT = ("Helvetica",16) 

class KompasArticleFinderApp:    
    
    def __init__(self,root):
        self.root = root
        self.root.minsize(600,600)
        
    def search(self,text):
        #print(str(TermDocumentMatrix(text)))
        #return text
        print(text)
      
   
#    def ui_main(self):
#        frame = tk.Frame(self.root)
#        frame.place(relx=.5,rely=.5,anchor=tk.CENTER)
        
#        tk.Label(frame,name="title", text = "Kompas Article Finder", font=FONT).pack(side = tk.TOP,pady=20,padx=5)
#       tk.Button(frame,name="btn_search",text="Search",command=self.do_something).pack(side = tk.RIGHT)
#        tk.Entry(frame,width=50,name="search_box").pack(side = tk.RIGHT,padx=10)
#        self.root.mainloop()

    
    def ui_search_result(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.05,rely=0.1,anchor=tk.NW)
                
        search_entry = tk.Entry(self.root,width=50,name="search_box")
        search_entry.place(x=20,y=50)
        
        search_result = tk.Label(self.root,text="helloskjdnfksjndf")
        search_result.place(x=20,y=90)       
        
        btn_search = tk.Button(self.root,text="Search",command= lambda: search_result.config(text=search_entry.get()))
        btn_search.place(x=330,y=45)
        
        var = tk.IntVar()
        tk.Radiobutton(self.root,text="Inverted Index",variable = var,value=1).place(x=20,y=20)
        tk.Radiobutton(self.root,text="Term document Matrix",variable = var,value=2).place(x=120,y=20)
        
        self.root.mainloop()
    
    def do_something(self):
        print("")
    

app = KompasArticleFinderApp(tk.Tk(screenName=None,baseName=None,className='Kelompok 1 - Boolean Retrieval',useTk=1))
app.ui_search_result()


