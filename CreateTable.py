from tkinter import *
class Table:
    def __init__(self, main):
        self.root = main
        for i in range(rows):
            for j in range(columns):
                if i == 0:
                    self.entry = Entry(self.root, width=20, fg='red',
                               font=('Arial',16,'bold'))
                    self.entry.grid(row=i, column=j)
                    self.entry.insert(END, lst[i][j])
                else:
                    self.entry = Entry(self.root, width=20, fg='blue',
                                font=('Arial',16,'bold'))
                    self.entry.grid(row=i, column=j)
                    self.entry.insert(END, lst[i][j])
  
# take the data
lst = [('STT', 'Name','Address','Age'),
       (1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
# find total number of rows and
# columns in list
rows = len(lst)
columns= len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()