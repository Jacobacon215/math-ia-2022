import random # this function imports the "random" module. i need random for the random.randint() function. this function allows me to pull a random value to use for drawing a card.

# defines "deck" early. it's needed for the self.probability definition (lines 15-16) in the Card class, so I had to put it early.
deck = 54 # I don't love making this a global variable but it's just way easier.

# I decided to use a class for the different cards because each of them has a bunch of attributes
# and this was cleaner and easier than storing them as a billion separate variables or as lists
class Card:
    def __init__(self, card, numCard) -> None: # initializes Card class
        self.card = card       # this attribute stores the type of card as a string, as shown on line 25
        self.numCard = numCard # this attribute stores the number of each type of card in the deck, as shown on line 25
        self.numDrawn = 0      # this attribute stores how many of this type of card have been drawn. defined at 0 because they all start at 0 and this way I don't have to fill this attribute on line 25.
        
    @property                    # the probability attribute is classified as a property so it can dynamically update. if the definition on lines 15-16 was in __init__, it would only check for it once.
    def probability(self):       # defining probability as a property basically makes a function that gets treated like an attribute. when instance.numCard is called, it returns the
        return self.numCard/deck # static (but updatable) value assigned to that attribute. if self.numCard/deck was in __init__, it would only get checked when the instance is
    'This property is the      ' # initialized. a property will execute its function every time it's called and return its dynamic value the same way an attribute would its static value.
    'probability of this type  '
    'of card being drawn.'

    def __str__(self) -> str: # defines how the class Card will be displayed if called in a print() or str() function.
        return f"There are {self.numCard} {self.card}s remaining in the deck. {self.numDrawn} have been drawn. The probability of drawing {self.card}s is {self.probability}."

# this is the mass definition of each type of card that I care about. formula: Card('name of card', how many of that card there are to start)
joker, ace, king, queen, other = Card('joker', 2), Card('ace', 4), Card('king', 4), Card('queen', 4), Card('other', 40)

def draw(): # this function simulates drawing a card based on a random number and returns what card was drawn.
    global deck # this pulls the deck variable we created earlier (line 4) into this function, so it can be updated as cards are drawn
    drawNum = random.randint(0,100000)/100000 # defines "drawNum" as a random number between 0 and 1. the number has 5 decimal places, which I think is plenty.

    # this for loop is the part that simulates drawing the card. it checks if the randomly generated number
    # is within range of a type of card: [          other          ][  queen  ][   king  ][   ace   ][joker]
    #                                                          ↑
    # and if it is, then it says "yes okay this is it, good" and stops.
    #
    # if it's not, then it removes
    # the section that it checked        [          other          ][  queen  ][   king  ][   ace   ][joker]
    # and keeps removing sections                                                  ↑
    # until the random number is
    # within range of the section        [  queen  ][   king  ][   ace   ][joker]
    # that's being checked.                             ↑
    # it removes sections by
    # subtracting the probability        [   king  ][   ace   ][joker]
    # of the active section if the           ↑
    # random number isn't within range.
    # when the program finds which card the random number responds to, it increments numDrawn (line 12),
    # decrements numCard (line 11), and decrements deck (line 4). decrementing deck and numCard affects
    # the probability property (lines 15-16) of every card, simulating drawing from the deck without
    # replacement.

    for i in [other, queen, king, ace, joker]: # the list is ordered like this because it corresponds to the graphic this way
        if drawNum <= i.probability: # checks if the random number is in range of the card that's currently being checked.
            # if it is:
            deck -= 1       # decrements deck (line 4, line 28) to simulate removing a card from the deck.→ → → → → → → ↘      The deck and instance.numCard variables are necessary
            i.numDrawn += 1 # increments numDrawn (line 12) to note how many of this type of card have been drawn.        → →  to calculate the instance.probability property.
            i.numCard -= 1  # decrements the numCard to simulate removing this specific type of card from the deck. → → ↗      The property (line 15-16) updates dynamically based
                            #                                                                                                  on these two variables.
            break           # there's no reason to keep checking numbers if the correct card was already found.
                            # this break statement cuts off the for loop for that reason.
        else:
            # if it isn't:
            drawNum -= i.probability # decrements the random number by the probability of the checked card appearing.
                                     # this sounds complicated but it's just the "cutting off" shown in the graphic.
            


draw()