# Zoomin saavutettavuusparannukset #

* Tekijät: Mohamad Suliman ja Eilana Benish
* Lataa [vakaa versio][1]
* Yhteensopivuus: NVDA 2018.4-2022.1

Tämä lisäosa parantaa Zoomin käyttökokemusta NVDA-käyttäjille tarjoamalla
pikanäppäimiä eri tapahtumahälytysten käsittelyyn kokouksen aikana,
tekemällä etäkäytöstä paljon helpompaa ja sujuvampaa sekä paljon muuta.

## pikanäppäimet hälytyksien hallintaan kokouksissa

* NVDA+Vaihto+A: vaihtaa eri ilmoitustilojen välillä. Seuraavat tilat ovat
  käytettävissä:

    * Puhu kaikki ilmoitukset: Kaikki ilmoitukset puhutaan tavalliseen
      tapaan.
    * Ilmaise ilmoitukset äänimerkillä: NVDA antaa lyhyen äänimerkin
      jokaisesta Zoomin ilmoituksesta.
    * Hiljennä kaikki ilmoitukset: NVDA ohittaa kaikki ilmoitukset.
    * Mukautettu: Käyttäjä voi mukauttaa, mitä ilmoituksia hän haluaa saada
      ja mitä ei. Tämä voidaan tehdä lisäosan asetusikkunaa tai siihen
      tarkoitettuja pikanäppäimiä käyttäen.

Seuraavia pikanäppäimiä voidaan käyttää kunkin ilmoitustyypin käyttöön
ottamiseen tai käytöstä poistamiseen (huomaa, että tämä toimii vain, kun
mukautettu tila on valittuna):

* NVDA+Ctrl+1: Osallistuja on liittynyt/poistunut kokouksesta (vain isäntä)
* NVDA+Ctrl+2: Osallistuja on liittynyt/poistunut odotushuoneesta (vain
  isäntä)
* NVDA+Ctrl+3: Isäntä mykisti äänen
* NVDA+Ctrl+4: Isäntä lopetti videon
* NVDA+Ctrl+5: Osallistuja aloitti/lopetti näytön jakamisen
* NVDA+Ctrl+6: Tallennuslupa myönnetty/peruutettu
* NVDA+Ctrl+7: Julkinen kokouksen sisäinen keskustelu vastaanotettu
* NVDA+Ctrl+8: Yksityinen kokouksen sisäinen keskustelu vastaanotettu
* NVDA+Ctrl+9: Kokouksen sisäinen tiedostolataus valmis
* NVDA+Ctrl+0: Isäntäoikeus myönnetty/peruutettu
* NVDA+Vaihto+Ctrl+1: Osallistuja on nostanut/laskenut käden (vain isäntä)
* NVDA+Vaihto+Ctrl+2: Etäkäyttöoikeus myönnetty/peruutettu
* NVDA+Vaihto+Ctrl+3: Pikaviestikeskustelu vastaanotettu


Huomaa, että kaikki ilmoitukset on oltava valittuna Zoomin
saavutettavuusasetuksissa, jotta lisäosa toimii odotetulla tavalla.

## Pikanäppäin lisäosan asetusvalintaikkunan avaamiseen

NVDA+Z avaa lisäosan asetusvalintaikkunan

Tätä valintaikkunaa käyttäen voit:

* Katsoa, mitkä ilmoitukset ovat käytössä ja mitkä eivät
* Valita puhuttavien ilmoitusten tyypit
* Valitse ilmoitustila
* Tallenna mukautetut muutokset

## Etäkäyttö

Kun etäkäyttölupa on myönnetty, NVDA+O siirtää kohdistuksen etäkäyttöruutuun
tai siitä pois.

Huomaa, että kohdistuksen tulee olla jonkin kokoussäätimen kohdalla, jotta
etäkäyttö on mahdollista.

## Tärkeä huomautus

Tällä hetkellä mukautettu ilmoitustila, jossa käyttäjä voi valita, mitkä
ilmoitukset hän haluaa saada ja mitkä ei, toimii Zoomin kanssa vain, kun
käyttöliittymän kielenä on englanti.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
