# Melhorias na acessibilidade do  Zoom #

* Autores: Mohamad Suliman, Eilana Benish
* Baixar [Versão estável][1]
* Compatibilidade com o NVDA: 2018.4 a 2020.2

Este extra melhora a experiência de utilização do Zoom para utilizadores do
NVDA ao fornecer atalhos de teclado para tratar alertas para diferentes
eventos Enquanto estiver numa reunião, torna o processo de controlo remoto
muito mais acessível e mais suave, e ainda mais.

## atalhos de teclado para controlo de alertas Em reuniões

* NVDA + Shift + A: alterna entre diferentes modos de notificação de
  alertas. Estão disponíveis os seguintes modos:

    * Indicar todos os modos de alerta, onde todos os alertas são indicados,
      como habitualmente
    * Bip para alertas, onde o NVDA emitirá um curto sinal sonoro para cada
      alerta apresentado no Zoom
    * Silenciar todos os alertas, onde a NVDA ignorará todos os alertas
    * Modo personalizado, onde o utilizador pode personalizar quais os
      alertas que quer e quais não quer ter. Isto pode ser feito usando o
      diálogo de configurações do extra, ou usando os atalhos de teclado
      dedicados para esse efeito

Os seguintes atalhos podem ser usados para ligar/desligar os anúncios de
cada tipo de alerta (note que isto será eficaz quando o modo personalizado
for seleccionado):

* NVDA + Ctrl + 1: Participante entrou/saiu da Reunião (Apenas anfitrião)
* NVDA + Ctrl + 2: Participante entrou/saiu da Sala de Espera (Apenas
  anfitrião)
* NVDA + Ctrl + 3: Áudio silenciado por anfitrião
* NVDA + Ctrl + 4: Vídeo Parado pelo Anfitrião
* NVDA + Ctrl + 5: Partilha de ecrã iniciada/terminada por um Participante
* NVDA + Ctrl + 6: Permissão de Gravação Concedida/Revogada
* NVDA + Ctrl + 7: Recebida Conversa Pública na Reunião
* NVDA + Ctrl + 8: Recebida Conversa Privada na Reunião
* NVDA + Ctrl + 9: Carregamento de ficheiro da reunião Completo
* NVDA + Ctrl + 0: Privilégio de anfitrião dado/retirado.
* NVDA + Shift + Ctrl + 1: Participante Levantou/baixou a Mão (Apenas
  anfitrião)
* NVDA + Shift + Ctrl + 2: Autorização de Controlo Remoto Concedida/Revogada
* NVDA + Shift + Ctrl + 3: Recebida mensagem interna da conversa.


Note que é necessário deixar todos os tipos de alerta seleccionados (em
configurações de acessibilidade do Zoom) para ter as funcionalidades do
extra, como se encontram descritas.

## Atalho de teclado para a abertura do Diálogo do extra

NVDA + Z Abre o diálogo do extra!

Ao Usar este diálogo, pode :

* Ver quais os alertas que são anunciados e quais não são
* Seleccionar os tipos de alertas que pretende que sejam anunciados
* Escolher o modo de indicação de alertas
* Guardar alterações personalizadas

## Controlo remoto

após a concessão de uma autorização de controlo remoto, o NVDA + O deslocará
o foco para dentro / fora do ecrã do controlo remoto

Note que o foco deve estar num dos controlos da reunião para poder
controlar, à distância, o outro ecrã

## Uma nota importante

Actualmente a funcionalidade do modo de alertas personalizados onde o
utilizador pode escolher quais os alertas que quer ter e quais os que não
funcionam com o Zoom funciona apenas quando a interface do utilizador está
definida para inglês.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
