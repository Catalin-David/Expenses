from Expense import Expense
import copy

class Service:

    def __init__(self):
        '''
        Function initializes a new object of type Service
        '''
        self._expenses = []
        self._history = []
        
        self.addExpense(Expense("5", "25", "McDonald's"))
        self.addExpense(Expense("8", "10", "Smoothie"))
        self.addExpense(Expense("10", "1199", "Yeezy shoes"))
        self.addExpense(Expense("12", "5", "Ice cream"))
        self.addExpense(Expense("18", "78", "Groceries"))
        self.addExpense(Expense("19", "120", "Gym membership"))
        self.addExpense(Expense("21", "99", "Protein shake"))
        self.addExpense(Expense("25", "400", "Really nice coat"))
        self.addExpense(Expense("27", "2750000", "Lamborghini Aventador Coupe"))
        self.addExpense(Expense("30", "10000", "Trip to Miami"))

        self._history.clear()

    def makeNewList(self):
        '''
        Function creates an identical copyy of the current expenses list and returns it
        '''
        newList = []
        for expense in self._expenses:
            newList.append(copy.copy(expense))
        return newList

    def addExpense(self, expense):
        '''
        Function adds a new expense to the list in a position such that expenses are ordered chronologically 
        '''
        newList = self.makeNewList()
        self._history.append(newList)

        self._expenses.append(expense)
        self.sortExpenses()

    def listExpenses(self):
        '''
        Function creates a list of printing models for each expense and returns it
        '''
        listOfExpenses = []
        for expense in self._expenses:
            listOfExpenses.append(expense.__str__())
        return listOfExpenses

    def sortExpenses(self):
        '''
        Function sorts the list of expenses in a chronological order
        '''
        for i in range(0, len(self._expenses)):
            for j in range(i+1, len(self._expenses)):
                if self._expenses[j] < self._expenses[i]:
                    self._expenses[i], self._expenses[j] = self._expenses[j], self._expenses[i]
    
    def filterExpenses(self, amount):
        '''
        Function modifies the expense list so that it only contains expenses above a certain amount
        params: amount - the amount to which we compare expenses' amount
        '''
        try:
            amount = int(amount)
        except:
            raise ValueError("Amount on which we filter should be an integer")

        newList = self.makeNewList()
        self._history.append(newList)

        anotherList = []
        for i in range(0, len(self._expenses)):
            if self._expenses[i].Amount > amount:
                anotherList.append(self._expenses[i])

        self._expenses.clear()
        self._expenses.extend(anotherList)

    def undo(self):
        '''
        Function undoes the last operation that changed the expense list
        '''

        if len(self._history) == 0:
            raise ValueError("No more undos")

        self._expenses.clear()
        self._expenses.extend(self._history.pop())