# use following Commands to check
'''
C=Customer('john','Sena',123,'zip123',60)
C=Customer('john1','Sena',123,'zip123',60)
C=Customer('john2','Sena',123,'zip123',60)
C=Customer('john3','Sena',123,'zip123',60)

E=Employee()
D=[]
D.append(E.emp_det('john','Sena'))
D.append(E.emp_det('joh1n','Sena'))
D.append(E.emp_det('john2','Sena'))
D.append(E.emp_det('john3','Sena'))
D.append(E.emp_det('joh4n','Sena'))

address='No:7,abc,xyz,ZIP123'
phno=1234
sales=1000
S=Store(D,address,phno,sales)
x=[['joh4n','Sena']]
S.addEMP(x)
S.removeEMP(x)
y=[['john','Sena']]
S.removeEMP(y)
price,crust_type=10,'thick'
toppings=['Pepperoni','Mushrooms','Onions','Sausage','Bacon','Extra cheese','Black olives','Green peppers']
P=Pizza(toppings,price,crust_type)
P.add_top('Chicken balls')
P.remove_top('Pepperoni')


po=Pizzaorders()
np=[2,'Mushrooms','Thin',50,'store1']
po.add_pizza(np)
np=[2,'peper','Thin',50,'store2']
po.add_pizza(np)
po.remove_pizza(np)
po.order_status('jo')
po.apply_promo('PAPATONY100')
po.apply_promo('PAPATONY50')
'''
import random
global EMP
class Customer:
    
     def __init__(self,FN,LN,PH_NO,ZIP,FMN):
         self.customer_details=[]
         self.customer_details.append([FN,LN,PH_NO,ZIP,FMN])
         #print(self.customer_details)
     
class Employee:
    
     def emp_det(self,FN,LN):
         self.employee_details=[]
         
         self.employee_details.append([FN,LN])
         self.detE=self.employee_details.copy()
         return self.detE
         
class Store(object):
     def __init__(self,D,address,phno,sales):
         print("ADDRESS:",address)
         print("Phone Number:",phno)
         print("Monthly Sales:",sales)
         self.EMP=D
     def addEMP(self,EP):
         self.EMP.append(EP)
         print(self.EMP)
     def removeEMP(self,EP1):
         self.EMP.remove(EP1)
         print("**********")
         print(self.EMP)
class Pizza(object):
     def __init__(self,toppings,price,crust_type):
         self.toppings=toppings
         print('Price is:',price)
         print('Crust Type is:',crust_type)
         for i in range(len(toppings)):
             print('Toppings are:')
             print(toppings[i])
     def add_top(self,T_item):
         self.toppings.append(T_item)
         print(self.toppings)
     def remove_top(self,T_item):
         self.toppings.remove(T_item)
         print(self.toppings)

class Pizzaorders(object):
     def __init__(self):
         self.pizza=[]
         
     def add_pizza(self,np):
         self.pizza.append(np)
         print(self.pizza)
     def remove_pizza(self,np):
         self.pizza.remove(np)
         print(self.pizza)
     def order_status(self,customer):
         r=random.randint(0,4)
         if r==0:
             print('Hello {0}! your order is Cancelled. Sorry for the inconvince!'.format(customer))
         elif r==1:
             print('Hello {0}! your order is Created.'.format(customer))
         elif r==2:
             print('Hello {0}! your order is Ready.'.format(customer))
         elif r==3:
             print('Hello {0}! your order on delivery.'.format(customer))
         elif r==4:
             print('Hello {0}! your order completed.'.format(customer))
     def apply_promo(self,promo):
        if promo=='PAPATONY100':
            print('Congrats!Promo Applied!')
        else:
            print('Invalid Promo!,Better luck next time!')
         
         
         
         


