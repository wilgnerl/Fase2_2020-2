# Coding Dojo
## Desenvolvimento de um RPG simples
A ideia é construir um jogo estilo RPG simples jogável pelo terminal. Não é necessário nenhuma interface gráfica para o game, porém o terminal deve exibir informações suficientes para que se entenda a situação atual do jogo.

## Requisitos
Como todo jogo de RPG o jogo deve possuir um herói controlado pelo jogador. Esse herói deve ter um nome, pontos de vida, pontos de estamina e carregar uma arma e uma armadura que devem poder ser trocados por outros pelo jogador. Nosso herói também deve ser capaz de carregar consigo poções para se recuperar.
Ele também deve ser capaz de atacar e lançar mágias em seus inimigos, assim como receber ataques deles, beber poções e morrer caso seus pontos de vida acabem.
    
Todo herói possui um vilão que deve enfrentar. Esse vilão deve possuir caracteristicas semelhantes ao herói, porém deve possuir nome, arma e armadura próprias e sua própria magia negra.
    
## Especificações
- #### Arma
    Define quanto de dano um personagem consegue infringir no outro. Esse dano deve ser especificado em valor máximo e minimo para que haja um aleatóridade em cada ataque.
- #### Armadura
    Define a resistencia a danos que o usuário possui. Deve possuir valores para defesa mágica e física que serão deduzidos de todos os ataques recebidos. Esse valor deve ser dado em porcentagem.
- #### Magia
    A magia é completamente aleatória e pode tanto atacar o inimigo de maneira brutal quanto dar errado, deduzindo pontos do próprio usuário. Consome uma certa quantidade de estamina. A tabela abaixo indica as possibilidades.

    | Porcentagem | Acontecimento | Consequencia |
    | ------ | ------ | ------ |
    | 10% | Erro grave | Usuário perde pontos de vida |
    | 20% | Erro simples | Nada ocorre |
    | 50% | Magia lançada | Tira uma quantidade fixa de pontos do inimigo |
    | 20% | Super magia lançada | Tira uma quantidade fixa de pontos muito maior |

    
## Jogabilidade
O jogo deve ocorrer por turnos com cada personagem escolhendo uma ação por vez. Um ação do nosso herói então um ação do vilão até que um dos dois acabem derrotados. Todas as ações que o usuário pode escolher deve sem exibidas no terminal, assim como seus pontos de vida e estamina. Toda ação tomada deve ser evidenciada com alguma mensagem, para que se possa construir uma linha do tempo com todas as ações tomadas e suas consequências.