# Barrierefreie Zoom-Verbesserung #

* Autoren: Mohamad Suliman, Eilana Benish
* [Stabile Version herunterladen][1]
* NVDA-Kompatibilität: 2018.4 bis 2022.1

Diese Erweiterung verbessert die Erfahrung mit Zoom für Nutzerinnen und
Nutzer von NVDA, in dem Tastenkombinationen für Benachrichtigungen bei
verschiedenen Ereignissen zur Verfügung gestellt werden. Der Prozess der
Fernsteuerung wird dadurch bedienbarer und vieles mehr.

## Tastenkombinationen zur Kontrolle von Ereignis-Benachrichtigungen

* NVDA+Umschalt+A: Wechselt zwischen mehreren Modi der
  Benachrichtigungen. Die folgenden Modi sind verfügbar:

    * Alle Benachrichtigungen mitteilen: Hier werden wie voreingestellt alle
      Benachrichtigungen mitgeteilt
    * Piepton bei Benachrichtigung: Für jede Benachrichtigung, die Zoom
      anzeigt, wird ein Piepton ausgegeben
    * Alle Benachrichtigungen stummschalten: Hier ignoriert NVDA alle
      Benachrichtigungen
    * Eigene Auswahl: Hier kann die Nutzerin oder der Nutzer selbst
      festlegen, über welche Benachrichtigungen er oder sie informiert
      werden möchte und welche ignoriert werden sollen. Dies kann im
      Einstellungs-Dialogfeld der Erweiterung oder über die entsprechende
      Tastenkombination festgelegt werden

Die folgenden Tastenkombinationen stehen zur Verfügung, um die Mitteilung
von Benachrichtigungsarten ein- oder auszuschalten, sofern der Modus
"persönliche Auswahl" aktiviert ist:

* NVDA+Strg+1: Teilnehmer hat das Meeting betreten/verlassen (nur
  Veranstalter)
* NVDA+Strg+2: Teilnehmer hat den Wartebereich betreten/verlassen (nur
  Veranstalter)
* NVDA+Strg+3: Audio durch den Veranstalter stummgeschaltet
* NVDA+Strg+4: Video durch den Veranstalter gestoppt
* NVDA+Strg+5: Bildschirm-Freigabe durch Teilnehmer gestartet/gestoppt
* NVDA+Strg+6: Aufzeichnungsgenehmigung gewährt oder widerrufen
* NVDA+Strg +7: Öffentliche Chat-Nachricht (während einer Veranstaltung)
  erhalten
* NVDA+Strg+8: Private Chat-Nachricht (während einer Veranstaltung) erhalten
* NVDA+Strg+9: Datei innerhalb der Veranstaltung hochgeladen
* NVDA+Strg+0: Ernennung zum Veranstalter gewährt oder widerrufen
* NVDA+Umschalt+Strg+1: Teilnehmer hat die Hand gehoben/gesenkt (nur
  Veranstalter)
* NVDA+Umschalt+Strg+2: Fernsteuerungsgenehmigung gewährt oder widerrufen
  (nur Veranstalter)
* NVDA+Umschalt+Strg+3: Chat-Nachricht innerhalb des Meetings erhalten


Beachten Sie, dass in den Zoom-Einstellungen alle Meldungen aktiviert sein
müssen, damit die Erweiterung richtig funktioniert.

## Tastenkürzel um den Dialog der Erweiterung aufzurufen

NVDA+Z öffnet den Dialog der Erweiterung!

In diesem Dialog können Sie:

* Feststellen, welche Benachrichtigungen mitgeteilt oder nicht mitgeteilt
  werden
* Wählen Sie die Benachrichtigungsarten aus, über die Sie informiert werden
  möchten
* Wählen Sie den Benachrichtigungsmodus aus
* Benutzerdefinierte Änderungen speichern

## Fernsteuerung

Sofern man eine Fernsteuerungsgenehmigung erhalten hat, bewegt NVDA+O den
Fokus in und aus dem zu kontrollierenden Bildschirm

Bitte beachten Sie, dass der Fokus auf einem Meeting-Element sein sollte,
damit Sie einen anderen Bildschirm fernsteuern können

## Wichtiger Hinweis

Momentan funktioniert das Feature der benutzerspezifischen Auswahl der
Benachrichtigungen nur, bei dem der/die Nutzer/in selbst festlegen kann,
welche Benachrichtigungen er/sie erhalten möchte, wenn die Sprache von Zoom
auf Englisch eingestellt ist.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
