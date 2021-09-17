# Tilgængelighedsforbedringer i Zoom #

* Forfattere: Mohamad Suliman, Eilana Benish
* Download [stabil version][1]
* NVDA -kompatibilitet: 2018.4 til 2020.2

Denne tilføjelse forbedrer brugen af Zoom for NVDA-brugere ved at tilbyde
tastaturgenveje til at håndtere advarsler for forskellige begivenheder, mens
du er i et møde, gør processen med fjernbetjening meget mere tilgængelig og
nemmere, m.m.

## tastaturgenveje til styring af meddelelser i møder

* NVDA+Shift+A: Skifter mellem de forskellige måder, hvorpå du kan få
  meddelelser oplyst. Følgende tilstande er tilgængelige:

    * Oplys alle meddelelser, hvor alle meddelelser rapporteres som normalt
    * Bip for meddelelser, hvor NVDA vil bippe, hver gang en meddelelse
      vises i Zoom
    * Ignorér alle meddelelser, hvor NVDA ignorere alle meddelelser
    * Tilpasset tilstand, hvor brugeren kan tilpasse, hvilke meddelelser de
      vil have oplyst. Dette kan gøres ved hjælp af indstillingsdialogen i
      tilføjelsen eller ved at bruge de særlige tastaturgenveje

Følgende genveje kan bruges til at slå meddelelser om hver meddelelsestype
til / fra (bemærk, at dette kun fungerer, når tilpasset tilstand er valgt):

* NVDA+Ctrl+1: Deltager deltager nu i mødet eller forlod møde (kun vært)
* NVDA+Ctrl+2: Deltager deltager eller har forladt venteværelse (kun vært)
* NVDA+Ctrl+3: Lyd dæmpet af vært
* NVDA+Ctrl+4: Video stoppet af vært
* NVDA+Ctrl+5: Skærmdeling startet/stoppet af en deltager
* NVDA+Ctrl+6: Optagelsestilladelse givet/tilbagekaldt
* NVDA+Ctrl+7: Offentlig chat i møde modtaget
* NVDA+Ctrl+8: Privat chat i møde modtaget
* NVDA+Ctrl+9: Filoverførsel i møde afsluttet
* NVDA+Ctrl+0: Værtsrolle tildelt/tilbagekaldt
* NVDA+Shift+Ctrl+ 1: Deltageren har løftet/sænket hånden (kun vært)
* NVDA+Shift+Ctrl+2: Tilladelse til fjernstyring givet/tilbagekaldt
* NVDA+Shift+Ctrl+3: IM chatbesked modtaget


Bemærk, at du skal lade "Oplys alle meddelelser" være markeret (i Zoom
Accessibility Settings) for at have tilføjelsesfunktionen fungere som
forventet.

## Tastaturgenvej til at åbne tilføjelsesindstillingerne

NVDA+Z Åbner tilføjelsesdialogboksen!

Ved hjælp af denne dialog kan du:

* Se, hvilke meddelelser der annonceres
* Vælg de typer af meddelelser, der skal oplyses
* Vælg tilstand for meddelelser
* Gem tilpassede ændringer

## Fjernstyring

Efter tilladelse til fjernstyring er givet, vil NVDA+O flytte fokus ind/ud
af den fjernstyrede skærm

Bemærk, at fokus skal være på en af mødekontrollerne for at kunne
fjernbetjene den anden skærm

## En vigtig bemærkning

I øjeblikket er funktionen for tilpassede meddelelsestyper, hvor brugeren
kan vælge, hvilke meddelelser de vil have kun tilgængelig, når
brugergrænsefladesproget er indstillet til engelsk i Zoom.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
