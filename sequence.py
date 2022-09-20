def main():
    exit = False
    list = get_list()
    _pass = 1

    while not deviation_zero(list) and not list_of_one(list):
        print(list,_pass)
        _pass += 1 
        list = deviation_array(list)


def get_list():
    while True:
        try:
            a = input("Digite sua lista(digite os termos separados por espaços): ")        
            return string_to_float_array(a)
        except:
            print("Não foi possivel converter a lista, certifique-se de que todos os elementos sejam numeros")


def list_of_one(list):
    if len(list) == 1:
        return True
    return False


def string_to_float_array(str):
    x = str.split()
    a =[]
    for i in x:
        a.append(float(i))

    return a


def deviation_array(list):
    a=[]
    for i in range(len(list)):
        if i < len(list)-1:
            a.append(list[i+1]-list[i])
    
    return a


def deviation_zero(list):
    for i in list:
        if i != 0.0:
            return False
    return True


main()
