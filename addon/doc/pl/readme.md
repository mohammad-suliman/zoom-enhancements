# Zoom Accessibility Enhancements #

* Autorzy: Mohamad Suliman, Eilana Benish
* Pobierz [Wersja stabilna][1]
* Zgodność z wersjami NVDA: 2018.4 do 2020.2

Ten dodatek ułatwia użytkownikom NVDA korzystanie z programu Zoom. Wprowadza
skróty klawiszowe do obsługi alertów dla różnych zdarzeń podczas
spotkania. Poprawia też jakość wsparcia zdalnego, które staje się bardziej
dostępne.

## Skróty klawiszowe do obsługi alertów podczas spotkań

* NVDA + Shift + A: przełącza między różnymi trybami ogłaszania
  alertów. Dostępne są następujące tryby:

    * Tryb "Ogłaszaj wszystkie alerty", w którym każdy alert jest wymawiany.
    * Tryb "Ogłaszaj dźwiękiem", w którym NVDA odtwarza krótki sygnał
      dźwiękowy dla każdego alertu wyświetlanego przez Zoom.
    * Tryb "Wycisz wszystko", w którym NVDA ignoruje każdy alert.
    * "Tryb użytkownika", w którym można określić, jakie alerty mają być
      sygnalizowane, a jakie nie. Należy to zrobić w oknie ustawień dodatku
      lub za pomocą odpowiednich skrótów klawiszowych.

Następujące skróty służą do włączania lub wyłączania alertów każdego
typu. Uwaga! Działają tylko w trybie użytkownika.

* NVDA + Ctrl + 1: Uczestnik dołączył do spotkania/opuścił
  spotkanie. (Widoczne tylko dla organizatora)
* NVDA + Ctrl + 2: Uczestnik dołączył do poczekalni/opuścił
  poczekalnię. (Widoczne tylko dla organizatora)
* NVDA + Ctrl + 3: Organizator wyciszył audio.
* NVDA + Ctrl + 4: Organizator zatrzymał wideo.
* NVDA + Ctrl + 5: Uczestnik rozpoczął/zatrzymał dzielenie ekranu.
* NVDA + Ctrl + 6: Nadano/odebrano uprawnienia do nagrywania.
* NVDA + Ctrl + 7: Otrzymano publiczną wiadomość czatu.
* NVDA + Ctrl + 8: Otrzymano prywatną wiadomość czatu.
* NVDA + Ctrl + 9: Wysyłanie pliku do spotkania zakończone.
* NVDA + Ctrl + 0: Nadano/odebrano uprawnienia organizatora.
* NVDA + Shift + Ctrl + 1: Uczestnik podniósł/opuścił rękę. (Widoczne tylko
  dla organizatora)
* NVDA + Shift + Ctrl + 2: Nadano/odebrano uprawnienia do wsparcia zdalnego.
* NVDA + Shift + Ctrl + 3: Otrzymano wiadomość czatu


Uwaga! Aby dodatek działał poprawnie, należy zaznaczyć tryb "Ogłaszaj
wszystkie alerty" w ustawieniach dostępności Zoom.

## Skrót klawiszowy otwierający okno dodatku

NVDA + Z otwiera okno dodatku.

Można w nim:

* Sprawdzić, które alerty są ogłaszane, a które nie
* Wybrać, jakiego rodzaju alerty mają być ogłaszane
* Wybrać tryb ogłaszania alertów
* Zapisać zmiany urzytkownika

## Wsparcie zdalne

Po nadaniu uprawnień do wsparcia zdalnego, skrót NVDA + O przenosi kursor
systemu na lub poza kontrolowany zdalnie ekran.

Uwaga! Kursor systemu powinien znajdować się na jednej z kontrolek
spotkania, aby można było kontrolować zdalnie inny ekran.

## Ważne!

Funkcja Trybu Użytkownika pozwalająca określić, które alerty mają być
ogłaszane, a które nie, działa tylko wtedy, gdy język interfejsu użytkownika
w programie Zoom jest ustawiony na angielski.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
