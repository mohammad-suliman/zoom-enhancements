# Verbesserung für Zoom-Barrierefreiheit #

* Autoren: Mohamad Suliman, Eilana Benish
* [Stabile Version herunterladen][1]
* NVDA-Kompatibilität: 2018.4 bis 2020.2

Diese Erweiterung verbessert die Zoom-Erfahrung für NVDA-Nutzer in dem
Tastenkombinationen für Meldungen bei verschiedenen Veranstaltungen zur
Verfügung gestellt werden, der Prozess der Fernsteuerung wird viel
bedienbarer und mehr.

## Tastenkombinationen zur Kontrolle von Meldungen in Veranstaltungen 

* NVDA+Umschalt+A: Wechselt zwischen mehreren Modi zur Meldungs-Ansage. Die
  folgenden Modi sind verfügbar:

    * Alle Meldungen ansagen: Hier werden wie voreingestellt alle Meldungen
      angesagt
    * Piepton bei Meldungen: Für jede Meldung, die Zoom anzeigt, wird ein
      Piepton ausgegeben
    * Alle Meldungen stummschalten: Hier ignoriert NVDA alle Meldungen
    * Eigene Auswahl: Hier kann der Nutzer selbst festlegen, über weelche
      Meldungen er informiert werden möchte und welche ignoriert werden
      sollen. Dies kann im Einstellungs-Dialog der Erweiterung oder über die
      entsprechende Tastenkombination festgelegt werden

Die folgenden Tastenkombinationen stehen zur Verfügung, um die Ansage von
Meldungstypen ein- oder auszuschalten, sofern der Modus "persönliche
Auswahl" aktiviert ist:

* NVDA+Strg+1: Teilnehmer hat die Besprechung betreten/verlassen (nur
  Veranstalter)
* NVDA+Strg+2: Teilnehmer hat den Warteraum betreten/verlassen (nur
  Veranstalter)
* NVDA+Strg+3: Ton durch den Veranstalter stummgeschalten
* NVDA+Strg+4: Video durch den Veranstalter gestoppt
* NVDA+Strg+5: Bildschirm teilen durch einen Teilnehmer gestartet/gestoppt
* NVDA+Strg+6: Erlaubnis zur Aufname genehmigt/untersagt
* NVDA+Strg +7: Öffentliche Chat-Nachricht (in einer Veranstaltung) erhalten
* NVDA+Strg+8: Private Chat-Nachricht (innerhalb der Veranstaltung) erhalten
* NVDA+Strg+9: Datei innerhalb der Veranstaltung hochgeladen
* NVDA+Strg+0: Ernennung zum Veranstalter erhalten/zurückgezogen
* NVDA+Umschalt+Strg+1: Teilnehmer hat die Hand gehoben/gesenkt (nur
  Veranstalter)
* NVDA+Umschalt+Strg+2: Genehmigung der Fernsteuerung erhalten/zurückgezogen
  (nur Veranstalter)
* NVDA+Umschalt+Strg+3: Direkt-chat-nachricht erhalten


Beachten Sie, dass in den Zoom-Einstellungen alle Meldungen aktiviert sein
müssen, damit die Erweiterung richtig funktioniert.

## Tastenkürzel um den Dialog der Erweiterung aufzurufen 

NVDA+Z öffnet den Dialog der Erweiterung!

In diesem Dialog können Sie:

* Feststellen, welche Meldungen angesagt oder nicht angesagt werden
* Wählen Sie die Meldungstüpen, über welche Sie informiert werden wollen
* Wähle auszugebende Meldungen
* Persönliche Änderungen speichern

## Fernsteuerung 

Sofern man eine Steuerungs-Erlaubnis erhalten hat, bewegt NVDA+o den Fokus
in und aus dem zu kontrollierenden Bildschirm

Bitte beachten Sie, dass der Fokus auf einem Meeting-Element sein sollte,
damit Sie einen anderen Bildschirm fernsteuern können

## Wichtiger Hinweis

Momentan funktioniert das Feature der benutzerspezifischen Meldungsauswahl,
bei dem der Nutzer selbst festlegen kann, welche Meldungen er mitbekommen
möchte nur, wenn die Sprache von Zoom auf Englisch eingestellt ist.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
