from datetime import datetime
import random
import json
import os

class RPS:

    def playGame(self):
        gameArticles = ['Rock','Paper','Scissors']
        self.user1 = input('Enter the name of first user.')
        self.secondUserChoice = input('Do you want to play with User(U) or Computer (C) ?')
        if self.secondUserChoice.lower() == 'c' or self.secondUserChoice.lower() == 'computer':
            self.user2 = 'Computer'
        else: #here, we can get the second user probably from a network, anyone online or anyone from a list
            self.user2 = 'SomeOtherUser'
        self.user1Score = 0
        self.user2Score = 0
        print('Hello ', self.user1, 'and ', self.user2, '. Happy Playing')
        while True:
            user1Choice = input('Select one of the game articles from ' + str(gameArticles))
            user2Choice = random.choice(gameArticles)
            print('Thank you for your selection. Wait till the result is being determined.')
            result = self.__determineResult__(user1Choice.lower(),user2Choice.lower())
            if result.get('Winner') == None:
                print(result['Description'])
            else:
                if result.get('Winner') == 'user1':
                    result['Winner'] = self.user1
                    self.user1Score += 1
                elif result.get('Winner') == 'user2':
                    result['Winner'] = self.user2
                    self.user2Score += 1
            print('The winner is - ', result['Winner'], '.Description: ', result['Description'])
            result['YourChoice'] = user1Choice
            result['OpponentChoice'] = user2Choice
            result['YourScore'] = self.user1Score
            result['OpponentScore'] = self.user2Score
            #the results can be stored in a file or DB or any other medium.
            filePath = self.__saveResult__(self.user1,result)
            contChoice = input('Do you want to continue playing Y/N')
            if contChoice.lower() == 'n':
                print('The game results are stored in ', filePath)
                return filePath,result
                #break


    def __determineResult__(self,user1Choice, user2choice):
        resultDesc = None
        winner = None
        if user1Choice == 'rock':
            if user2choice == 'rock':
                resultDesc = 'There is a tie. Please play again'
            elif user2choice == 'paper':
                resultDesc = 'The paper has covered the rock.'
                winner = 'user2'
            elif user2choice == 'scissors':
                resultDesc = 'The rock has smashed the scissors.'
                winner = 'user1'
        elif user1Choice == 'paper':
            if user2choice == 'rock':
                resultDesc = 'The paper has covered the rock.'
                winner = 'user1'
            elif user2choice == 'paper':
                resultDesc = 'This is a tie. Please play again'
            elif user2choice == 'scissors':
                resultDesc = 'The Scissors have cut the paper.'
                winner = 'user2'
        elif user1Choice == 'scissors':
            if user2choice == 'rock':
                resultDesc = 'The rock has smashed the scissors.'
                winner = 'user2'
            elif user2choice == 'paper':
                resultDesc = 'The scissors have cut the paper.'
                winner = 'user1'
            elif user2choice == 'scissors':
                resultDesc = 'This is a tie. Please play again'
        else:
            resultDesc = 'Please make a proper selection'

        return {'Description':resultDesc,'Winner':winner}

    def __saveResult__(self,userName,result):
        filePath = os.path.dirname(__file__)
        filename = userName+'.txt'
        result['TimeStamp'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        with open(os.path.join(filePath,filename),'a') as fh:
            fh.write(json.dumps(result))
        return os.path.join(filePath,filename)

