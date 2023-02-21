def draw(           # this is the main function. it's best practice to program within a function rather than write everything globally. everything in this program is inside of draw().
    deck=54,        # sets the default deck size to 54 but allows the parameter to be modified for flexibility
    numJokers=2,    # sets the default number of jokers to 2 but allows the parameter to be modified for flexibility
    numAces=4,      # sets the default number of aces to 4 but allows the parameter to be modified for flexibility
    numKings=4,     # sets the default number of kings to 4 but allows the parameter to be modified for flexibility
    numQueens=4,    # sets the default number of queens to 4 but allows the parameter to be modified for flexibility
    numOther=40,    # sets the default number of other cards to 4 but allows the parameter to be modified for flexibility
    selectCard=None # allows the function to draw a predetermined card when prompted. default is to draw a random card.
) -> tuple:         # metadata indicating the output format of the function is a tuple

    import random   # this statement imports the "random" module. i need random for the random.randint() function.
                    # the function allows me to pull a random value to use for drawing a card.


    # I decided to use a class for the different cards because each of them has a bunch of attributes
    # and this was cleaner and easier than storing them as a billion separate variables or as lists
    class Card:
        def __init__(self, card, numCard) -> None: # initializes Card class
            self.card = card       # this attribute stores the type of card as a string, as shown on line 30
            self.numCard = numCard # this attribute stores the number of each type of card in the deck, as demonstrated on line 30
            self.numDrawn = 0      # this attribute stores how many of this type of card have been drawn. defined at 0 because they all start at 0 and this way I don't have to fill this attribute on line 30.

        @property # the probability attribute is classified as a property so it can dynamically update. if the definition on lines 20-21 was in __init__, it would only check for it once.
        def probability(self) -> float: # defining probability as a property basically makes a function that gets treated like an attribute. when instance.numCard is called, it returns the
            return self.numCard/deck    # static (but updatable) value assigned to that attribute. if self.numCard/deck was in __init__, it would only get checked when the instance is
        'This property is the      '    # initialized. a property will execute its function every time it's called and return its dynamic value the same way an attribute would its static value.
        'probability of this type  '
        'of card being drawn.      '

        def __str__(self) -> str: # defines how the class Card will be displayed if called in a print() or str() function.
            return f"There are {self.numCard} {self.card}s remaining in the deck. {self.numDrawn} have been drawn. The probability of drawing {self.card}s is {self.probability}."

    # this is the mass definition of each type of card that I care about. formula: Card('name of card', how many of that card there are to start)
    other, queen, king, ace, joker = Card('other', numOther), Card('queen', numQueens), Card('king', numKings), Card('ace', numAces), Card('joker', numJokers)

    def drawCard() -> Card: # this function simulates drawing a card and returns the corresponding Card object.
        nonlocal deck, selectCard # this pulls the deck variable we created earlier (line 2) into this function, so it can be updated as cards are drawn.
                                  # it also pulls the selectCard parameter of draw() (line 8) into this function. this para
        
        # this try/except expression processes the selectCard parameter of draw() (line 8). it checks if a card
        # type was inputted when draw() was called.
        try:
            activeCard = eval(selectCard)
        except TypeError or NameError or EOFError: # only activates if no card was selected with selectCard (line 8). the except statement and its constituent clause are the random draw logic.
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
            # when the program finds which card the random number corresponds to, it increments numDrawn (line 17),
            # decrements numCard (line 16), and decrements deck (line 2). decrementing deck and numCard affects
            # the probability property (lines 19-21) of every card, simulating drawing from the deck without
            # replacement.

            for activeCard in [other, queen, king, ace, joker]: # the list is ordered like this [other, queen, king, ace, joker] because it corresponds to the graphic this way
                if drawNum <= activeCard.probability: # checks if the random number is in range of the card that's currently being checked.                                                                                            on these two variables.
                    break                             # if the correct card was found, this stops the for loop. stopping the for loop when
                                                      # the correct card is found leaves activeCard equal to the correct card. this lets
                                                      # the random part of the function
                else:
                    # if it isn't:
                    drawNum -= activeCard.probability # decrements the random number by the probability of the checked card appearing.
                                                      # this sounds complicated but it's just the "cutting off" shown in the graphic.
        

        deck -= 1                # decrements deck (line 2, line 33) to simulate removing a card from the deck.→ → → → → → → ↘      The deck and instance.numCard variables are necessary
        activeCard.numDrawn += 1 # increments numDrawn (line 17) to note how many of this type of card have been drawn.        → →  to calculate the instance.probability property.
        activeCard.numCard -= 1  # decrements the numCard to simulate removing this specific type of card from the deck. → → ↗      The property (line 19-21) updates dynamically based

        return activeCard        # when called, drawCard will run and then act as the variable activeCard

    
    drawnCard = drawCard()

    return deck, drawnCard
            













                           # the following code is only run if drawCard.py is run as a script. 
if __name__ == '__main__': # running code as a script sets __name__ to __main__, but running code as a module does not.
    draw_a_card = draw() # calls the main function defined on line 1. no parameters are specified, so all are default.
    print(f'''cards remaining in deck: {draw_a_card[0]}
    {draw_a_card[1]}''')

## TODO:
##      fix comments
##      