def read_list1():
    """
    Citire prima lista
    :return: lista de numere intregi
    """
    n=int(input("Introduceti nr de elemente pentru prima lista: "))
    lst1=[]
    for i in range(n):
        x=int(input("a[{}]= ".format(i+1)))
        lst1.append(x)
    return lst1

def read_list2():
    """
    Citire a doua lista
    :return: lista de numere intregi
    """
    n=int(input("Introduceti nr de elemente pentru a doua lista: "))
    lst2=[]
    for i in range(n):
        x=int(input("b[{}]= ".format(i+1)))
        lst2.append(x)
    return lst2


def concateneaza_numerele(nr1, nr2):
    """
    Determina numarul obtinut prin concatenarea nr1 cu nr2
    :param nr1: numar intreg
    :param nr2: numar intreg
    :return: numar intreg
    """
    #le concatenez (fac o metoda care sa includa si cazul nr1=360, nr2=63 de ex)
    nr_nou=nr1
    #formez invers pentru nr 2
    invers_nr2=0
    while nr2 !=0:
        invers_nr2 = invers_nr2 * 10 + int(nr2 % 10)
        nr2 //=10
    #concatenez nr1 cu inversul nr2
    while invers_nr2 != 0:
        nr_nou= nr_nou*10 + int(invers_nr2 % 10)
        invers_nr2 //= 10
    return nr_nou

def test_concateneaza_numerele():
    assert concateneaza_numerele(1245, 6789) == 12456789
    assert concateneaza_numerele(1,12) == 112
    assert concateneaza_numerele(2,2) == 22
    assert concateneaza_numerele(132, 234) == 132234

test_concateneaza_numerele()

def verif_palindrom(nr1, nr2):
    """
    verificam daca numarul formal e egal cu oglinditul sau
    :param nr1: numar intreg
    :param nr2: numar intreg
    :return: True daca numarul obtinut este palindrom, false alfel
    """
    nr_nou= concateneaza_numerele(nr1, nr2)
    #verific daca nr format e egal cu oglinditul sau
    invers_nr_nou=0
    copie_nr_nou=nr_nou
    while copie_nr_nou != 0:
        invers_nr_nou = invers_nr_nou * 10 + int(copie_nr_nou % 10)
        copie_nr_nou //= 10
    return invers_nr_nou == nr_nou

def test_verif_palindrom():
    assert verif_palindrom(360, 63) == True
    assert verif_palindrom(1, 1) == True
    assert verif_palindrom(10, 1) == True
    assert verif_palindrom(234, 764) == False

test_verif_palindrom()

def palindroame_obtinute(lst1, lst2):
    """
    Afisarea tuturor palindroamelor obtinute prin concatenarea elementelor de pe
    aceleași poziții în lst1 si lst2.
    :param lst1: prima lista de numere intregi
    :param lst2: a doua lista de numere intregi
    :return:
    """
    palindroame=[]
    if len(lst1) > len(lst2):
        for i in range(0, len(lst2)):
            if verif_palindrom(lst1[i], lst2[i]) == 1:
                palindroame.append(concateneaza_numerele(lst1[i], lst2[i]))
    else:
        for i in range(0, len(lst1)):
            if verif_palindrom(lst1[i], lst2[i]) == 1:
                palindroame.append(concateneaza_numerele(lst1[i], lst2[i]))
    return palindroame

def test_palindroame_obtinute():
    assert palindroame_obtinute([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]
    assert palindroame_obtinute([133, 22, 36, 11], [331, 23, 63, 55, 424]) == [133331, 3663]
    assert palindroame_obtinute([143, 22, 78], [23, 63, 55, 424]) == []

test_palindroame_obtinute()

def intersectia_listelor(lst1, lst2):
    """
    Determina o listă care reprezinta intersecția dintre lst1 si lst2.
    :param lst1: prima lista de numere intregi
    :param lst2: a doua lista de numere intregi
    :return:
    """
    lst3=[]
    ele=0
    for i in range (0, len(lst1)):
        for j in range(0, len(lst2)):
            if lst1[i] == lst2[j]:
                ele = lst1[i]
                lst3.append(ele)
    return lst3

def test_intersectia_listelor():
    assert intersectia_listelor([12, 22, 36, 424], [22, 23, 36, 55, 424]) == [22, 36, 424]
    assert intersectia_listelor([-5, -4, 0], [-8, -5, 9]) == [-5]
    assert intersectia_listelor([12, 22, 36, 424], [1, 2, 3,]) == []
    assert intersectia_listelor([23, 45, 67], [23, 45, 67]) == [23, 45, 67]

test_intersectia_listelor()

def nr_egal_elem_pare(lst1, lst2):
    """
    Determinati dacă lst1 si lst2 au același număr de elemente pare.
    :param lst1: prima lsita de nr intregi
    :param lst2: a doua lista de numere intregi
    :return: True daca au acelasi numar de elmente egale, False altfel
    """
    k1 = 0 #nr de elm pare pt lst1
    k2 = 0  # nr de elm pare pt lst2
    for i in range(0, len(lst1)):
        if int(lst1[i]%2==0):
            k1=k1+1
    for i in range(0, len(lst2)):
        if int(lst2[i]%2==0):
            k2=k2+1
    if k1==k2:
        return True
    else:
        return False

def test_nr_egal_elem_pare():
    assert nr_egal_elem_pare([2, 3, 4], [1, 3, 5, 9]) == False
    assert nr_egal_elem_pare([-8, 3, 9, 9], [3, 0, 9]) == True

test_nr_egal_elem_pare()


def show_menu():
    print("""
    1. Citire doua liste
    2. Afișați dacă cele două liste au același număr de elemente pare.
    3. Afișați o listă reprezentând intersecția listelor citite de la tastatură.
    4. Afișați toate palindroamele obținute prin concatenarea elementelor de pe 
    aceleași poziții în cele două liste.
    5. Citiți o a treia listăși afișați listele obținute prin înlocuirea în cele 
    două liste citite la punctul 1 a tuturor elementelor cu oglinditul lor dacă 
    îndeplinesc următoarea regulă: elementele sunt divizibile cu toate elementele 
    din a treia lista. Dacă nu îndeplinesc regula, păstrați elementul așa cum e.
    6. Afisare cele doua liste
    x. Iesire
    """)


def main():
    show_menu()
    lst1 = []
    lst2 = []
    while True:
        cmd=input("Introduceti comanda: ")
        if cmd=='1':
            lst1 = read_list1()
            lst2 = read_list2()
        elif cmd=='2':
            rez = nr_egal_elem_pare(lst1, lst2)
            print(rez)
        elif cmd=='3':
            rez = intersectia_listelor(lst1, lst2)
            print(rez)
            pass
        elif cmd=='4':
            rez = palindroame_obtinute(lst1, lst2)
            print(rez)
        elif cmd=='5':
            pass
        elif cmd=='6':
            print(lst1)
            print(lst2)
        elif cmd=='x':
            break
        else:
            print("Comanda invalida")

main()