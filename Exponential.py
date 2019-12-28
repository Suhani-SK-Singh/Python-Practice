# A program to calculate and prints an approximation of the quantity e^x
#Formulae e^x=(x^0/0! + x^1/1! + x^2/2! + x^3/3! + - - - - + x^99/99!

#Student name : Suhani
#Student number: 119220491


def factorial_value(value):
    """
    This function calculates factorial by.

    Arguments:
    1. value :any number for which we have to find factorial
    
    Return:
    factorial:final output of factorial
    """
    factorial=1

    for i in range(1,value+1):
        factorial=factorial*i

    return factorial

def exponential_power(value,r):
    """
    This function calculates exponential e^x .

    Arguments:
    1.)value:for which we need to calculate exponential.
    2.)r:No.of terms of infinte sum to be computed

    Return Value:
    first_value : 
    """
    first_value =0
    try:
        for element in range(r):
            next_value=float(value) ** element /factorial_value(element)
            first_value += next_value
        return first_value
    except ValueError:
        print('The number you have entered is not an integer or floating number')

number =input('Input the number whose exponential power you want to find:')
exp_value =exponential_power(number,100)
print('The value of e^{} is :{}'.format(number,exp_value))
