import matplotlib.pyplot as plt
import simple_module1 as rg 

#make series of rockets
rockets=[]
rockets.append(rg.Rocket())
rockets.append(rg.Rocket(0,2))
rockets.append(rg.Rocket(1,4))
rockets.append(rg.Rocket(2,6))
rockets.append(rg.Rocket(3,7))
rockets.append(rg.Rocket(5,9))
rockets.append(rg.Rocket(8,15))  


#show where each rocket is

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