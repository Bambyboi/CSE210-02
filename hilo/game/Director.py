from game.Card import Card

class Director:

    def __init__(self):
        self.card = Card()
        self.another = ""
        self.choice = ""
        self.score = 0
        self.keep_playing = True
        self.points = 0

    def start_playing(self):
        """Gets things going and will be cycled through every time they choose to play another round"""
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Starts things out by getting assigning card_number1"""
        self.card.card_number1
        

    def do_updates(self):
        """Checks the guess of the player by reaching into Card.py and gives or takes poins accordingly."""
        if self.choice == "low":
            self.points = self.card.low()
        
        elif self.choice == "high":
            self.points = self.card.high()

    def do_outputs(self):
        """Outputs the important game information for each round of play. it shows the player
        their first card and shows them their score. it then asks them if they would like another card
        if yes, it gets their guess and startes everything over. 
        if no, it stopps the game. 
        """

        self.another = input("Play again (y/n):")
        print(f"\nThe card is: {self.card.card_number1}")
        
        if self.another == "y":
            self.choice = input("High or Low? [high/low]:")
            print(f"Your next card was {self.card.next_card}")
            print(f"Your score is: {self.card.point_total}")
            
            self.do_updates

        else:
            self.keep_playing = False
        
