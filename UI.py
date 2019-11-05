from Service import Service
from Expense import Expense
from os import *

class UI:
    
    def __init__(self, service):
        '''
        Function initializes an object fo type UI
        '''
        self._service = service

    def addExpense(self):
        '''
        Function reads input of a new expense and adds it to the list
        '''
        expense = Expense()

        expense.Day = input("Give day (integer between 1 and 30): ")
        expense.Amount = input("Give cost of expense (integer number): ")
        expense.Type = input("What did you spend this money on? : ")
        print("")
        self._service.addExpense(expense)

    def listExpenses(self):
        '''
        Function receives a list of printing models from the service and prints it
        '''
        lista = self._service.listExpenses()

        for l in lista:
            print(l)
        print("")

    def filterExpenses(self):
        '''
        Function receives input for an operation of type filter and executes the filtering
        '''
        amount = input("Only expenses above the value that you type here will be shown: ")
        print("")
        self._service.filterExpenses(amount)

    def undo(self):
        '''
        Function undoes the last operatiton that changed the expense list
        '''
        self._service.undo()

    def printMenu(self):
        print("Welcome to your expense assistant")
        print("What would you like to do?")
        print("     a -> add a new expense")
        print("     l -> list expenses")
        print("     x -> exit the program")
        print("     f -> filter expenses above a certain value")
        print("     u -> undo the last operation")
        print("")

    def start(self):
        '''
        Function navigates the user through the program
        '''
        stillRunning = True
        commands = {"a" : self.addExpense,
                    "x" : 0,
                    "l" : self.listExpenses,
                    "f" : self.filterExpenses,
                    "u" : self.undo}

        while(stillRunning):
            self.printMenu()
            command = input("Give command: ")
            print("")
            if command not in commands.keys():
                print("Invalid command")
            elif command == "x":
                print("Program will now exit. We look forward to seeing you again!")
                stillRunning = False
            else:
                try: 
                    commands[command]()
                    print("Operation carried out successfully")
                except Exception as error:
                    print(error)

            print("")
            system("pause")
            system("cls")

s = Service()
ui = UI(s)
ui.start()