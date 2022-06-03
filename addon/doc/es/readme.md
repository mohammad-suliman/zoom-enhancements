# Mejoras de accesibilidad para Zoom #

* Autores: Mohamad Suliman, Eilana Benish
* Descargar [versión estable][1]
* Compatibilidad con NVDA: de 2018.4 a 2022.1

Este complemento mejora la experiencia de usuario al utilizar Zoom con NVDA
proporcionando atajos de teclado para gestionar las alertas de eventos
durante una reunión, haciendo el proceso de control remoto más accesible y
fluido, y mucho más.

## atajos de teclado para controlar alertas durante una reunión 

* NVDA+shift+a: alterna entre los distintos modos de anuncio de alertas. Los
  modos disponibles son:

    * Modo anunciar todas las alertas, donde se anuncian todas las alertas
      como siempre
    * Pitar en cada alerta: NVDA emitirá un breve pitido cada vez que Zoom
      emita una alerta
    * Silenciar alertas: NVDA ignorará todas las alertas
    * Modo personalizado, donde el usuario elige qué alertas quiere y cuáles
      no. Esto se puede hacer desde el diálogo de opciones del complemento,
      o utilizando los atajos de teclado dedicados a tal efecto

Los siguientes atajos se pueden usar para activar o desactivar el anuncio de
cada tipo de alerta (ten en cuenta que sólo tendrán efecto cuando se
seleccione el modo personalizado):

* NVDA+ctrl+1: un participante se ha unido o ha abandonado la reunión (sólo
  anfitrión)
* NVDA+ctrl+2: un participante se ha unido o ha abandonado la sala de espera
  (sólo anfitrión)
* NVDA+ctrl+3: audio silenciado por el anfitrión
* NVDA+ctrl+4: vídeo detenido por el anfitrión
* NVDA+ctrl+5: un participante comparte o deja de compartir pantalla
* NVDA+ctrl+6: permiso para grabar concedido o revocado
* NVDA+ctrl+7: chat público recibido
* NVDA+ctrl+8: chat privado recibido
* NVDA+ctrl+9: subida de archivos a la reunión completada
* NVDA+ctrl+0: privilegio de anfitrión concedido o revocado
* NVDA+ctrl+shift+1: un participante ha levantado o bajado la mano (sólo
  anfitrión)
* NVDA+ctrl+shift+2: permiso de control remoto concedido o revocado
* NVDA+ctrl+shift+3: mensaje de chat recibido


Ten en cuenta que deberás dejar activados los anuncios de todos los tipos de
alertas en las opciones de accesibilidad de Zoom para que el complemento
funcione como se espera.

## Atajo de teclado para abrir el diálogo de opciones del complemento 

¡NVDA+z abre el diálogo del complemento!

Usando este diálogo puedes:

* Ver qué alertas se anuncian y cuáles no
* Seleccionar los tipos de alertas que quieres que se anuncien
* Elegir el modo de anuncio de alertas
* Guardar cambios personalizados

## Control remoto 

después de que se conceda permiso de control remoto, NVDA+o situará el foco
en la pantalla controlada o lo sacará de allí

Ten en cuenta que el foco debe estar situado en uno de los controles de la
reunión para poder controlar la otra pantalla

## Nota importante

Actualmente, la función de modo de alertas personalizadas, en las que el
usuario puede elegir qué alertas quiere tener y cuáles no, sólo funciona con
Zoom cuando el idioma de la interfaz de usuario se ha configurado en inglés.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
