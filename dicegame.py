import random

# 3 Class Blackjack Simulation but with dice and adjusted rules

# Dice class
class die:
    def __init__(self):
        self.val = random.randrange(1,7)

# Dealer Class
class dealer:
    # Initialize dealer
    def __init__(self, lvl):
        self.dicearr = []
        self.val = 0
        self.hold = False
        self.bust = False
        # Game version
        self.diff = lvl
        self.ones = 0
        # Dealer hold levels:
        self.lvl1 = 11
        self.lvl2 = 23
        
    # Flip function
    def flip(self):
        # Version 1 conditional: 2 flipped die originally
        if self.diff == 1:
            die1 = die()
            self.dicearr.append(die1)
            if die1.val == 1:
                die1.val = 7
                self.ones += 1
            #print("\nFirst die value: ", die1.val) 
            die2 = die()
            self.dicearr.append(die2)
            if die2.val == 1:
                die2.val = 7
                self.ones += 1
            #print("Second die value: ", die2.val)

            # Find if there are any duplicate dice
            val_list = []
            for i in self.dicearr:
                val_list.append(i.val)
            val_list.sort()
            val_dup = []
            # Make any duplicate values sum to 12
            for ind, i in enumerate(val_list):
                if ind > 0 and i < 6:
                    if val_list[ind-1] == i and (i not in val_dup):
                        val_list[ind] = 12 - val_list[ind-1]
                        #Keep track of duplicated die, only can get duplicate
                        #max once per dice value
                        val_dup.append(val_list[ind-1])
            
            val_list.sort()
            for i in val_list:
                self.val += i

                
            if self.val >= self.lvl1:
                self.hold = True

            # Die flip loop
            while not(self.hold):
                dieFlip = die()
                #print("Flipped die value: ", dieFlip.val)
                self.dicearr.append(dieFlip)
                #Test if its a one, only if a val of 7 would be helpful
                if self.val <= 6:
                    if dieFlip.val == 1:
                        dieFlip.val = 7
                        self.ones += 1
                
                #Test for duplicate die
                for i in val_list:
                    if i < 6 and (i not in val_dup):
                        if i == dieFlip.val:
                            val_dup.append(i)
                            dieFlip.val = 12 - dieFlip.val
                self.val += dieFlip.val

                #End conditions
                if self.val >= self.lvl1:
                    self.hold = True
                    if self.val >= 14:
                        for i in val_list:
                            if i == 7:
                                self.val -= 6
                                break
                        if self.val < self.lvl1:
                                self.hold = False
                        if self.val >= 14:
                            if self.ones == 2 and self.val == 14:
                                self.bust = False
                            else:
                                self.bust = True
                
            
            #print("Dealer total val: ", self.val)
            #print("Dealer bust: ", self.bust)
            return self.val, self.bust
        
        # Version 2 conditional: 4 flipped die originally
        if self.diff == 2:
            die1 = die()
            self.dicearr.append(die1)
            if die1.val == 1:
                die1.val = 7
                self.ones += 1
            #print("\nFirst die value: ", die1.val) 
            die2 = die()
            self.dicearr.append(die2)
            if die2.val == 1:
                die2.val = 7
                self.ones += 1
            #print("Second die value: ", die2.val)
            die3 = die()
            self.dicearr.append(die3)
            if self.ones < 2:
                if die3.val == 1:
                    die3.val = 7
                    self.ones += 1
            #print("Third die value: ", die3.val)
            die4 = die()
            self.dicearr.append(die4)
            if self.ones < 2:
                if die4.val == 1:
                    die4.val = 7
                    self.ones += 1
            #print("Fourth die value: ", die4.val)
            #Find if there are any duplicate dice
            val_list = []
            for i in self.dicearr:
                val_list.append(i.val)
            val_list.sort()
            val_dup = []
            #Make any duplicate values sum to 12
            for ind, i in enumerate(val_list):
                if ind > 0 and 1 < i < 6:
                    if val_list[ind-1] == i and (i not in val_dup):
                        val_list[ind] = 12 - val_list[ind-1]
                        #Keep track of duplicated die, only can get
                        #duplicate max once per dice value
                        val_dup.append(val_list[ind-1])
            
            val_list.sort()
            for i in val_list:
                self.val += i
            
            if self.val >= self.lvl2:
                self.hold = True

            # Die flip loop
            while not(self.hold):
                dieFlip = die()
                #print("Flipped die value: ", dieFlip.val)
                self.dicearr.append(dieFlip)
                #Test if its a one, only if a val of 7 would be helpful
                if self.val <= 19 and self.ones < 2:
                    if dieFlip.val == 1:
                        dieFlip.val = 7
                #Test if its a duplicate
                for i in val_list:
                    if i < 6 and (i not in val_dup):
                        if i == dieFlip.val:
                            val_dup.append(i)
                            dieFlip.val = 12 - dieFlip.val
                            
                self.val += dieFlip.val

                #End conditions
                if self.val >= self.lvl2:
                    self.hold = True
                    if self.val >= 27:
                        for i in val_list:
                            if i == 7:
                                self.val -= 6
                                break
                        if self.val < self.lvl2:
                            self.hold = False
                        if self.val >= 27:
                            self.bust = True
            
            #print("Dealer total val: ", self.val)
            #print("Dealer bust: ", self.bust)

            return self.val, self.bust

