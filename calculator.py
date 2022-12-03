import logging

logging.basicConfig(level=logging.INFO)

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
    logging.info("Wynik to: {}".format(add_result))      
elif choice == '2':
    sub_result = subtract(num1,num2)
    logging.info("Dodaję {} i {}".format(num1, num2))
    logging.info("Wynik to: {}".format(sub_result))    
elif choice == '3':
    multi_result = multiply(num1,num2)
    logging.info("Dodaję {} i {}".format(num1, num2))
    logging.info("Wynik to: {}".format(multi_result))       
elif choice == '4':
    div_result = divide(num1,num2)
    logging.info("Dodaję {} i {}".format(num1, num2))
    logging.info("Wynik to: {}".format(div_result))       
else:    
    logging.error("Podaj liczbę!")