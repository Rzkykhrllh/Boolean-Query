import tkinter as tk

FONT = ("Helvetica",16) 

class KompasArticleFinderApp(tk.Tk):    
    
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in (MainPage,SearchResultPage):
            if(F == SearchResultPage):
                frame = F(container,self,"")
            else:
                frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(MainPage)
    
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
   
    def ui_main(self):
        frame = tk.Frame(self.root)
        frame.place(relx=.5,rely=.5,anchor=tk.CENTER)
        
        tk.Label(frame,name="title", text = "Kompas Article Finder", font=FONT).pack(side = tk.TOP,pady=20,padx=5)
        tk.Button(frame,name="btn_search",text="Search",command=self.search).pack(side = tk.RIGHT)
        tk.Entry(frame,width=50,name="search_box").pack(side = tk.RIGHT,padx=10)
        self.root.mainloop()

    
    def ui_search_result(self,search_result):
        frame = tk.Frame(self.root)
        frame.place(relx=0.05,rely=0.05,anchor=tk.NW)
        
        tk.Button(frame,name="btn_search",text="Search",command=self.search).pack(side=tk.RIGHT,padx=10)
        tk.Entry(frame,width=50,name="search_box").pack(side=tk.RIGHT)
       
        tk.Label(self.root,text=search_result,justify=tk.LEFT).place(relx=0.05,rely=0.1,anchor=tk.NW)
        self.root.mainloop()
        

class MainPage(tk.Frame):
    def search():
        print('')
        
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        
        title = tk.Label(self,name="title", text = "Kompas Article Finder", font=FONT)
        title.pack(side = tk.TOP,pady=20,padx=5)
        
        btn_search = tk.Button(self,name="btn_search",text="Search",command= lambda : controller.show_frame(SearchResultPage))
        btn_search.pack(side = tk.RIGHT)
        
        search_entry = tk.Entry(self,width=50,name="search_box")
        search_entry.place(relx=.5,rely=.5,anchor = tk.CENTER)  

class SearchResultPage(tk.Frame):
    
    def __init__(self,parent,controller,search_query):
        tk.Frame.__init__(self, parent)
        print(search_query)
        btn_search = tk.Button(self,name="btn_search",text="Search",command=self.search)
        btn_search.pack(side=tk.LEFT,padx=10)
        
        search_entry = tk.Entry(self,width=50,name="search_box")
        search_entry.pack(side=tk.TOP)
       
        txt_search_result = tk.Label(self,text="Hello world",justify=tk.LEFT)
        txt_search_result.pack(side=tk.BOTTOM,padx = 20)
        
    def search():
        print('')
                
app = KompasArticleFinderApp(className="Kelompok 1 - Boolean Retrieval",baseName=None,useTk=1)
app.mainloop()

