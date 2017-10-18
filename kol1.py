#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

#class bank:
def client(name, surname, year, cash_amount, bank):
	f = open(str(bank)+'.txt', 'w');
	f.write('Name: '+str(name) + 'Surname: '+str(surname)+ 'year: '+str(year)+'cash_amount: '+str(cash_amount)+'\n')
	f.close()
	return surname


print client("Anna", "Kowalski", 2017, 10000, 'bank1');
name = input('Name: ')
surname = input('Surname: ')
year = input('Year: ')
cash = input('Cash: ')
bank = input('bank: ')
print client(name, surname, year, cash, bank)
print(name)

