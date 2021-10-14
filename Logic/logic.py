import random 

sequence = []
player_sequence = []

def getSequence():
    return sequence

def appendPlayerSequence(character):
    #player_sequence.insert(0, character)
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
    #sequence.insert(0, x)
    #print(sequence)

'''
def check(index):
    if player_sequence[len(player_sequence) - 1] == sequence[index]:
        return True
    else:
        return False

'''
def check():
    if player_sequence == sequence[:len(player_sequence)]:
        return True
    else:
        return False
 
def clearPlayerSequence():
    player_sequence.clear()

def getPlayerSequence():
    return player_sequence

print(check())