# Player Class
class player:
    def __init__(self, lvl, hold1, hold2):
        self.dicearr = []
        self.val = 0
        self.hold = False
        self.bust = False
        # 1 or 2
        self.diff = lvl
        self.ones = 0
        #Player hold levels:
        self.lvl1 = hold1
        self.lvl2 = hold2
        
    # Flip function
    def flip(self):
        # Version 1 conditional: 2 flipped die originally
        if self.diff == 1:
            die1 = die()
            self.dicearr.append(die1)
            if die1.val == 1:
                die1.val = 7
                self.ones += 1
            #print("\nFirst die value: ", die1.val) 
            die2 = die()
            self.dicearr.append(die2)
            if die2.val == 1:
                die2.val = 7
                self.ones += 1
            #print("Second die value: ", die2.val)

            # Find if there are any duplicate dice
            val_list = []
            for i in self.dicearr:
                val_list.append(i.val)
            val_list.sort()
            val_dup = []
            # Make any duplicate values sum to 12
            for ind, i in enumerate(val_list):
                if ind > 0 and i < 6:
                    if val_list[ind-1] == i and (i not in val_dup):
                        val_list[ind] = 12 - val_list[ind-1]
                        #Keep track of duplicated die, only can get duplicate
                        #max once per dice value
                        val_dup.append(val_list[ind-1])
            
            val_list.sort()
            for i in val_list:
                self.val += i

                
            if self.val >= self.lvl1:
                self.hold = True

            # Die flip loop
            while not(self.hold):
                dieFlip = die()
                #print("Flipped die value: ", dieFlip.val)
                self.dicearr.append(dieFlip)
                #Test if its a one, only if a val of 7 would be helpful
                if self.val <= 6:
                    if dieFlip.val == 1:
                        dieFlip.val = 7
                        self.ones += 1
                
                #Test for duplicate die
                for i in val_list:
                    if i < 6 and (i not in val_dup):
                        if i == dieFlip.val:
                            val_dup.append(i)
                            dieFlip.val = 12 - dieFlip.val
                self.val += dieFlip.val

                #End conditions
                if self.val >= self.lvl1:
                    self.hold = True
                    if self.val >= 14:
                        for i in val_list:
                            if i == 7:
                                self.val -= 6
                                break
                        if self.val < self.lvl1:
                                self.hold = False
                        if self.val >= 14:
                            if self.ones == 2 and self.val == 14:
                                self.bust = False
                            else:
                                self.bust = True
                
            
            #print("Dealer total val: ", self.val)
            #print("Dealer bust: ", self.bust)
            return self.val, self.bust
        
        # Version 2 conditional: 4 flipped die originally
        if self.diff == 2:
            die1 = die()
            self.dicearr.append(die1)
            if die1.val == 1:
                die1.val = 7
                self.ones += 1
            #print("\nFirst die value: ", die1.val) 
            die2 = die()
            self.dicearr.append(die2)
            if die2.val == 1:
                die2.val = 7
                self.ones += 1
            #print("Second die value: ", die2.val)
            die3 = die()
            self.dicearr.append(die3)
            if self.ones < 2:
                if die3.val == 1:
                    die3.val = 7
                    self.ones += 1
            #print("Third die value: ", die3.val)
            die4 = die()
            self.dicearr.append(die4)
            if self.ones < 2:
                if die4.val == 1:
                    die4.val = 7
                    self.ones += 1
            #print("Fourth die value: ", die4.val)
            #Find if there are any duplicate dice
            val_list = []
            for i in self.dicearr:
                val_list.append(i.val)
            val_list.sort()
            val_dup = []
            #Make any duplicate values sum to 12
            for ind, i in enumerate(val_list):
                if ind > 0 and 1 < i < 6:
                    if val_list[ind-1] == i and (i not in val_dup):
                        val_list[ind] = 12 - val_list[ind-1]
                        #Keep track of duplicated die, only can get
                        #duplicate max once per dice value
                        val_dup.append(val_list[ind-1])
            
            val_list.sort()
            for i in val_list:
                self.val += i
            
            if self.val >= self.lvl2:
                self.hold = True

            # Die flip loop
            while not(self.hold):
                dieFlip = die()
                #print("Flipped die value: ", dieFlip.val)
                self.dicearr.append(dieFlip)
                #Test if its a one, only if a val of 7 would be helpful
                if self.val <= 19 and self.ones < 2:
                    if dieFlip.val == 1:
                        dieFlip.val = 7
                #Test if its a duplicate
                for i in val_list:
                    if i < 6 and (i not in val_dup):
                        if i == dieFlip.val:
                            val_dup.append(i)
                            dieFlip.val = 12 - dieFlip.val
                            
                self.val += dieFlip.val

                #End conditions
                if self.val >= self.lvl2:
                    self.hold = True
                    if self.val >= 27:
                        for i in val_list:
                            if i == 7:
                                self.val -= 6
                                break
                        if self.val < self.lvl2:
                            self.hold = False
                        if self.val >= 27:
                            self.bust = True
            
            #print("Dealer total val: ", self.val)
            #print("Dealer bust: ", self.bust)

            return self.val, self.bust


