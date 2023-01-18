import logging

logging.basicConfig(format="%(message)s", level=logging.INFO)

# This function add two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiply two numbers
def multiply(x, y):
    return x * y


# This divide multiply two numbers
def divide(x, y):
    return x / y


if __name__ == "__main__":
    
    # Take input from user
    choice = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1.Dodawanie, 2.Odejmowanie, 3.Mnożenie, 4.Dzielenie: "
    )
    num1 = float(input("Podaj składnik 1: "))
    num2 = float(input("Podaj składnik 2: "))

    # Check choice from user
    if choice == "1":
        logging.info("Dodaję {} i {}".format(num1, num2))
        print("Wynik to:", add(num1, num2))

    elif choice == "2":
        logging.info("Odejmuję {} i {}".format(num1, num2))
        print("Wynik to:", subtract(num1, num2))

    elif choice == "3":
        logging.info("Mnożę {} i {}".format(num1, num2))
        print("Wynik to:", multiply(num1, num2))

    elif choice == "4":
        logging.info("Dzielę {} i {}".format(num1, num2))
        print("Wynik to:", divide(num1, num2))

    else:
        print("Podaj liczbę!")
