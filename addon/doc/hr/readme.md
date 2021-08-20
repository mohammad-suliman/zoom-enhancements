# Poboljšanja pristupačnosti za Zoom (Zoom Accessibility Enhancements) #

* Autori: Mohamad Suliman, Eilana Benish
* Preuzmi [stabilnu verziju][1]
* NVDA kompatibilnost: od 2018.4 do 2020.2

Ovaj dodatak pomaže korisnicima NVDA čitača koristiti Zoom. Omogućuje
upotrebu tipkovničkih prečaca za upozorenja za razne događaje tijekom
sastanka, poboljšava i pojednostavljuje daljinsko upravljanje i još mnogo
toga.

## Tipkovnički prečaci za upravljanje upozorenjima u sastancima

* NVDA + šift + A: mijenja između različitih načina izvještavanja o
  upozorenjima. Dostupni su sljedeći načini:

    * Javi sve načine upozorenja. Sva se upozorenja izvještavaju kao i
      obično
    * Sviraj zvučni signal za upozorenja. NVDA će odsvirati kratki zvučni
      signal za svako upozorenje prikazano u Zoom-u
    * Isključi zvučni signal za sva upozorenja. NVDA će zanemariti sva
      upozorenja
    * Prilagođeni način. Korisnik može odrediti upozorenja koja će se
      koristiti. To se može učiniti pomoću dijaloškog okvira za postavke
      dodatka ili pomoću posebnih tipkovnih prečaca

Sljedeći prečaci mogu se koristiti za uključivanje/isključivanje najava svih
vrsta upozorenja (prečaci se koriste kad se odabere prilagođeni način rada):

* NVDA + kontrol + 1: Sudionik se pridružio ili je napustio sastanak (samo
  voditelj)
* NVDA + kontrol + 2: Sudionik se pridružio ili je napustio čekaonicu (samo
  voditelj)
* NVDA + kontrol + 3: Voditelj je isključio zvuk
* NVDA + kontrol + 4: Voditelj je prekinuo videosnimku
* NVDA + kontrol + 5: Sudionik je pokrenuo/prekinuo dijeljenje ekrana
* NVDA + kontrol + 6: Dozvola za snimanje odobrena/opozvana
* NVDA + kontrol + 7: Primljen je javni razgovor u sastanku
* NVDA + kontrol + 8: Primljen je privatni razgovor u sastanku
* NVDA + kontrol + 9: Dovršen prijenos datoteke u sastanku
* NVDA + kontrol + 0: Prava voditelja odobrena/opozvana
* NVDA + šift + kontrol + 1: Sudionik je dignuo/spusito ruku (samo voditelj)
* NVDA + šift + kontrol + 2: Dozvola za daljinsko upravljanje
  odobrena/opozvana
* NVDA + šift + kontrol + 3: Primljena je poruka u sastanku


Za dobivanje očekivane funkciju dodatka, sve vrste upozorenja moraju biti
odabrane (u Zoom postavkama pristupačnosti).

## Tipkovnički prečac za otvaranje dijaloškog okvira dodatka

NVDA + Z: Otvara dijaloški okvir dodatka!

Pomoću ovog dijaloškog okvira, moguće je:

* Saznati koja se upozorenja najavljuju, a koja ne
* Odabrati vrste upozorenja koja se najavljuju
* Odabrati način izvještavanja o upozorenjima
* Spremiti prilagođene promjene

## Daljinsko upravljanje

nakon odobrenja daljinskog upravljanja, NVDA + O će premjestiti fokus u/iz
daljinski upravljenog ekrana

Napomena: fokus bi trebao biti jedan od kontrola sastanka, kako bi se moglo
upravljati drugim ekranom

## Važna napomena

Trenutačno, funkcija za prilagođena upozorenja, u kojem korisnik može
odabrati željena upozorenja, funkcionira sa Zoomom samo kad je jezik
korisničkog sučelja postavljen na engleski.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
