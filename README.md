# Baralla

(Baralla em galego da Galícia, na Espanha, significa baralho da cartas.)

O objetivo deste projeto é reunir desenvolvimentos e testes de ideias de códigos fonte que sirvam de base para desenvolvimento de jogos de cartas.

### Fechada Versão 0.1 - Executar jogo

2023-12-13

Até aqui foram desenvolvidas uma coleção de classes para simular um jogo de cartas. Está inicialmente pensado para atender a vários jogos, mas esse pré-requisito ainda está bem flexível.

As classes que descrevem os jogos ainda são altamente voltadas para informação, porém alguns parâmetros já saem de dados encontrados nelas.

Ao executar teste.py, que testa toda a estrutura, um jogo de brisca é jogado entre 2 jogadores, até um dos jogadores ganhar quatro partidas, sendo assim o vencedor do jogo.

A única regra da Brisca não atendida é a de uma pontuação alta da partida valer por duas partidas.

Diversos outputs de estados parciais são feitos pelo script para verificarmos o funcionamento.

A lógica de jogo da classe jogador é, até aqui, apenas a escolha aleatória de uma das cartas da mão. (lógica "0.10.0")

Executando 10 mil vezes um dos jogadores ganhou 51,87%, ficando perto do esperado 50%.

Criada lógica "0.10.1", em que o jogado pega sempre a carta que esta na mão há mais tempo. Isso, como a lógica anterior, também resulta em um jogo completamente aleatório, afinal as cartas são embaralhadas.

### Fechada Versão 0.11.0

Heurística:
- Como primeiro jogador da mão: sorteia uma carta
- Como segundo: escolhe carta maior que a da mesa, se tiver, senão sorteia

Performance:
- contra 0.10.0: 84,2% de vitórias
- contra 0.10.1: 82,6% de vitórias
- contra si próprio: 50,3% de vitórias

Resultados equivalentes. Então sempre a comparação com a abordagem aleatória será contra a lógica 0.10.1.

### Fechada Versão 0.11.1

Heurística:
- Como primeiro jogador da mão: escolhe carta de menor valor
- Como segundo: escolhe carta maior que a da mesa, se tiver, senão escolhe carta de menor valor

Performance:
- contra 0.10.1: 94,3% de vitórias
- contra 0.11.0: 72,7% de vitórias
- contra si próprio: 53,5% de vitórias

Apresenta melhora relavante com relação às versões anteriores e coerência contra si.

## Próximos passos

Próximo objetivo principal é apenas incluir inteligência na lógica de jogo.

### Versão 0.11.x

Criar algumas regras bem básicas, utilizando apenas "if"s.

Obs. válidas para 0.1y:
- 0.1y.x - O número indicado no "x" será a versão a lógica desenvolvida com técnica semelhante à inicial (0.1y.1).
- Uma nova lógica sempre enfrentará as lógicas anteriores para medir a performance.

### Versão 0.12.x

Será iniciado o uso de IA na lógica.

Provavelmente a primeira versão utilizará aprendizado por reforço.

### Versão 0.13.x

Provável utilização de deep learning. A decidir.

### Versão 0.20.x

Alguma interface simples para jogar com humanos.

O histórico de todos os jogos contra humanos (ou entre humanos, quando houver) será guardado.

### Versão 0.21.x

Revisão completa da estrutura de classes, objetivando ser mais genérica

### Versão 0.2y.x

Variações no "y" alternarão entre melhorias de inteligência, interface humana e estrutura de código.

### Versão 0.30.x

Abrir alguma interface para jogo via web.
