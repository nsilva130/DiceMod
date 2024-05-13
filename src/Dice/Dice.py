import random

class Dice:
    
    # Initialize logger
    import logging
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
            sides (int, optional): The maximum value that a given die should generate. Defaults to 6. Must be 0 or a positive integer
            count (int, optional): The number of this type of dice for this Dice instance. Defaults to 1. Must be 0 or a positive integer.

        Raises:
            ValueError: If sides or count are a negative or non-integer value
        """
        
        # Check if sides parameter is valid
        # Must be Integer and non-negative
        if not (isinstance(sides,int) and sides>=0):
            message = f"sides must be 0 or a positive integer. Received value: {sides}"
            self.__log.error(f"ValueError: {message}")
            raise ValueError(f"{message}")
        
        # Check if count parameter is valid
        # Must be Integer and non-negative
        if not (isinstance(sides,int) and sides>=0):
            message = f"count must be 0 or a positive integer. Received value: {count}"
            self.__log.error(f"ValueError: {message}")
            raise ValueError(f"{message}")
        
        # Assign the values to the new Dice object
        self.__sides = sides
        self.__count = count
        self.__previous = None
        
        
    def __str__(self):
        """Creates the String representation of the Dice. 

        Returns:
            str: A string that represents the given Dice object.
        """
        return f"{self.__count}d{self.__sides}"
    
    
    def getSides(self):
        """Get the number of sides for the Dice

        Returns:
            int: The number of sides
        """
        return self.__sides
        
    def getCount(self):
        """Get the number of die for the Dice

        Returns:
            int: The number of die
        """
        return self.__count
    
    def getPrevious(self):
        """Get the most recent result of the Dice

        Returns:
            int: The most recent result of the Dice
        """
        return self.__previous
    
    def roll(self):
        """Roll a die a number of times equal to its count and get the sum of all rolls.

        Returns:
            int: The result of the roll
        """
        
        value = 0
        
        if self.__sides > 0:
            for i in range(self.__count):
                value += random.randint(1, self.__sides)
        
        self.__previous = value
        return value

    # Define alias of roll method.
    r = roll