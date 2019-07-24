import matplotlib.pyplot as plt

class Rocket():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

rockets=[]
rockets.append(Rocket())
rockets.append(Rocket(0,2))
rockets.append(Rocket(1,4))
rockets.append(Rocket(2,6))
rockets.append(Rocket(3,7))
rockets.append(Rocket(5,9))
rockets.append(Rocket(8,15))  

for index, rocket in enumerate(rockets):
  #original position of rockets
  print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
  plt.plot(rocket.x, rocket.y, 'ro', linewidth=2, linestyle='dashed', markersize=12)
  #move the 'rocket' one up
  rocket.move_up()
  print("New Rocket position %d is at (%d, %d)." % (index, rocket.x, rocket.y))
  #plot the new position
  plt.plot(rocket.x, rocket.y, 'bo', linewidth=2, linestyle='dashed', markersize=12)
  #move the rocket left, then plot the new position
  rocket.move_left()
  plt.plot(rocket.x, rocket.y, 'yo', linewidth=2, linestyle='dashed', markersize=12)
#show graph legend to match colors with position
plt.gca().legend(('original position','^ - Moved up', '< - Moved left'))
plt.show()
#plt.legend(loc='upper left')