if __name__ == "__main__":

    #Dealer bust test, must make flip
    #function return bust boolean
    """
    print("Sample dealer process")
    print("\nlevel 1:")
    i = 0
    count = 0
    while i <= 10000:
        dealer1 = dealer(1)
        if dealer1.flip():
            count += 1
        i += 1
    print("Dealer bust %: ", count/100, "%")
    print("\nlevel 2:")
    i = 0
    count = 0
    while i <= 10000:
        dealer2 = dealer(2)
        if dealer2.flip():
            count += 1
        i += 1
    print("Dealer bust %: ", count/100, "%")
    """
    #Sample game test
    print("Sample game")
    i = 0
    count1 = 0
    count2 = 0
    count3 = 0
    while i <= 10000:
        dealer1 = dealer(2)
        player1 = player(2,9,24)
        player2 = player(2,10,25)
        player3 = player(2,13,26)
        vald, bustd = dealer1.flip()
        val1, bust1 = player1.flip()
        val2, bust2 = player2.flip()
        val3, bust3 = player3.flip()
        if bustd:
            if not(bust1):
                count1 += 1
            if not(bust2):
                count2 += 1
            if not(bust3):
                count3 += 1
            continue
        if not(bust1):
            if val1 > vald:
                count1 += 1
        if not(bust2):
            if val2 > vald:
                count2 += 1
        if not(bust3):
            if val3 > vald:
                count3 += 1
        i += 1
    
    print("Player 1 win %: ", count1/100, "%")
    print("Player 2 win %: ", count2/100, "%")
    print("Player 3 win %: ", count3/100, "%")
    
    
