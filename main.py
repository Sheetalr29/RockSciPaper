#Game board
from Game_RPS import game

#This function is like a collection of games that the user can select, out of which Rock Paper Scissor is
#one such game. The idea here was to finish a game, come back and play another game or quit completely.
def startGame():
    gameList = ['1:Game1','2:RockPaperScissor','3:Game2']
    inpText = 'Please enter the corresponding numbers of the game that you want to play \n '
    sorryMsg = 'Sorry this game is not yet available. Select another'
    successMsg = 'Nice Choice. We shall now take you to the game'
    rps = None
    gameChoice = input(inpText + str(gameList))
    while True:
        match gameChoice:
            case '1':
                print(sorryMsg)
                gameChoice = input(inpText + str(gameList))
                continue
            case '3':
                print(sorryMsg)
                gameChoice = input(inpText + str(gameList))
                continue
            case '2':
                print(successMsg)
                if rps == None:
                    rps = game.RPS()
                rps.playGame()
        contChoice = input('Do you want to continue playing? Enter Y/N')
        if contChoice.lower() == 'n':
            break
        if contChoice.lower() == 'y':
            gameChoice = input(inpText + str(gameList))


if __name__ == '__main__':
    startGame()




