# Zoom Accessibility Enhancements #

* Autores: Mohamad Suliman, Eilana Benish
* Descargar [versión estable][1]
* NVDA compatibility: 2018.4 to 2022.1

Este complemento mellora a experiencia de usar Zoom para usuarios do NVDA
fornecendo atallos de teclas para manexar alertas para diferentes eventos
durante unha reunión, facendo o proceso de control remoto moito máis
accesible e amigable, e máis.

## atallos de teclas para controlar alertas en reunións 

* NVDA + Shift + A: Cambia ciclicamente entre diferentes modos de anunciar
  alertas. Están dispoñibles os seguintes modos:

    * Modo de Anunciar tódalas alertas (Report all alerts), no que tódalas
      alertas se reportan coma sempre
    * Pitar para alertas (Beep for alerts), no que NVDA reproducirá un
      pitido curto para cada alerta que se amose en Zoom
    * Silenciar tódalas alertas (Silence all alerts), no que NVDA ignorará
      tódalas alertas
    * Modo Persoalizado (Custom), no que o usuario pode persoalizar as
      alertas que quere ter e as que non. Isto pode facerse utilizando o
      diálogo de opcións do complemento, ou utilizando os atallos de teclas
      dedicados para tal fin

Os seguintes atallos de teclas pódense usar para activar/desactivar os
anuncios de cada tipo de alerta (ten en conta que isto será efectivo cando
estea seleccionado o modo persoalizado):

* NVDA + Ctrl + 1: O Participante Uniuse/Abandoou a Conferencia (Só
  anfitrión)
* NVDA + Ctrl + 2: O participante Uniuse/Abandoou a Sala de Agarda (Só
  anfitrión)
* NVDA + Ctrl + 3: Audio Silenciado polo Anfitrión
* NVDA + Ctrl + 4: Vídeo Detido polo Anfitrión
* NVDA + Ctrl + 5: Compartir Pantalla Iniciado/Detido por un Participante
* NVDA + Ctrl + 6: Permiso de gravación Concedido/Revogado
* NVDA + Ctrl + 7: Recibido Chat Público na Reunión
* NVDA + Ctrl + 8: Recibido Chat Privado na Reunión
* NVDA + Ctrl + 9: Subida de Arquivo na Reunión Completada
* NVDA + Ctrl + 0: Permiso de Anfitrión Concedido/Revogado
* NVDA + Shift + Ctrl + 1: Un Participante Levantou/Baixou a man (Só
  Anfitrión)
* NVDA + Shift + Ctrl + 2: Permiso de Control Remoto Concedido/Revogado
* NVDA + Shift + Ctrl + 3: Recivida Mensaxe polo Chat IM/MI


Ten en conta que debes deixar seleccionado o anuncio de tódolos tipos de
alertas (nas opcións de accesibilidade do Zoom) para que o complementeo
funcione como se espera.

## Atallo de teclas para abrir o diálogo do complemento 

NVDA + Z Abre o diálogo do complemento !

Neste diálogo podes:

* Ver que alertas se anuncian e cales non
* Seleccionar os tipos de alertas que queres que se anuncien
* Escoller o modo de anunciado de alertas
* Gardar os cambios persoalizados

## Control remoto 

unha vez concedido un permiso de control remoto, NVDA + O moverá o foco
dentro/fóra da pantalla remotamente controlada

Ten en conta que o foco debería estar nun dos controis da reunión para que
sexa posible controlar remotamente a outra pantalla

## Unha nota Importante

Actualmente as características do modo persoalizado no que o usuario pode
escoller que alertas queren ter e cales non funcionan con Zoom só cando o
idioma da interface de usuario está configurado en inglés.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
