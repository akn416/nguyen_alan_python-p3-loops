



def square_integers(int_list):
    square_integers = [square ** 2 for square in int_list]
    print(square_integers)
    

square_integers([-1, -2, -3, -4, -5])

def square_integerz(int_list):
    new_list = list()
    for square in int_list:
        new_int = square ** 2
        new_list.append(new_int)
    print(new_list)

square_integerz([1, 2, 3, 4, 5])