import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)

def add(x, y):  
   return x + y   
def subtract(x, y):  
   return x - y   
def multiply(x, y):   
   return x * y   
def divide(x, y):      
   return x / y

choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1.Dodawanie, 2.Odejmowanie, 3.Mnożenie, 4.Dzielenie: ")

num1 = float(input ("Podaj składnik 1: "))    
num2 = float(input ("Podaj składnik 2: "))

if choice == '1':
    add_result = add(num1,num2)
    logging.info("Dodaję {} i {}".format(num1, num2))
    print("Wynik to:", add(num1,num2))      
elif choice == '2':
    logging.info("Dodaję {} i {}".format(num1, num2))
    print("Wynik to:", subtract(num1,num2))    
elif choice == '3':
    logging.info("Dodaję {} i {}".format(num1, num2))
    print("Wynik to:", multiply(num1,num2))       
elif choice == '4':
    logging.info("Dodaję {} i {}".format(num1, num2))
    print("Wynik to:", divide(num1,num2))       
else:    
    print("Podaj liczbę!")