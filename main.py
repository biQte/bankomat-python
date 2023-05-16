pin_uzytkownika = '0055'
stan_konta = 1000
kurs_euro = 4.7

liczba_prob = 3

def wyswietl_menu():
    print("Wybierz operację podając odpowiedni numer:")
    print("1. Wyświetl stan konta")
    print("2. Wpłać środki")
    print("3. Wypłać środki")
    print("4. Wyświetl stan konta w EURO")
    print("5. Zakończ")
    operacja = input("Numer operacji: ")
    if int(operacja) == 1:
        wyswietl_stan_konta()
    elif int(operacja) == 2:
        wplac_srodki()
    elif int(operacja) == 3:
        wyplac_srodki()
    elif int(operacja) == 4:
        wyswietl_stan_w_euro()
    elif int(operacja) == 5:
        print("Kończę działanie programu!")
        exit()
    else:
        print("Niepoprawny numer operacji!")
        wyswietl_menu()

def wyswietl_stan_konta():
    print("Stan konta: ", stan_konta)
    wyswietl_menu()

def wplac_srodki():
    global stan_konta
    kwota_do_wplacenia = input("Podaj kwotę jaką chcesz wpłacić: ")
    if int(kwota_do_wplacenia) <= 0:
        print("Podano niepoprawną kwotę!")
        wyswietl_menu()
    else:
        stan_konta += int(kwota_do_wplacenia)
        print("Wpłacono: ", int(kwota_do_wplacenia), " złotych")
        wyswietl_menu()

def wyplac_srodki():
    global stan_konta
    kwota_do_wyplacenia = input("Podaj kwotę jaką chcesz wypłacić: ")
    if int(kwota_do_wyplacenia) <= 0:
        print("Podano niepoprawną kwotę!")
        wyswietl_menu()
    elif int(kwota_do_wyplacenia) > stan_konta:
        print("Podana kwota przekracza stan konta! Wypłacenie jest niemożliwe")
        wyswietl_menu()
    else:
        stan_konta -= int(kwota_do_wyplacenia)
        print("Wypłacono: ", kwota_do_wyplacenia, " złotych")
        wyswietl_menu()

def wyswietl_stan_w_euro():
    print(int(stan_konta * kurs_euro))
    wyswietl_menu()


while liczba_prob > 0:
    podany_pin = input("Podaj pin: ")
    liczba_prob -= 1
    if podany_pin == pin_uzytkownika:
        print("Poprawny pin")
        wyswietl_menu()
    elif podany_pin != pin_uzytkownika and liczba_prob == 0:
        print("Niepoprawny pin! Liczba prób: ", liczba_prob)
    else:
        print("Niepoprawny pin, spróbuj jeszcze raz, liczba prób: ", liczba_prob)
else:
    print("Wykorzystano maksymalną liczbę prób! Kończę działanie programu!")