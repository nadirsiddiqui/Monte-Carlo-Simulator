# Metadata

* **Project Name:** Monte Carlo Simulator
* **Author:** Nadir Siddiqui

---
# Synopsis

## Installing

Once the repository has been locally cloned, navigate to the repository using bash terminal. To install the package, run this code:

```bash
pip install -e .
```

## Importing

Importing this package into a python file by running this code:

```python
from montecarlo.montecarlo import *
```

## Creating Dice

Create a die object by passing a list of strings or integers through the `Die()` class as a parameter:

```python
die = Die([1, 2, 3, 4, 5, 6]) ## This instantiates a 6-sided die with values 1-6
```

Change a die object's weights by passing the face *value* and new *weight* it will be assigned with the `.change_weight(value, weight)` method:

```python
die.change_weight(2, 5)
```

Roll a die using the `.roll(number)` method. The *number* of rolls defaults to 1 unless a different number is passed through:

```python
die.roll(10)
```

Show the die's current face values and weights using the `.show()` method:

```python
die.show()
```

## Playing Games

Start a game by passing a list of die objects through the `Game()` class as a parameter:

```python
game = Game([die1, die2, die3])
```

Play a game by passing the *number* of times the dice should be rolled through the `.play()` mehtod:

```python
game.play(10)
```

Show the results of the game as a data frame using the `.show(form)` method. The data frame defaults to "wide" form unless *form* is specified as "narrrow":

```
game.show()
```

## Analyzing Games

Initiate an analysis object by passing a game object through the `Analyzer()` class as a parameter:

```python
analysis = Analyzer(game)
```

Compute the number of times in the game a roll results with the same face value for each die using the `.jackpot()` method:

```python
analysis.jackpot()
```

Compute the distinct combination of face values rolled along with their counts using the `.combo()` method:

```python
analysis.combo()
```

Compute the number of times a given face is rolled in each event using the `.faces()` method:

```python
analysis.faces()
```

___
# API Description


## class Die()
This class initiates, modifies, and rolls "die". The following are methods and attributes of this class:

### __init__(array)
This method initializes a die object. It takes in an array of values (either numeric or string) as the faces of the object. Each object's faces default to a weight of 1.0.

**Parameters:**
array
	- array or list of face values
	- can be numeric or string
	- weights are defaulted to 1.0

### change_weight()
This method offers an opportunity to change the weights of the faces of the object that was created.

**Parameters:**
value
	- the face value that is to be affected
	- If the face value is not contained in the array of the object, an error message will be returned.
weight 
	- the new weight to be assigned to the face
	- If the weight is not a float or is unable to be converted to a float, an error message will be returned.
	
### roll()
This method rolls the object created by taking a random sample of the object's faces using the assigned weights.

**Parameters:**
number 
	- number of rolls desired;
	- the default is set to 1 

### show()
This method returns the current face values and the corresponding weights for the object.


## class Game()
This class initiates, plays, and displays the result of a game.

### __init__()
This method initializes a list of objects/die that will be used while playing the Game.

**Parameters:**
die 
	- a list of similar Die objects that will be used in the game
	
### play()
This method plays the Game by rolling each object a set number of times and adds the results of the rolls to a data frame.

**Parameters:**
number 
	- the number of rolls each die should be rolled

### show()
This method returns the data frame containing the results from playing the game.

**Parameters:**
form 
	- whether the data frame should be returned in wide or narrow form
	- if the input for this parameter is not "narrow" or "wide", it will return an error.


## class Analyzer()
This class takes the results of a game and computes various descriptive statistical properties about it.

### __init__()
This method initializes the results of a game to prepare for analysis.

**Parameters:**
game 
	- a Game object to analyze)
	
### jackpot()
This method compute how many times the game resulted in all faces being identical. It then stores the roll number along with the face value to a data frame. Finally, it returns how many jackpots occurred to the user.

### combo()
This method computes and returns the distinct combinations of faces rolled, along with their counts. This is returned as a data frame.

### faces()
This method computes how many times a given face is rolled in each event and stores the results into a data frame that is returned to the user.

---
# Manifest

Monte-Carlo-Simulator
    montecarlo
	    .DS_Store
        __init__.py
        montecarlo.py
	.DS_Store
	.gitignore
	LICENSE
	README.md
	montecarlo_demo.ipynb
	montecarlo_testresults.txt
	montecarlo_tests.py
	setup.py