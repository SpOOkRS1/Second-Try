from .models import Chore, Maid
from . import db
import datetime
import itertools
dai = datetime.datetime.today()
chores = ["Floors", "Bathrooms", "Trash & Recycling"]
maids = {
    "Anthony" : "N/a",
    "Donte" : "None",
    "Aaron" : "NuN",
}

# Set maid id equal to chore id to start chore rotation
maids["Anthony"] = chores[0]
maids["Donte"] = chores[1]
maids["Aaron"] = chores[2]
print("This month set of chores:")
print("___________________")
for maid, chore in maids.items():
  print(f"Maid: {maid} / Chore: {chore}")
print()
print()

# Set maid id equal to the next chore id to continue rotation
print("Next month set of chores:")
print("___________________")
if dai.day == 10:
  chore_cycle = itertools.cycle(chores)
  next(chore_cycle)
  maids["Anthony"] = next(chore_cycle)
  maids["Donte"] = next(chore_cycle)
  maids["Aaron"] = next(chore_cycle)
  for maid, chore in maids.items():
    print(f"Maid: {maid} / Chore: {next(chore_cycle)}")
  print()

else:
  print("No celebration today :(")


print('Hello world!!!')