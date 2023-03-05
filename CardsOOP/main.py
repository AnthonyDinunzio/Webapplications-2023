# Cards using obj oriented programing
# Imports
import random


class Card(object):
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        if self.value == 11:
            self.face = "J"
        elif self.value == 12:
            self.face = "Q"
        elif self.value == 13:
            self.face = "K"
        elif self.value == 14:
            self.face = "A"

        if self.value == 11:
            self.value = 10
        elif self.value == 12:
            self.value = 10
        elif self.value == 13:
            self.value = 10

    def show(self):
        print(f"{self.face}-{self.suit}")


class Deck(object):
    def __init__(self, cards):
        self.deck = []
        for card in cards:
            self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        card = self.deck[0]
        self.deck.remove(self.deck[0])
        return card


class Player(object):
    def __init__(self):
        self.wallet = 100
        self.hand = []
        self.score = 0
        self.bet = 0

    def set_bet(self):
        while True:
            self.bet = float(input("Enter a bet: $"))
            if self.bet > self.wallet:
                print("Insufficient funds!")
                continue
            else:
                self.wallet -= self.bet
                print("Bets Placed!")
                break

    def reset(self):
        self.hand = []
        self.score = 0
        self.wallet = 100
        self.bet = 0


class Dealer(object):
    def __init__(self):
        self.hand = []
        self.score = 0


class Game:
    def __init__(self):
        cards = []
        values = range(2, 15)
        suits = ["D", "H", "C", "S"]
        for suit in suits:
            for val in values:
                cards.append(Card(suit, val))

        self.winner = None

        self.deck = Deck(cards)
        self.deck.shuffle()

        self.player = Player()
        self.dealer = Dealer()

    def calc_score(self):
        p_score = self.player.score
        d_score = self.dealer.score

        if p_score > 21:
            self.winner = "dealer"
        elif p_score > d_score and d_score < 21:
            self.winner = "player"
        elif p_score < d_score and p_score < 21:
            self.winner = "dealer"
        elif p_score == d_score and p_score <= 21:
            self.winner = "push"

    def print_pay_winner(self):
        print("### HAND OVER ###")
        if self.winner == "player":
            print("You won!")
            pay = self.player.bet * 2
            self.player.wallet += pay
            print(f"You bet: ${self.player.bet}")
            print(f"You earned: ${pay}")
            print(f"New Wallet Balance: ${self.player.wallet}")

        elif self.winner == "dealer":
            print("You lost!")
            print(f"New Wallet Balance: ${self.player.wallet}")

        else:
            print("Push!")
            print("You kept your bet amount!")

    def blackjack(self):
        print("### WELCOME TO BLACKJACK IN PYTHON ###")
        print(f"Your starting balance: ${self.player.wallet}")
        print("First things first would you like to play?")
        while True:
            play = int(input("1. Yes | 2. No: "))
            if play == 2:
                print("Closing...")
                quit()
            elif play == 1:
                break

            else:
                print("Invalid input try 1 or 2.")
                continue

        self.player.set_bet()
        print("Dealing Cards")
        card = self.deck.draw_card()
        self.player.hand.append(card)
        card_split = card.split("-")
        score = card_split[0]
        self.player.score += int(score)
        card.show()

        card = self.deck.draw_card()
        self.dealer.hand.append(card)
        card.face = "?"
        card_split = card.split("-")
        score = card.split[0]
        self.dealer.score += int(score)
        card.show()

        card = self.deck.draw_card()
        self.player.hand.append(card)
        card_split = card.split("-")
        score = card_split[0]
        self.player.score += int(score)
        card.show()

        card = self.deck.draw_card()
        self.dealer.hand.append(card)
        card_split = card.split("-")
        score = card_split[0]
        self.dealer.score += int(score)
        card.show()

        print(f"Your score: {self.player.score}")
        print(f"Your cards: {self.player.hand}")
        print("Would you like to hit or stay?")

        while True:
            hs = int(input("1. Hit | 2. Stay"))
            if hs == 2:
                while self.dealer.score < 17:
                    print("Dealer Hit")
                    card = self.deck.draw_card()
                    self.dealer.hand.append(card)
                    card_split = card.split("-")
                    score = card_split[0]
                    self.dealer.score += int(score)
                    card.show()
                print("Dealer Stay")
                self.calc_score()
                self.print_pay_winner()
                break
            elif hs == 1:
                card = self.deck.draw_card()
                self.player.hand.append(card)
                card_split = card.split("-")
                score = card_split[0]
                self.player.score += score
                card.show()
                continue
            else:
                print("Invalid entry try 1 or 2")
                continue
        self.blackjack()






game = Game()
game.blackjack()

