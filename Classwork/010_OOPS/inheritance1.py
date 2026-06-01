class Pen:
    def __init__(self,price,color,company):
        self.price = price
        self.color = color
        self.company = company
    
    def display(self):
        print(self.price,self.color,self.company)

class Notebook(Pen):
    def __init__(self, price, color, company,pages): #extra property add karvi hoi to first ahiya and display ma lakhvu
        self.pages = pages  #child ne potani property use karvi pade aetle ahiya aa lakhvu pade
        super().__init__(price, color, company) #super-keyword parent class ne refer kare
    
    def display(self):
        print(self.price,self.color,self.company,self.pages)

p = Pen(30,"Red","DOMS")
p.display()

n = Notebook(40,"White","Classmate",50)
n.display()