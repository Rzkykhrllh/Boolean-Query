import tkinter as tk
from tkinter import ttk


LARGEFONT =("Helvetica", 16)

class KompasArticleFinderApp(tk.Tk):
	
	# __init__ function for class KompasArticleFinderApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (MainPage, SearchResultPage):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(MainPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class MainPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
        
		title = ttk.Label(self, text ="Kompas Article Finder", font = LARGEFONT)
		#title.grid(row = 0, column = 4, padx = 10, pady = 10)
        #search_entry = ttk.Entry(self)
        
       # button1 = ttk.Button(self, text ="Search", command = lambda : controller.show_frame(SearchResultPage))
        
      #  button1.grid(row = 1, column = 2, padx = 10, pady = 10)
        
		
       # search_entry.grid(row = 1, column = 2, padx = 10, pady = 10)
		# putting the grid in its place by using
		# grid
		
class SearchResultPage(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Search", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Main",
							command = lambda : controller.show_frame(MainPage))
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

# Driver Code
app = KompasArticleFinderApp()
app.mainloop()
