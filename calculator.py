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