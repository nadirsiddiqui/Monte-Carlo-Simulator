import pandas as pd
import numpy as np


class Die():
    """
    This class initiates, modifies, and rolls "die".
    """
    
    def __init__(self, array):
        """
        This method initializes a dice object. It takes in an array of 
        values (either numeric or string) as the faces of the object.
        Each object's faces default to a weight of 1.0.
        """

        self.w = []
        for i in array:
            self.w.append(1.0)
        self._df = pd.DataFrame({
            'faces': array, 
            'weights': self.w
        })
    
    def change_weight(self, value, weight):
        """
        This method offers an opportunity to change the weights of the 
        faces of the object that was created.
        
        There are two parameters: 
            - value (the face value that is to be affected 
            - weight (the new weight to be assigned to the face)
            
        If the face value is not contained in the array of the object,
        an error message will be returned. 
        If the weight is not a float or is unable to be converted to 
        a float, an error message will be returned.
        """
        
        if value not in self._df.faces.values:
            print("Face value is not in the original array")
        elif (type(weight) != float) and (type(weight) != int):
            print("Weight is not valid")
        else:
            weight = float(weight)
            self._df.loc[self._df['faces'] == value, 'weights'] = weight
        
    def roll(self, number = 1):
        """
        This method rolls the object created by taking a random sample of the 
        object's faces using the assigned weights.
        
        There is one parameter:
            - number (number of rolls desired; The default is set to 1)
        """
        
        return list(self._df.sample(number, weights = self._df.weights, replace=True).faces)
        
    def show(self):
        """
        This method returns the current face values and the corresponding 
        weights for the object. 
        """
        
        return self._df

    
class Game():
    """
    This class initiates, plays, and displays the result of a game.
    """
    
    def __init__(self, die):
        """
        This method initializes a list of objects/die that will be used
        while playing the Game.
        
        There is 1 parameter:
            - die (A list of similar Die objects that will be in the game)
        """
        
        self.die = die
        
    def play(self, number):
        """
        This method plays the Game by rolling each object a set number of 
        times and adds the results of the rolls to a data frame. 
        
        There is 1 parameter:
            - number (The number of rolls each die should be rolled)
        """
        
        self._df = pd.DataFrame()
        self.x = 1
        for i in self.die:
            df1 = pd.DataFrame({"Die "+str(self.x): pd.Series(i.roll(number))})
            self._df = pd.concat([self._df, df1], axis = 1)
            self.x += 1

        self._df['Rolls'] = list(range(1, number+1))
        self._df.set_index('Rolls', inplace=True)
            
    def show(self, form = "wide"):
        """
        This method returns the data frame containing the results from
        playing the game. 
        
        There is 1 parameter:
            - form (Whether the data frame should be returned in wide or
            narrow form. If the input for this paramtere is not "narrow" or 
            "wide", it will return an error.
        """
  
        if form != "wide" and form != "narrow":
            print("Invalid form")
        elif form == "wide":
            return self._df
        elif form == "narrow":
            self._df = self._df.stack().to_frame('Face')
            self._df.reset_index().set_index(['Rolls','Face'])
            return self._df 
        

class Analyzer():
    """
    This class takes the results of a game and computes various descriptive
    statistical properties about it.
    """
    
    def __init__(self, game):
        """
        This method initializes the results of a game to prepare for analysis.
        
        There is 1 parameter:
            - game (a Game object to analyze)
        """
        
        self.game = game
        self._result = self.game.show()
            
    def jackpot(self):
        """
        This method compute how many times the game resulted in all faces 
        being identical. It then stores the roll number along with the face 
        value to a data frame called dfjack. Finally, it returns how many 
        jackpots occured to the user. 
        """
       
        vals = self._result.values
        self.dfjack = pd.DataFrame()
        self.jackpot = 0
        
        for i in range(0, len(self._result)-1):
            if pd.Series(vals[i]).nunique() == 1:
                df2 = pd.DataFrame({'Face' : pd.Series(vals[i][0]),
                                    'Roll' : i+1
                                   })
                self.dfjack = pd.concat([self.dfjack, df2], axis = 0)
                self.jackpot += 1
                
        self.dfjack.set_index('Roll', inplace=True)
        
        return self.jackpot   
            
    def combo(self):
        """
        This method computes and returns the distinct combinations of faces rolled, 
        along with their counts. This is returned as a data frame.
        """
        
        return self._result.apply(lambda x: pd.Series(sorted(x)), 1)\
    .value_counts()\
    .to_frame('n')
        
    def faces(self):
        """
        This method computes how many times a given face is rolled in each event and
        stores the results intoa data frame that is returned to the user. 
        """
        
        self.df = self._result.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        
        return self.df 