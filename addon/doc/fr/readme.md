# Zoom Accessibility Enhancements #

* Auteurs : Mohamad Suliman, Eilana Benish
* Télécharger [version stable][1]
* NVDA compatibility: 2018.4 to 2022.1

Cette extension améliore l'expérience utilisateur lors de l'utilisation de
Zoom avec NVDA fournissant des raccourcis clavier pour gérer les alertes
d'événements au cours d'une réunion, ce qui rend le processus de contrôle à
distance plus accessible et fluide, et bien plus encore.

## Raccourcis clavier pour le contrôle des alertes au cours d'une réunion 

* NVDA+maj+a: basculant entre les différents modes d'annonce des
  alertes. Les modes disponibles sont:

    * Mode annoncer toutes les alertes, où toutes les alertes sont annoncés
      comme d'habitude
    * Émettre un bip  à chaque alerte: NVDA émettra un petit "bip" chaque
      fois  que Zoom émet une alerte
    * Couper les alertes: NVDA ignorera toutes les alertes
    * Mode personnalisé, où l'utilisateur peut choisir quelles alertes
      souhaite et lesquels non. Cela peut être fait à partir du dialogue
      Paramètres de l'extension, ou en utilisant les raccourcis clavier
      dédiés à cet effet

Les raccourcis clavier suivants peuvent être utilisés pour activer ou
désactiver l'annonce de chaque type d'alerte (notez que ne prennent effet
que lorsque vous sélectionnez le Mode personnalisé):

* NVDA+Ctrl+1: un participant a rejoint ou quitté la réunion (hôte
  uniquement)
* NVDA+Ctrl+2: un participant a rejoint ou quitté la salle d'attente (hôte
  uniquement)
* NVDA+Ctrl+3: audio coupé par l'hôte
* NVDA+Ctrl+4: vidéo interrompue par l'hôte
* NVDA+Ctrl+5: un participant partage  ou a laissé de partager l'écran
* NVDA+Ctrl+6: autorisation d'enregistrement accordée ou révoquée
* NVDA+Ctrl+7: discussion publique reçu
* NVDA+Ctrl+8: discussion privée reçu
* NVDA+Ctrl+9: transfert de fichiers de la réunion terminée
* NVDA+Ctrl+0: privilèges d'hôte accordé ou révoqué
* NVDA+Ctrl+maj+1: un participant a soulevé  ou Abaissé la main (hôte
  uniquement)
* NVDA+Ctrl+maj+2: autorisation de contrôle à distance accordé ou révoqué
* NVDA+Ctrl+maj+3: message de discussion reçu


Notez que vous devez laisser activé les annonces de tous les types d'alertes
dans le dialogue Paramètres Accessibilité de Zoom pour que l'extension
fonctionne comme prévu.

## Raccourci clavier pour ouvrir le dialogue Paramètres de l'extension 

NVDA+z ouvre le dialogue de l'extension!

En utilisant ce dialogue, vous pouvez:

* Voir quelles alertes sont annoncées et et lesquels non
* Sélectionner les types des alertes que vous souhaitez annoncer
* Choisir le mode d'annonce des alertes
* Enregistrer les changements personnalisées

## Contrôle à distance 

Après avoir accordé l'autorisation du contrôle à distance, NVDA+o mettra le
focus sur l'écran contrôlée ou le sortira de là

Notez que  le focus doit être mis sur l'un des contrôles de la réunion afin
de contrôler l'autre écran

## Une remarque importante

Actuellement, la fonction du mode d'alertes personnalisés où l'utilisateur
peut choisir quelles alertes souhaite et lesquels ne souhaite pas voir
fonctionner avec Zoom uniquement lorsque la langue de l'interface
utilisateur est l'anglais

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
