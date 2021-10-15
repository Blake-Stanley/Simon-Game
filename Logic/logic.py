import random 

sequence = []
player_sequence = []

def getSequence():
    return sequence

def appendPlayerSequence(character):
    player_sequence.append(character)
    
def progress():
    x = random.randint(1,4)
    if x == 1:
        x = 'g'
    elif x == 2:
        x = 'r'
    elif x == 3:
        x = 'y'
    elif x == 4:
        x = 'b'
    sequence.append(x)

def check():
    if player_sequence == sequence[:len(player_sequence)]:
        return True
    else:
        return False
 
def clearPlayerSequence():
    player_sequence.clear()

def getPlayerSequence():
    return player_sequence

# gets the current high score 
def getHighScore():
    current_high_score_obj = open('Logic/highScore.txt', 'r')
    return current_high_score_obj.read()
    # for score in current_high_score:
    #         return score

# sets high score to the player's score
def setHighScore():
    current_high_score = int(getHighScore())
    if current_high_score < len(sequence) - 1:
        current_high_score_obj = open('Logic/highScore.txt', 'w')
        current_score = "" + str(len(sequence)-1)
        current_high_score_obj.write(current_score)

# sets high score back to 0
def clearHighScore():
    current_high_score_obj = open('Logic/highScore.txt', 'w')
    current_high_score_obj.write("0")


