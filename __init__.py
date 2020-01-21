import pandas as pd
from PIL import Image
import os, random, re
import Gwent
import Gwent.AllCards as AllCards
import inspect

class Card():
    """Card class, each card that will be used in the game will be an instance of this class, the data of the game is recorded
    in dictionnaries that will be unpickled at the start of each game, then all card will be instanced and stored in the NameSpace
        _ Indicant of the card (str)
        _ Power of the card (int)
        _ Name of the card (str)
        _ Faction it belongs to (str)
        _ Role it takes on the field (str), infantry, archery, siege or Weather (horn is considered as weather)
        _ Special powers (str) : clone, spy, medic, reforce, burn, muster
        _ Hero (bool)"""


    def __init__(self, CardData={}):
        super(Card, self).__init__()

        self.ImagePath = inspect.getfile(Gwent).split("__")[0]+"images\\"
        
        self.data = CardData

        self.Indicant = CardData.Indicant
        self.Name = CardData.Name
        self.Power = CardData.Power
        self.Faction = CardData.Faction
        self.Role = CardData.Role
        self.Special = CardData.Special
        self.Hero = CardData.Hero
        self.imgrectopath = str(self.ImagePath)+str(self.Indicant)+".png"
        self.imgversopath = str(self.ImagePath)+str(self.Faction)+".png"
        
    def chgfaction(self, faction):
        """Change the neutal cards to the desired faction"""
        self.Faction = faction
        self.imgversopath = "images\\Thumbs\\"+str(self.Faction)+".png"
        
    def showimage(self, recto=True):
        """Later, to provide visuals """
        try:
            if recto:
                img = Image.open(card.imgrectopath)
            else:
                img = Image.open(card.imgversopath)
            img.show()
        except IOError: 
            pass
        
