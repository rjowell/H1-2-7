'''
Whole Number - pos, neg, 0 - INTEGER
Num with a decimal point - float
True / False - BOOLEAN
"Text inside of quotes" - STRING


'''
#print("Hello World")

print("hello")
userInput = input("How much gas do you want?")


class MyCar:

  started = False
  gasTankSize = 48
  currentFuel = 10
  
  
  def addFuel(self,howMuchFuel):
    if self.currentFuel + howMuchFuel > self.gasTankSize:
      print("There's not enough room in the tank!")
    else:
      self.currentFuel += howMuchFuel
      print("Current Fuel: "+str(self.currentFuel))
  
  def drive(self,distance):
    if self.started == False:
      print("Sorry, you haven't turned your car on yet!")
    elif self.currentFuel - distance <= 0:
      print("You don't have enough gas!")
      print("Current Fuel: "+str(self.currentFuel))
    else:
      print("We're crusing down the road!")
      self.currentFuel -= distance
      print("Current Fuel: "+str(self.currentFuel))
      #self.currentFuel = self.currentFuel - 1
  
  def stop(self):
    print("STOOOOP!!!")

  def startCar(self):
    self.started = True

  def turn(self):
    print("Turning")

  def __init__(self,whatColor,whatSeatMaterial,whatMake,howMuchGas):
    self.color = whatColor
    self.seatMaterial = whatSeatMaterial
    self.make = whatMake
    self.gasTankCapacity = howMuchGas
  #Drive
  #Stop
  #Turn - Left/Right

IansCar = MyCar("Black","Leather","Toyota",40)
IansCar.startCar()
IansCar.drive(15)
IansCar.drive(20)

IansCar.addFuel(35)
IansCar.addFuel(20)


