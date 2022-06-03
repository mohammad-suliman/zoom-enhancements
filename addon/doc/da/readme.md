# Tilgængelighedsforbedringer i Zoom #

* Forfattere: Mohamad Suliman, Eilana Benish
* Download [stabil version][1]
* NVDA compatibility: 2018.4 to 2022.1

Denne tilføjelse forbedrer brugen af Zoom for NVDA-brugere ved at tilbyde
tastaturgenveje til at håndtere meddelelser for forskellige hændelser, mens
du er i et møde. Tilføjelsen forbedre også processen med fjernstyring og gør
denne meget mere tilgængelig og nemmere, m.m.

## tastaturgenveje til styring af meddelelser i møder

* NVDA+Shift+A: Skifter mellem de forskellige måder, hvorpå du kan få
  meddelelser oplyst. Følgende tilstande er tilgængelige:

    * Oplys alle hændelser, hvor alle hændelser oplyses som normalt
    * Bip for hændelser, hvor NVDA vil bippe, hver gang en hændelse vises i
      Zoom
    * Ignorér alle hændelser, hvor NVDA ignorere alle hændelser
    * Tilpasset tilstand, hvor brugeren kan tilpasse, hvilke hændelser, der
      skal oplyses. Dette kan gøres ved hjælp af indstillingsdialogen i
      tilføjelsen eller ved at bruge de særlige tastaturgenveje

Følgende genveje kan bruges til at slå hver hændelsestype til / fra (bemærk,
at dette kun fungerer, når tilpasset tilstand er valgt):

* NVDA+Ctrl+1: Deltager deltager nu i mødet eller forlod møde (kun vært)
* NVDA+Ctrl+2: Deltager deltager eller har forladt venteværelse (kun vært)
* NVDA+Ctrl+3: Lyd slået til eller fra af vært
* NVDA+Ctrl+4: Video stoppet af vært
* NVDA+Ctrl+5: Skærmdeling startet/stoppet af en deltager
* NVDA+Ctrl+6: Optagelsestilladelse givet/tilbagekaldt
* NVDA+Ctrl+7: Offentlig chat i møde modtaget
* NVDA+Ctrl+8: Privat chat i møde modtaget
* NVDA+Ctrl+9: Filoverførsel i møde afsluttet
* NVDA+Ctrl+0: Værtsrolle tildelt/tilbagekaldt
* NVDA+Shift+Ctrl+ 1: Deltageren har løftet/sænket hånden (kun vært)
* NVDA+Shift+Ctrl+2: Tilladelse til fjernstyring givet/tilbagekaldt
* NVDA+Shift+Ctrl+3: IM-chatbesked modtaget


Bemærk, at du skal lade "Oplys alle hændelser" være markeret i Indstillinger
for zoom-forbedringer, før tilføjelsen fungere som forventet.

## Tastaturgenvej til at åbne tilføjelsesindstillingerne

NVDA+Z: Viser dialogboksen Indstillinger for Zoom-forbedringer

Ved hjælp af denne dialog kan du:

* Se, hvilke hændelser der oplyses
* Vælg de hændelser, der skal oplyses
* Vælg tilstand for hændelser
* Gem tilpassede ændringer

## Fjernstyring

Efter tilladelse til fjernstyring er givet, vil NVDA+O flytte fokus til
eller væk fra den fjernstyrede skærm

Bemærk, at fokus skal være på en af mødekontrollerne for at kunne fjernstyre
den anden skærm

## En vigtig bemærkning

I øjeblikket er funktionen for tilpassede hændelser, hvor brugeren kan
vælge, hvilke hændelser de vil have oplyst kun tilgængelig, når
brugergrænsefladesproget er indstillet til engelsk i Zoom.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
