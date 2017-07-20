import random

five = ["california", "discrimination", "photosynthesis", "marijuana", "illuminati", "mummification", "lackadaisical"]
two = ["pumpkin", "mumbai", "yellow", "nothing", "broken", "alone", "baby", "london", "ism", "ogre"]
fiveSeven = ["thermochemistry", "sacrification", "executioner", "vegetarian", "mediterranean", "equilibrium", "sagittarius", "stoichiometry", "bureaucracy"]
fiveTwo = ["abracadabra", "hippopotamus", "antihistamine", "gentrification", "cafeteria", "radioactive", "awesomeness", "cytokinesis"]

lineOne = random.randint(0,6)
lineTwoSyl = random.randint(0,9)
lineTwoSev = random.randint(0,8)
lineThree = random.randint(0,7)

print(five[lineOne])
print(two[lineTwoSyl], fiveSeven[lineTwoSev])
print(fiveTwo[lineThree])
#5
#7
#5
