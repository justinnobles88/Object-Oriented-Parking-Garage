class Garage:
  def __init__(self):
    self.tickets = 5
    self.spaces = 5
    self.cars_added = []

  def ShowSpaces(self):
    return(f'\nNumber of spaces: {self.spaces}')
  def ShowTickets(self):
    return(f'Number of tickets: {self.tickets}\n')
  def spots_available(self):
    return f'Number of spaces and tickets: {self.spaces}, {self.tickets}\n'
  def add_car(self, car):
    self.identifier = ['A1', 'A2', 'A3', 'A4', 'A5']
    if self.spaces > 0:
      self.cars_added.append(str(car).split(','))
      self.spaces -= 1
      self.tickets -= 1
      return f'Number of spaces and tickets available: {self.spaces}, {self.tickets}\n'
    else:
      print(f'We have {self.spaces} spaces available. I am sorry, please try the lot on Main St.!\n')
  def remove_car(self, car):
    self.identifier = ['A1', 'A2', 'A3', 'A4', 'A5']
    if self.spaces >= 0:
      self.cars_added.append(str(car).split(','))
      self.spaces += 1
      self.tickets += 1
      return f'Number of spaces and tickets available: {self.spaces}, {self.tickets}\n' 
my_garage = Garage()
print(my_garage.ShowSpaces(), my_garage.ShowTickets())

     

while True:
    response = input('Hello, would you like to park here today? yes/no/quit\n ')
    if response.lower() == 'no':
      print('Sorry we could not help, have a nice day!\n')
      
    if response.lower() == 'yes':
      print('Here is your ticket! You have a parking limit of 1 hour!\n')
      print(my_garage.add_car('A1'))
    if response.lower() == 'quit':
      break
      
    answer = input('Are you done with your errands and ready to leave? yes/no/quit \n')
    if answer.lower() == 'no':
      print('Okay, just checking since i seen you come by! Come back when you are ready to leave.\n')
    if answer.lower() == 'yes':
      print('Thank you for choosing our garage! Have a pleasant day!\n')
      print(my_garage.remove_car('A1'))
    if answer.lower() == 'quit':
      break
      





