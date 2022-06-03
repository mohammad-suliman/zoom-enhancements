# Zoom Accessibility Enhancements #

* Autori: Mohamad Suliman, Eilana Benish
* Scarica la [versione stabile][1]
* NVDA compatibility: 2018.4 to 2022.1

Questo add-on migliora l'esperienza di utilizzo di Zoom per gli utenti di
NVDA, fornendo comandi da tastiera per gestire, durante una riunione, le
notifiche relative agli eventi che si verificano. rende inoltre il controllo
remoto molto più accessibile e fluido, ecc.

## Comandi da tastiera per controllare le notifiche durante le riunioni 

* NVDA + Shift + A: cicla tra le diverse modalità di leggere le
  notifiche. Sono disponibili le seguenti modalità:

    * Leggi tutte le notifiche, in cui tutte le notifiche sono lette come al
      solito
    * Beep per le notifiche, in cui NVDA emetterà un piccolo beep per ogni
      notifica mostrata in Zoom
    * Silenzia tutte le notifiche, in cui NVDA ignorerà tutte le notifiche
    * Personalizzata, in cui gli utenti possono decidere quali notifiche
      vogliono avere e quali no. Ciò può essere fatto utilizzando la
      finestra impostazioni dell'add-on o i tasti rapidi a ciò dedicati

Per attivare o disattivare la lettura di ciascun tipo di notifica nella
modalità personalizzata, possono essere utilizzati i seguenti tasti:

* NVDA + Ctrl + 1: NomePartecipante è entrato / uscito dalla riunione (solo
  per l'organizzatore)
* NVDA + Ctrl + 2: NomePartecipante è entrato / uscito dalla sala di attesa
  (solo per l'organizzatore)
* NVDA + Ctrl + 3: microfono disattivato dall'organizzatore
* NVDA + Ctrl + 4: video disattivato dall'organizzatore
* NVDA + Ctrl + 5: condivisione schermo avviata / interrotta da un
  partecipante
* NVDA + Ctrl + 6: autorizzato / revocato il permesso di registrare
* NVDA + Ctrl + 7: ricevuto messaggio pubblico
* NVDA + Ctrl + 8: ricevuto messaggio privato
* NVDA + Ctrl + 9: caricamento file completato
* NVDA + Ctrl + 0: autorizzati / revocati i privilegi di organizzatore
* NVDA + Shift + Ctrl + 1: NomeParticipante ha alzato / abbassato la mano
  (solo per l'organizzatore)
* NVDA + Shift + Ctrl + 2: autorizzato / revocato il permesso di controllare
  da remoto
* NVDA + Shift + Ctrl + 3: ricevuto messaggio di chat


Notate che dovrete lasciare selezionata la lettura di tutti i tipi di
notifiche (nelle impostazioni di accessibilità di Zoom) affinché l'add-on
funzioni come previsto.

## Comandi da tastiera per aprire la finestra dell'add-on 

NVDA + Z apre la finestra dell'add-on !

Da questa finestra potete:

* Vedere quali notifiche sono lette e quali no
* Selezionare i tipi di notifiche che volete siano lette
* Scegliere la modalità di lettura delle notifiche
* Salvare le modifiche

## Controllo remoto 

Dopo che è stato accordato il permesso per il controllo remoto, NVDA + O
sposterà il focus dentro o fuori lo schermo controllato a distanza

Notate che il focus deve essere su uno dei controlli della riunione per
poter controllare l'altro schermo

## Nota importante

Al momento la modalità notifiche personalizzata, nella quale gli utenti
possono scegliere quali notifiche avere e quali no, funziona con Zoom solo
quando la lingua dell'interfaccia utente è impostata su inglese.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
