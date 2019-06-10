# Odaif

Projeto implementado para a discipla DCA0120 - Projeto e Desenvolvimento de Software no sementre 2019.1

## Servidor

O servidor implementado foi uma especialização de um servidor HTTP, que lida com requisições feitas em duas rotas, sendo elas a rota /buy que aqui representa uma solicitação de compra do usuário, o servidor ao receber esta solicitação realizará a geração de um QRCode representando a reserva e o enviará ao usuário apresentando também uma mensagem de sucesso se todo o processo descrito foi bem sucedido ademais a rota /deliver modela o comportamento do sistema durante a entrega de uma reserva sendo assim o servidor fica aguardando a leitura do código de reserva para validar a entrega do pedido.

A utilização do servidor pode ser feita da seguinte forma, substituindo IP pelo IP do computador:

```console
user@computer:~/odaif $ python server.py IP
Server is running on IP ...
```

## Interface do usuário

A interface de usuário é a responsável por enviar as requisições cabíveis a depender da ação que o usuário deseja tomar, sendo assim será mostrada a mensagem “What to do?:” instruindo o usuário a inserir a ação que deseja executar sendo suportada as seguintes ações: buy que realizará a solicitação de compra ao servidor e receberá o QRCode da reserva e a ação deliver que é responsável por mostrar o QRCode da reserva para leitura e receber a resposta do servidor quando a leitura é feita. Ao fim de cada ação o programa será redirecionado para a mensagem “What to do?:” mostrando a que ação anterior foi realizada e uma nova pode ser feita.

```console
user@computer:~/odaif $ python odaif.py

What to do:
```
