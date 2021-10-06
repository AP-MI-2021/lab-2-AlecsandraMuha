def is_palindrome(n):
    '''
    determinam daca un numar este palindrom sau nu
    :return True daca numarul este palindrom sau False in caz contrar
    '''
    x = n
    inv = 0
    while x:
        c = x % 10
        inv = inv * 10 + c
        x = x // 10
    if n == inv:
        return True
    else:
        return False
def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(237) == False
def is_prime(n):
    '''
    verificam daca un numar este prim sau nu
    :param n: numarul pe care il verificam daca este prim sau nu
    :return: True daca numarul este prim sau False in caz contrar
    '''

    for d in range(2, int(n ** (1 / 2)) + 1):
        if n % d == 0:
            return False
    return True
def is_superprime(n):
    '''
    verificam daca un numar este superprim sau nu
    :return:True daca numarul este superprim sau False in caz contrar
    '''

    n = [int(i) for i in str(n)]
    nr = 0
    for i in n:
        nr = nr * 10 + i
        if is_prime(nr) == False:
            return False
    return True
def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False
def is_antipalindrome(n):
    '''
    Determina daca un numar dat n este antipalindrom
    :param n:numarul dat
    :return: True daca n este antipalindrom si False in cazul in care n nu este antipalindrom
    '''

    nrc = 0
    x = n
    while x!= 0:
        nrc= nrc + 1
        x = x// 10
    x = n
    inv = 0
    while x != 0:
        inv = inv * 10 + x % 10
        x = x // 10
    i = nrc // 2
    while i != 0:
        if n % 10 == inv % 10:
            return False
        i = i - 1
        n = n // 10
        inv = inv // 10
    return True


def test_is_antipalindrome():
    assert is_antipalindrome(1234) == True
    assert is_antipalindrome(2773) == False
def main():
    while True:
        print("Optiunea 1.Determină dacă un număr dat este palindrom")
        print("Optiunea 2.Determină dacă un număr este superprim")
        print("Optiunea 3.Determină dacă un număr dat este antipalindrom")
        print("Optiunea 4.iesire")
        option = input("selectati optiunea: ")
        if option == "1":
            test_is_palindrome()
        elif option == "2":
            test_is_superprime()
        elif option == "3":
            test_is_antipalindrome()
        elif option == "4":
            break
        else:
            print("optiune gresita.selecteaza alta optiune")
main()

if __name__ == '__main__':

    test_is_palindrome()
    test_is_superprime()
    test_is_antipalindrome()
main()
exit(0)

