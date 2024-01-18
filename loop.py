

# arr=["Ram","Syam","Hari","Sudip"]

# for index,value in enumerate(arr):
#     if(index%2==0):
#         print(value

# value=input("Enter any number:")
# print(value)




def toFahrenheit(c):
    fahrenheit=(9*c)/5+32
    print("The fahrenheit valus is ",fahrenheit)

def toCelsius(f):
    celsius=((f-32)*5)/9
    print("The celsius value is ",celsius)            
    
# Taking user decision 
inputValue=int(input("Enter 1 to convert celsius into fahrenheit and 2 to convert fahrenheit into celsius:"))

if inputValue==1:
    c=int(input("Enter celsius value:"))
    toFahrenheit(c)
elif inputValue==2:
    f=int(input("Enter fahrenheit value:"))
    toCelsius(f)
else:
    print("Invalid")    

# def division(a,b):
#     try:
        
#         # if b==0:
#         #    raise Exception("Infinity")
#         result=a/b
#         return result
#     # except ZeroDivisionError as e:
#     #     print(e)
#     except Exception as e:
#         print(e)
    
        
        
# division(2,0)