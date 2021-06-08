import DiceModule as dm

player1, player2 = dm.name_input()
dm.game_core(player1, player2)
dm.winner(player1, player2)
