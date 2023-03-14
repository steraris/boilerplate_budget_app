class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = []
    self.balance = 0
    self.spent = 0
  def deposit(self,amount,description = None):
    self.amount = amount
    self.description = description if description is not None else ''
    (self.ledger).append({"amount":self.amount,"description":self.description})
    self.balance += self.amount
  def print_ledger(self):
    return self.ledger
  def check_funds(self,check_amount):
    self.check_amount = check_amount
    if self.check_amount > self.balance:
      return False
    else:
      return True
  def withdraw(self,amount,description = None):
    self.amount = amount
    self.description = description if description is not None else ''
    if self.amount <= self.balance:
      self.balance -= self.amount
      (self.ledger).append({"amount": -abs(self.amount), "description": self.description})
    self.check_funds(amount)
    self.spent += self.amount
    if self.amount <= self.balance:
      return True
    else:
      return False
  def get_balance(self):
    return self.balance
  def transfer(self,amount,other_category):
    self.amount = amount
    self.other_category = other_category
    if self.check_funds(self.amount) == True:
      self.withdraw(self.amount,f'''Transfer to {self.other_category.name}''')
      other_category.deposit(self.amount,f'''Transfer from {self.name}''')
      return True
    else:
      return False
  def __str__(self):
    header = ''
    list_str = ''
    final_list = ''
    total_str = ''
    #Making the header
    if len(self.name) % 2 == 0:
      first_line = f'''{'*' * int(15-(len(self.name)/2))}{self.name}{'*' * int(15-(len(self.name)/2))}'''
      header += f'''{first_line}'''
    else:
      first_line = f'''{'*' * int(15 - (len(self.name) / 2))}{self.name}{'*' * int(16 - (len(self.name) / 2))}'''
      header += f'''{first_line}'''
    #Making the list
    for i in self.ledger:
      list_str += f'''{i['description'][:23]}{' '*(30 - (len(i['description'][:23])+len('%.2f' % i['amount'])))}{'%.2f' % i['amount']}\n'''
    #Displaying the Total
    total_str += f'''Total: {'%.2f' % self.balance}'''
    #Adding the components for the final string
    final_list = f'''{header}\n{list_str}{total_str}'''


    return final_list
  def get_spent(self):
    return self.spent


def create_spend_chart(category):
    sum_spent = 0
    percentages = {}
    f_string = ''
    for i in category:
        sum_spent += i.spent
    for i in category:
        percentages[i.name] = ((i.spent*100)/sum_spent)
    header = 'Percentage spent by category'
    f_string += header + '\n'
    if len(category) == 1:
        for i in reversed(range(0,101,10)):
            x = f'''{' '*(3-len(str(i)))}{i}| {'o ' if list(percentages.values())[0] >= (i) else ' '}  \n'''
            f_string += x
    if len(category) == 2:
        for i in reversed(range(0,101,10)):
            x = f'''{' '*(3-len(str(i)))}{i}| {'o ' if list(percentages.values())[0] >= (i) else '  '} {'o ' if list(percentages.values())[1] >= (i) else ' '}  \n'''
            f_string += x
    if len(category) == 3:
        for i in reversed(range(0,101,10)):
            x = f'''{' '*(3-len(str(i)))}{i}| {'o ' if list(percentages.values())[0] >= (i) else '  '} {'o ' if list(percentages.values())[1] >= (i) else '  '} {'o' if list(percentages.values())[2] >= (i) else ' '}  \n'''
            f_string += x
    if len(category) == 4:
        for i in reversed(range(0,101,10)):
            x = f'''{' '*(3-len(str(i)))}{i}| {'o ' if list(percentages.values())[0] >= (i) else '  '} {'o ' if list(percentages.values())[1] >= (i) else '  '} {'o ' if list(percentages.values())[2] >= (i) else '  '} {'o' if list(percentages.values())[3] >= (i) else ' '}  \n'''
            f_string += x
    f_string += f'''    {'-' * (len(x) - 5)}\n'''
    category_list = []
    for i in category:
        category_list.append(i.name)
    longestStr = max(category_list, key=len)
    longestStrNum = len(longestStr)
    Line = ''
    for value in range(0,longestStrNum):
        Line += '    '
        number = 1
        for i in category_list:
            if len(i) > value:
                Line += (" " + i[value] + " ")
                if number == len(category_list):
                    Line += (' ' + '\n')

            else:
                Line += '   '
            number += 1
    f_string += Line
    f_string = f_string[:-1]
    return f_string