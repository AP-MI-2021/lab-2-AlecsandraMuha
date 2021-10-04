def main():
    while True:

        print("Optiunea 1.Determină dacă un număr dat este palindrom")
        print("Optiunea 2.Determină dacă un număr este superprim")
        print("Optiunea 3.iesire")

        option = input("selectati optiunea: ")

        if option == "1":
            print(test_is_palindrome(n))


        elif option == "2":
            print(test_is_superprime(n))

        elif option == "3":
            break

        else:
            print("optiune gresita.selecteaza alta optiune")


main()


def is_palindrome(n):
    n = [i for i in str(n)]
    if n != n[::-1]:
        return False
    return True


def test_is_palindrome():
    n = int(input('Introduceti un numar:'))
    if is_palindrome(n):
        print("este palindrom")
    else:
        print("nu este palindrom")


test_is_palindrome()


def is_prime(n):
    for d in range(2, int(n ** (1 / 2)) + 1):
        if n % d == 0:
            return False
    return True


def is_superprime(n):
    n = [int(i) for i in str(n)]
    nr = 0
    for i in n:
        nr = nr * 10 + i
        if is_prime(nr) == False:
            return False
    return True


def test_is_superprime():
    n = int(input('Introduceti un numar:'))
    if is_superprime(n):
        print('este superprim')
    else:
        print('nu este superprim')


test_is_superprime()
