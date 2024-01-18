#constructor

class Fruit:
    
    def displayData(self,name:str,price:int):
       return print(name,price)
    

obj=Fruit() 
        
obj.displayData("Apple",250)