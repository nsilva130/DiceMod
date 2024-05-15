import random
import logging

class Dice:
    
    # Initialize logger
    dateFormat = '%Y-%m-%d %H:%M:%S'
    logFormat = '[%(asctime)s.%(msecs)03d] %(name)s (%(levelname)s): %(msg)s'
    __log = logging.getLogger("Dice")
    logging.basicConfig(format=logFormat,datefmt=dateFormat)
    
    ## Set Default Log Level
    _LOG_LEVEL = logging.INFO
    __log.setLevel(_LOG_LEVEL)
    
    
    def __init__(self,sides=6,count=1):
        """Creates an instance of Dice, which handles the rolling of different types of groups of integer values.

        Args:
            sides (int, optional): The maximum value that a given die should generate. Defaults to 6. Must be a positive integer
            count (int, optional): The number of this type of dice for this Dice instance. Defaults to 1. Must be 0 or a positive integer.

        Raises:
            ValueError: If sides or count are a negative or non-integer value
        """
        
        # Check if sides parameter is valid
        # Must be Integer and non-negative
        if not (isinstance(sides,int) and sides>=0):
            message = f"sides must be a positive integer. Received value: {sides}"
            self.__log.error(f"ValueError: {message}")
            raise ValueError(f"{message}")
        
        # Check if count parameter is valid
        # Must be Integer and non-negative
        if not (isinstance(sides,int) and sides>=0):
            message = f"count must be a positive integer. Received value: {count}"
            self.__log.error(f"ValueError: {message}")
            raise ValueError(f"{message}")
        
        # Assign the values to the new Dice object
        self.__sides = sides
        self.__count = count
        self.__previous = []
        
        
    def __str__(self):
        """Creates the String representation of the Dice. 

        Returns:
            str: A string that represents the given Dice object.
        """
        return f"{self.__count}d{self.__sides}"
    
    def sides(self):
        """Get the number of sides for the Dice

        Returns:
            int: The number of sides
        """
        return self.__sides
        
    def count(self):
        """Get the number of die for the Dice

        Returns:
            int: The number of dice in the Dice object
        """
        return self.__count
    
    def previous(self):
        """Get the most recent result of the Dice

        Returns:
            list[int] : The most recent roll of the Dice. Returns an empty list if no roll has taken place for this object. Returns a list of integers corresponding to the most recent roll otherwise.
        """
        return self.__previous
    
    def previousSum(self):
        """Get the sum of the most recent result of the Dice

        Returns:
            int : The most recent result of the Dice. Returns 0 if no roll has taken place for this object. Returns a single positive integer otherwise.
        """
        
        if (self.__count <= 0 or len(self.__previous) <= 0):
            return 0
        else:
             return sum(self.__previous)
    
    
    
    def rollSum(self):
        """Roll a die a number of times equal to its count and get the sum of all rolls.

        Returns:
            int: The result of the roll
        """
        values = [0] * self.__count
        
        if self.__sides > 0:
            for i in range(self.__count):
                values[i] = random.randint(1, self.__sides)
                
        self.__previous = values
        
        if (self.__count <= 0 or len(values) <= 0):
            return 0
        else:
             return sum(values)
    
    
    def roll(self):
        """Roll a die a number of times equal to its count, but do not sum the rolls,

        Returns:
            list[int]: The resulting collection of rolls
        """
        values = [0] * self.__count
        
        if self.__sides > 0:
            for i in range(self.__count):
                values[i] = random.randint(1, self.__sides)
                
        self.__previous = values
        return values
    


class DiceMath:
    
    # Initialize logger
    dateFormat = '%Y-%m-%d %H:%M:%S'
    logFormat = '[%(asctime)s.%(msecs)03d] %(name)s (%(levelname)s): %(msg)s'
    __log = logging.getLogger("DiceMath")
    logging.basicConfig(format=logFormat,datefmt=dateFormat)
    
    ## Set Default Log Level
    _LOG_LEVEL = logging.INFO
    __log.setLevel(_LOG_LEVEL)
    
    
    def _checkDice(self, obj) -> Dice:
        """Internal check to verify if the argument is an instance of the Dice object

        Args:
            obj (any): The object to test
            
        Returns:
            Dice: The object explicitly cast as a Dice object.

        Raises:
            ValueError: If the object is not an instance of the Dice class
        """
        if not isinstance(obj,Dice):
            message = f"dice must be an instance of the Dice class. Received value: {obj} ({type(obj)})"
            self.__log.error(f"ValueError: {message}")
            raise ValueError(f"{message}")
        else:
            return obj
    
    def average(self,dice):
        """Calculate the average result of rolling a single Dice object
        
        If either the sides or count of the Dice object are equal to 0, its average() will always be 0.
        
        Args:
            dice (Dice): The Dice object to get the average roll of.

        Returns:
            float: The average result of an infinite number of rolls
        """
        
        dice = self._checkDice(dice)
        
        value = 0.0
        
        if (dice.sides() > 0):
            value = dice.count() * ( ( dice.sides() / 2.0 ) + 0.5 )
        return value
    
    def max(self,dice):
        """Calculate the maximum possible value achievable when rolling the Dice.
        
        If either the sides or count of the Dice object are equal to 0, its max() will always be 0.
        
        Args:
            dice (Dice): The Dice object to get the max roll of.

        Returns:
            int: The maximum value the Dice will take.
        """
        
        dice = self._checkDice(dice)
        
        value = 0
        # If the Dice has no sides, will always be 0.
        if (dice.sides() > 0):
            value = dice.count() * dice.sides()
        return value
    
    def min(self,dice):
        """Calculate the minimum possible value achievable when rolling the Dice.
        
        If either the sides or count of the Dice object are equal to 0, its min() will always be 0.
        
        Args:
            dice (Dice): The Dice object to get the min roll of.

        Returns:
            int: The minimum value the Dice will take.
        """
        
        dice = self._checkDice(dice)
        
        value = 0
        # If the Dice has no sides, will always be 0.
        if (dice.sides() > 0):
            value = dice.count()
        return value
    
    def rollDropLow(self,dice: Dice,lowest=1):
        """Rolls a provided dice object and provides the resultant values with a specified number of lowest values removed.
        
        If lowest = 0, returns the result of rolling the Dice object once.
        
        If lowest >= dice.count(), it removes all values and returns an empty list.

        Args:
            dice (Dice): The Dice object to roll.
            lowest (int, optional): The number of lowest values to remove. Defaults to 1.

        Returns:
            List[int]: The values after removing the specified number of lowest values
            
        Raises:
            ValueError: If lowest is not 0 or a positive integer.
        """
        
        # If trying to remove a negative number of dice, raise an error
        if (not isinstance(lowest,int) or lowest < 0):
            message = f"lowest must be 0 or a positive integer. Received value: {lowest} ({type(lowest)})"
            self.__log.error(f"ValueError: {message}")
            raise ValueError(f"{message}")
        
        
        # Verify if dice is a Dice
        dice = self._checkDice(dice)
        
        # If removing more than the number of die in the Dice, return empty array
        if lowest >= dice.count():
            return [0] * 0
        
        # Roll the dice once for new values
        values = dice.roll()
        
        # Get a copy of those values
        result = values[:]
        
        # Remove the provided number of lowest values
        for i in range(lowest):
            result.remove(min(result))

        return result