class Field():
    """
        _ AccessCards : initializes the Card classes of all the cards
        _ BeginGame : setups the field, begins a while loop until victory is true for one user, creates two decks and shows them to each user
        _ BeginTurn : start one turn
        _ Play : function that allows one to put a card on the field.
        _ SpecialActive : function that after the card is dropped, checks if she has a special power and activates it.
        _ EndTurn : ends the turn, begins a new one.
        _ EndGame : Concludes the game
    """
    
    def __init__(self):
        self.AccessCards()
        self.BeginGame()
        
    def AccessCards(self):
        #Create decks by adding faction and neutral cards, data is stored in another file in the function CreateCardsDict
        self.FullDeck = AllCards.CreateCardsDict()
        self.BossesDeck = AllCards.CreateBossesDict()

        #Create a dict per Deck
        self.NeutralCardsDict = self.FullDeck[self.FullDeck["Faction"] == "Neutral"]

        self.DeckNorthermRealmsDict = self.FullDeck[self.FullDeck["Faction"] == "NorthernRealms"].append(self.NeutralCardsDict)        

        self.DeckNilfgaardDict = self.FullDeck[self.FullDeck["Faction"] == "Nilfgaard"].append(self.NeutralCardsDict)

        self.DeckMonstersDict = self.FullDeck[self.FullDeck["Faction"] == "Monsters"].append(self.NeutralCardsDict)

        self.DeckScoiataelDict = self.FullDeck[self.FullDeck["Faction"] == "Scoiatael"].append(self.NeutralCardsDict)

        #Create an instance of the class Card for each card and regroup them in Decks
        self.DeckDictTypes = [self.DeckNorthermRealmsDict, self.DeckNilfgaardDict, self.DeckMonstersDict, self.DeckScoiataelDict]
        
        #Initialize the final decks, and regroup them for iteration
        self.DeckNorthermRealms, self.DeckNilfgaard, self.DeckMonsters, self.DeckScoiatael = [], [], [] ,[]
        self.DeckTypes = [self.DeckNorthermRealms, self.DeckNilfgaard, self.DeckMonsters, self.DeckScoiatael]

        #A deck per faction is created
        for DeckDictType, self.DeckType in zip(self.DeckDictTypes, self.DeckTypes):
            for row in DeckDictType.itertuples():
                self.DeckType.append(Card(row))
        
    def PickDeck(self, Faction):
        """Creates a random deck"""
        
        if Faction == "NorthernRealms":
            Deck = random.sample(self.DeckNorthermRealms, 10)
        elif Faction == "Monsters":
            Deck = random.sample(self.DeckMonsters, 10)
        elif Faction == "Scoiatael":
            Deck = random.sample(self.DeckScoiatael, 10)
        elif Faction == "Nilfgaard":
            Deck = random.sample(self.DeckNilfgaard, 10)
        return Deck
    
    def ShowCards(self, Player):
        """Show the cards to the players"""
        
        if Player is "Player1":
            print("\n"+self.Player1Name+", you have the following Deck\n")
            for card in self.Player1Deck:
                print("{} has a power of {}, is played as {}. Specialty : {}, Heroism? {}\n".format(card.Name, card.Power, card.Role, card.Special, card.Hero))
        else:
            print("\n"+self.Player2Name+", you have the following Deck\n")
            for card in self.Player2Deck:
                print("{} has a power of {}, is played as {}. Specialty : {}, Heroism? {}\n".format(card.Name, card.Power, card.Role, card.Special, card.Hero))

    def StartPlayer(self):
        """Pick who starts the game"""
        
        if random.sample([0, 1], 1) == 1:
            return input("\n"+self.Player1Name+", choose who starts by answering 1 or 2 :")
        else:
            return input("\n"+self.Player2Name+", choose who starts by answering 1 or 2 :")
                
    def get_bool(self, prompt):
        """Function that gets a boolean input"""
        
        while True:
            try:
               return {"yes":True, "true":True, "false":False, "no":False}[input(prompt).lower()]
            except KeyError:
               print("Invalid input please enter True or False!")
            
    def get_int(self, prompt):
        "Make sure that we get a number between 1 and 10"
        
        while True:
            try:
                return {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10}[int(input(prompt))]
            except ValueError:
               print("Please enter a number between 1 and 10")
            except KeyError:
               print("Please enter a number between 1 and 10")
            
    def get_faction(self, prompt):
        """Make sure that the faction is correctly imputed by the user"""
        
        while True:
            try:
                return {"nilfgaard":"Nilfgaard", "scoiatael":"Scoiatael", "northernrealms":"NorthernRealms", "monsters":"Monsters"}[
                    input(prompt).lower().replace(" ", "").replace("'", "")]
            except KeyError:
               print("Invalid input, please enter either Nilfgaard, Scoiatael, Northern Realms or Monsters!")
        
    def ChangeCards(self):
        """At the beginning of the turn, one can change up to two cards"""
        
        if self.get_bool("\n"+self.Player1Name+", Do you want to change a first card ?"):
            nb = self.get_int("\nWhich card do you want to change ?")
            
        if self.get_bool("\n"+self.Player1Name+", Do you want to change a second card ?"):
            nb = self.get_int("\nWhich card do you want to change ?")

        if self.get_bool("\n"+self.Player2Name+", Do you want to change a first card ?"):
            nb = self.get_int("\nWhich card do you want to change ?")
            
        if self.get_bool("\n"+self.Player2Name+", Do you want to change a second card ?"):
            nb = self.get_int("\nWhich card do you want to change ?")

    def BeginGame(self):
        """Main function executed in __init__, assign names and deck, lauches the game and stays on a while loop"""
        
        #Create Names
        self.Player1Name = input("Player 1, what is your name ? ")
        self.Player2Name = input("\nPlayer 2, what is your name ? ")
        
        #Assign faction and decks
        self.Player1Faction = self.get_faction("\n"+self.Player1Name+", choose your Faction between Nilfgaard, Northern Reamls, Scoia'tael and Monsters:")
        self.Player1Deck = self.PickDeck(self.Player1Faction)
        self.Player2Faction = self.get_faction("\n"+self.Player2Name+", choose your Faction between Nilfgaard, Northern Reamls, Scoia'tael and Monsters:")
        self.Player2Deck = self.PickDeck(self.Player2Faction)
        
        #Show the cards
        self.ShowCards("Player1")
        self.ShowCards("Player2")

        #Change two cards
        self.ChangeCards()
        
        #Pick who starts
        self.Starter = self.StartPlayer()
        if self.Starter == "1":
            print("\n"+self.Player1Name+", you will begin the first turn!\n")
        else:
            print("\n"+self.Player2Name+", you will begin the first turn!\n")
            
        #Create some key variables
        self.Turn = 1
        self.Player1Points = 0
        self.Player2Points = 0

        while self.Player1Points != 2 and self.Player2Points !=2:
            self.BeginTurn()

        self.EndGame()
        
    def BeginTurn(self):
        """Begin a new turn"""
        
        print("\nThis is the turn number {}!\n".format(self.Turn))
        
        #Show who begins the turn
        if self.Starter == "1":
            print("\n"+self.Player1Name+", you begin!\n")
        else:
            print("\n"+self.Player2Name+", you begin!\n")
        
        #Modify the turn number and the player that will begin the next turn
        self.Turn += 1
        self.Starter = str((int(self.Starter)-1)**2)
        
        #Security for now
        self.Player1Points +=1
        
    def EndGame(self):
        """Ends the game, prints the name of the winner"""
        
        if self.Player1Points == 0 and self.Player2Points == 2:
            print("Good job "+self.Player1Name+", you have won!")
            
        if self.Player1Points == 1 and self.Player2Points == 2:
            print("Good job "+self.Player2Name+", you have won!")
            
        if self.Player1Points == 2 and self.Player2Points == 2:
            print("Good job guys, it's a tie !")
            
        if self.Player1Points == 2 and self.Player2Points == 1:
            print("Good job "+self.Player2Name+", you have won!")
            
        if self.Player1Points == 2 and self.Player2Points == 0:
            print("Good job "+self.Player2Name+", you have won!")