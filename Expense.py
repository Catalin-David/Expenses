class Expense:

    def __init__(self, day= 1, amount=0, tip=""):
        '''
        Function initializes a new Expense
        params: day (default:1) - day of the expense (integer between 1-30)
                amount (default:0) - amount that is paid (integer)
                tip - type of expense/object that was purchased
        '''
        try:
            self._day = int(day)
            if self._day < 1 or self._day > 30:
                raise ValueError("Day should be between 1 and 30")
        except:
            raise ValueError("Day should be an integer")

        try:
            self._amount = int(amount)
            if self._amount < 0:
                raise ValueError("Amount of expense should be positive")
        except:
            raise ValueError("Amount of expense should be an integer")

        self._type = tip
    
    @property
    def Day(self):
        '''
        Property that returns the day of an expense
        '''
        return self._day

    @Day.setter
    def Day(self, value):
        '''
        Function is a setter for parameter day of an expense
        '''
        try:
            value = int(value)
        except:
            raise ValueError("Day should be an integer")
        if value < 1 or value > 30:
            raise ValueError("Day should be between 1 and 30")
        self._day = value

    @property
    def Amount(self):
        '''
        Property that returns the amount of an expense
        '''
        return self._amount
    
    @Amount.setter
    def Amount(self, value):
        '''
        Function is a setter for parameter amount of an expense
        '''
        try:
           value = int(value)
        except:
            raise ValueError("Amount of expense should be an integer")
        if value < 0:
            raise ValueError("Amount of expense should be positive")
        self._amount = value

    @property
    def Type(self):
        '''
        Property that returns the type of an expense
        '''
        return self._type
    
    @Type.setter
    def Type(self, value):
        '''
        Function is a setter for parameter type of an expense
        '''
        self._type = value

    def __str__(self):
        '''
        Function creates a model for priting an object of type Expense
        '''
        return "(Day: " +str(self.Day) + ", Amount: " + str(self.Amount) + ", Type: " + self.Type + ")"

    def __lt__(self, other):
        '''
        Function creates a model for comparing two objects of type Expense
        '''
        return self._day < other._day

def tests():
    try:
        expense = Expense("32", "100", "Food")
        assert False
    except ValueError:
        assert True

    try:
        expense = Expense("10.5", "100", "Food")
        assert False
    except ValueError:
        assert True

    try:
        expense = Expense("30", "100.5", "Food")
        assert False
    except ValueError:
        assert True

    try:
        expense = Expense("1", "-100", "Food")
        assert False
    except ValueError:
        assert True

    expense1 = Expense("25", "100", "Food")
    expense2 = Expense("18", "2500", "Gucci")
    assert expense2 < expense1

tests()