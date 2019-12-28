#Student name : Suhani
#Student number: 119220491
##Python program to find toll_dodgers that takes a string parameter which represent name of text file
#containing toll data in specific format and print out vehicles that owes at least 50 euro in toll.
#Argument: string representing name of text file.
#return: list of toll_dodgers vehicle number in sorted order.

def list_toll_dodgers(tfile):
  if tfile != '':
    # Lets create a dictionary for putting vehicle breaking rule against time and date
    dodgers = {}
    file = open(tfile, 'r')

    for line in file:
      veh_det = line.split()
      veh_num = veh_det[0]
      date = ''
      time = ''
      date_split = veh_det[1].split('/')

      # Check for the first date of a month to not include it as there is no fine on that day
      if date_split[0] != '1':
        date = veh_det[1]
        time = veh_det[2]

      # Check for dodgers data in dictionary and append the time and date of rule
      #breaking if there is any data corresponding to the dodger vechicle
      if dodgers.get(veh_num) == None:
        if date != '':
          dodgers[veh_num] = [(date, time)]
      else:
        if date != '':
          dodgers.get(veh_num).append((date, time))
    
    # Lets create a dictionary for putting fine corresponding to dodger vehicle
    dodger_fine = {}

    for vehicle in dodgers.keys():
      timings = dodgers.get(vehicle)

      # Get the timings for each vehicle and find at what time of day it broke rule
      for time in timings:
        time_split = int(time[1].split(':')[0])

        # If rule was broken between 7 am and 7pm then give them a fine of 2.5 euros else 1 euro
        if dodger_fine.get(vehicle) == None:
          if time_split >= 7 and time_split <= 19:
            dodger_fine[vehicle] = 2.5
          else:
            dodger_fine[vehicle] = 1.0

        else:
          if time_split >= 7 and time_split <= 19:
            dodger_fine[vehicle] = dodger_fine.get(vehicle) + 2.5
          else:
            dodger_fine[vehicle] = dodger_fine.get(vehicle) + 1.0
  
  # Sort the dictionary by descending order of values
  sorted_dodgers = [(key, dodger_fine[key]) for key in sorted(dodger_fine, key=dodger_fine.get, reverse=True)]


  # Final dodgers to return are those having fine more than 50 euros.
  #Lets create a dictionary to return those vehicle who owe more than 50 euros or above
  final_dodgers = []

  for dodger in sorted_dodgers:
    veh_name = dodger[0]
    fine = dodger[1]
    if fine >= 50:
      final_dodgers.append(veh_name)

  if len(final_dodgers) > 0:
    return final_dodgers
  else:
    return 'No vehicles are fined more than 50 euros'


