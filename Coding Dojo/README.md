# Coding Dojo

## Desenvolvimento de um RPG simples

A ideia é construir um jogo estilo RPG simples jogável pelo terminal. Não é necessário nenhuma interface gráfica para o game, porém o terminal deve exibir **informações suficientes¹** para que se entenda a situação atual do jogo.

    ¹ O grupo deve decidir o que são "informações suficientes";
---

## Requisitos

Como todo jogo de RPG, o jogo deve possuir um personagem no papel de herói (ou de heroína) controlado pelo jogador. Esse personagem deve ter um nome, pontos de vida, pontos de pontos de magia e carregar uma **arma** e uma **armadura** que devem poder ser trocados por outros pelo jogador. Nosso herói também deve ser capaz de carregar consigo **porções** para se recuperar.
Ele também deve ser capaz de **atacar** e **lançar mágias** em seus inimigos, assim como **receber ataques** deles, **beber poções** e **morrer** caso seus pontos de vida acabem.

O personagem possui um vilão² que deve enfrentar. Esse vilão deve possuir **caracteristicas** semelhantes ao herói, porém deve possuir nome, arma e armadura próprias e sua própria magia negra.

    ² O vilão pode ser jogável ou não, mas é esperado que exista um mecanismo de combate;

---

## Especificações

### Arma

É responsável por causar danos no adversário. Esse dano deve ser delimitado dentro de algum intervalo (definido pelo grupo) e não deve ser um valor fixo;

### Armadura

É responsável por resistir ao dano causado por ataques do adversário. Deve possuir valores para defesa mágica e física que serão deduzidos de todos os ataques recebidos. Esse valor deve ser dado em porcentagem.

### Magia

A magia é completamente aleatória e pode tanto atacar o adversário de maneira brutal quanto dar errado, deduzindo pontos do próprio usuário. Consome uma certa quantidade de pontos de magia. A tabela abaixo indica as possibilidades. A coluna "Chance" indica a chance de ocorrer o caso indicado na coluna "Efeito". A coluna "Consequência" indica o que ocorre com o personagem que tentou fazer uso de magia.

| Chance | Efeito  | Consequência |
| ------ | ------------------- | ------ |
| 10%    | Erro grave          | Usuário perde pontos de vida |
| 20%    | Erro simples        | Nada ocorre |
| 50%    | Magia lançada       | Tira uma quantidade fixa de pontos do inimigo |
| 20%    | Super magia lançada | Tira uma quantidade fixa de pontos muito maior |

## Jogabilidade

O jogo deve ocorrer por turnos com cada personagem escolhendo uma ação por vez. Uma ação do nosso personagem deve ser seguida por uma ação do adversário até que um dos dois acabem derrotados. Todas as ações que o usuário pode escolher devem ser exibidas no terminal, assim como seus pontos de vida e pontos de magia. Toda ação tomada deve ser evidenciada com alguma mensagem, para que se possa construir uma linha do tempo com todas as ações tomadas e suas consequências.
