
from die import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = ""
        self.rollsCount = 0
        self.atStartup = True
        self.winner = self.loser = False

    def __str__(self):
        """Returns a string representation of the list of rolls."""
       
        return self.roll

    def getRollsCount(self):
        """Returns the number of the rolls."""
        return self.rollsCount

    def rollDice(self):
        self.rollsCount += 1
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.roll = str((v1, v2)) + " total = " + str(v1 + v2)
        if self.atStartup:
            self.initialSum = v1 +v2
            self.atStartup = False
            if self.initialSum in (2,3,12):
                self.loser = True
            elif self.initialSum in (7,11):
                self.winner = True
        else:
            laterSum = v1 + v2
            if laterSum == 7:
                self.loser == True
            elif laterSum == self.initialSum:
                self.winner == True
        return(v1,v2)
        
    def isWinner(self):
        return self.winner
                
    def isLoser(self):
        return self.loser
    
    def play(self):
        """Plays a game, saves the rolls for that game,
        and returns True for a win and False for a loss."""
        while not self.isWinner() and not self.isLoser():
            self.rollDice()
        return self.isWinner()

def playOneGame():
        """Plays a single game and prints the results."""
        player = Player()
        while not player.isWinner() and not player.isLoser():
            player.rollDice()
            print(player)
        if player.isWinner():
            print("Number of rolls: " + str(player.getRollsCount()))
            print("You Win!")
        else:
            print("Number of rolls: " + str(player.getRollsCount()))
            print("You Lose!")
        
def playManyGames(number):
            """Plays a number of games and prints statistics."""
            wins = 0
            losses = 0
            winRolls = 0
            lossRolls = 0
            
            for number in range(number):
                player = Player()
                hasWon = player.play()
                rolls = player.getRollsCount()
                if hasWon:
                    wins += 1
                    winRolls += rolls
                else:
                    losses += 1
                    lossRolls += rolls
            print("The total number of wins is", wins)
            print("The total number of losses is", losses)
            print("The average number of rolls per win is %0.2f" % \
                  (winRolls / wins))
            print("The average number of rolls per loss is %0.2f" % \
                  (lossRolls / losses))
            print("The winning percentage is %0.3f" % (wins / number))

def main():
        """Plays a number of games and prints statistics."""
        #number = int(input("Enter the number of games: "))
        #playManyGames(number)
playOneGame()
number = int(input("Enter the number of games: "))
playManyGames(number)
    
if __name__ == "__main__":
    main()

