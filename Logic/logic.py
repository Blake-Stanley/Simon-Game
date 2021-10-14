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
