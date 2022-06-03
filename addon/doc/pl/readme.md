# Zoom Accessibility Enhancements #

* Autorzy: Mohamad Suliman, Eilana Benish
* Pobierz [Wersja stabilna][1]
* Zgodność z wersjami NVDA: od 2018.4 do 2022.1

Ten dodatek ułatwia użytkownikom NVDA korzystanie z programu Zoom. Wprowadza
skróty klawiszowe do obsługi alertów dla różnych zdarzeń podczas
spotkania. Poprawia też jakość wsparcia zdalnego, które staje się bardziej
dostępne.

## skróty klawiaturowe służące do kontrolowania alertów w spotkaniach 

* NVDA + Shift + A: przełącza między różnymi trybami ogłaszania
  alertów. Dostępne są następujące tryby:

    * Zgłoś wszystkie alerty w trybie, w którym wszystkie alerty są
      zgłaszane jak zwykle
    * Sygnał dźwiękowy dla alertów, w którym NVDA będzie odtwarzać krótki
      sygnał dźwiękowy dla każdego alertu wyświetlanego w Zoom
    * Wycisz wszystkie alerty, gdzie NVDA zignoruje wszystkie alerty
    * Tryb niestandardowy, w którym użytkownik może dostosować, które alerty
      chce mieć, a które nie. Można to zrobić za pomocą okna dialogowego
      ustawień dodatku lub za pomocą dedykowanych skrótów klawiaturowych do
      tego celu.

Następujące skróty mogą być używane do włączania / wyłączania ogłoszeń
każdego typu alertu (należy pamiętać, że będzie to skuteczne po wybraniu
trybu niestandardowego):

* NVDA + Ctrl + 1: Uczestnik dołączył do spotkania/opuścił
  spotkanie. (Widoczne tylko dla organizatora)
* NVDA + Ctrl + 2: Uczestnik dołączył do poczekalni/opuścił
  poczekalnię. (Widoczne tylko dla organizatora)
* NVDA + Ctrl + 3: Dźwięk wyciszony przez hosta
* NVDA + Ctrl + 4: Wideo zatrzymane przez hosta
* NVDA + Ctrl + 5: Udostępnianie ekranu rozpoczęte/zatrzymane przez
  uczestnika
* NVDA + Ctrl + 6: Zezwolenie na nagrywanie udzielone/cofnięte
* NVDA + Ctrl + 7: Otrzymano publiczny czat na spotkaniu
* NVDA + Ctrl + 8: Otrzymano prywatny czat na spotkaniu
* NVDA + Ctrl + 9: Przesyłanie pliku na spotkaniu zakończone
* NVDA + Ctrl + 0: Przywilej hosta przyznany/odwołany
* NVDA + Shift + Ctrl + 1: Uczestnik podniósł/opuścił rękę. (Widoczne tylko
  dla organizatora)
* NVDA + Shift + Ctrl + 2: Udzielone/odwołane uprawnienie do zdalnego
  sterowania
* NVDA + Shift + Ctrl + 3: Otrzymano wiadomość czatu


Uwaga! Aby dodatek działał poprawnie, należy zaznaczyć tryb "Ogłaszaj
wszystkie alerty" w ustawieniach dostępności Zoom.

## Skrót klawiaturowy dla Otwieranie dodatku w oknie dialogowym 

NVDA + Z Otwiera okno dialogowe dodatku!

Można w nim:

* Sprawdzić, które alerty są ogłaszane, a które nie
* Wybrać, jakiego rodzaju alerty mają być ogłaszane
* Wybrać tryb ogłaszania alertów
* Zapisać zmiany urzytkownika

## Pilot 

po przyznaniu uprawnień do zdalnego sterowania NVDA + O przesunie ostrość w
/ Poza zdalnie sterowany ekran

Należy pamiętać, że fokus powinien znajdować się na jednej z kontrolek
spotkania, aby móc zdalnie sterować drugim ekranem.

## Ważna uwaga

Funkcja Trybu Użytkownika pozwalająca określić, które alerty mają być
ogłaszane, a które nie, działa tylko wtedy, gdy język interfejsu użytkownika
w programie Zoom jest ustawiony na angielski.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
