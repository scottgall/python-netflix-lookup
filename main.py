import os
import csv

show = input("what show or movie are you looking for? --> ")

csvpath = os.path.join("resources", "netflix-ratings.csv")

found = False

with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")

  for line in csvreader:
    if line[0].lower() == show.lower():
      print("{} is rated {} with a rating of {}.".format(line[0], line[1], line[3]))
      found = True
      break

  if found is False:
    print("Sorry, we didn't find {}.".format(show))
