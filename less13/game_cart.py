from random import choice


class Cart:
    list_suit = ["♣️", "♠️", "♥️", "♦️"]

    def __init__(self, suit: str, number: str):
        self.suit = Cart.add_suit(suit)
        self.number = number.upper()
        self.points = 0
        self.points_cart()

    def points_cart(self):
        if self.number.isdigit():
            self.points = int(self.number)
        elif self.number.upper() == "B":
            self.points = 2
        elif self.number.upper() == "D":
            self.points = 3
        elif self.number.upper() == "K":
            self.points = 4
        elif self.number.upper() == "T":
            self.points = 11

    @staticmethod
    def add_suit(suit: str) -> str:
        if suit.lower() == "tref":
            return Cart.list_suit[0]
        elif suit.lower() == "piki":
            return Cart.list_suit[1]
        elif suit.lower() == "chervi":
            return Cart.list_suit[2]
        elif suit.lower() == "bybna":
            return Cart.list_suit[3]
        else:
            print("NOT")

    def __repr__(self):
        return f'{"_" * 15}\n' + \
            f'{"{}{}{}".format(f"|{self.suit}{self.number}", (" " * 8), f"{self.suit}|")}\n' + \
            "|{}|\n".format(" " * 13) * 6 + "\n" + \
            "{}{}{}".format(f"|{self.suit}", (" " * 8), f"{self.number}{self.suit}|") + "\n" + "_" * 15


def summ_point_cart(cart1: Cart, cart2: Cart) -> int:
    return cart1.points + cart2.points


def card_deck() -> list[object]:
    deck = []
    numbers_list = [*range(6, 11), "B", "D", "K", "T"]
    suit_list = ["tref", "piki", "chervi", "bybna"]

    for number in numbers_list:
        for suit in suit_list:
            deck.append(Cart(suit, str(number)))

    return deck


