from matplotlib import pyplot as plt
import csv
import pandas as pd
import numpy as np
import statistics as av

# aspects of wellbeing
"""
competence, emotional stability, engagement, meaning, optimism, positive emotion, positive relationships, resilience, self-esteem, and vitality.
"""

# list only for converting to integer
# ------------------------------------------------------------------

reps_str = []
time_mili = []
temp = []
#         / enter csv file here / 
with open('microbit.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
            #print(row)
            temp.append(row[3])
            reps_str.append(row[1])
            time_mili.append(row[0])
    csv_file.close()
    
# ------------------------------------------------------------------

# removes microbits datalogging titles from the top of each column data
time_mili.remove("Time_secs")
reps_str.remove("Repititions")
temp.remove("Temp")

# new lists to be converted to integers
reps = []
time_milisecs = []
temp_celsius = []
# converting lists to integers for conditional statements
for obj in temp:
  temp_celsius.append(int(obj))

for item in reps_str:
    reps.append(int(item))
  
for thing in time_mili:
  time_milisecs.append(float(thing))
  
# running time and rep variable data  
columns = ["Time_secs", "Repititions"]

df = pd.read_csv("microbit.csv", usecols=columns)
# prints the set count, the rep per set and how long the set took

# ------------------------------------------------------------------

# Gives the user advice on their progress based on the number of repititions done
# This advice is based on research conducted into both bodybuilding and powerlifting
def well_being():
  count = 0
  # set is the reps in a set
  reps_set = []
  training_style = input("What are your fitness goals (aesthetics or strength):")
  print("\n")
  if training_style == "aesthetics":
    for x in reps:
      if x > 12:
        print(f"set {count+1} | {x} reps | is too light you should increase the weight for 8 reps")
      elif x >= 8 and x <= 12:
        print(f"set {count+1} | {x} reps | you should stick to the same weight but try to increase your reps to 12 then increase the weight")
      elif x <= 7:
        print(f"set {count+1} | {x} reps | is too heavy you should drop the weight so you do 12 reps")
      # count is the number of sets
      count += 1
      
  elif training_style == "strength":
    for x in reps:
      if x > 6:
        print(f"set {count+1} | {x} reps | is too light you should up the weight for strength building")
      elif x > 4 and x <= 6:
        print(f"set {count+1} | {x} reps | is the ideal weight for strength training")
      elif x < 4:
        print(f"set {count+1} | {x} reps | you should lower the weight to gain more strength")
      # count is the number of sets
      count += 1

# calls the well_being function       
well_being()

# ------------------------------------------------------------------

# anaylis component used to predict future data
def graph1():
  # taken from statology
  # ---------------------------------
  x = df.Time_secs 
  y = df.Repititions
  plt.figure(figsize=(5, 4))
  plt.xlabel("Time(seconds)")
  plt.ylabel("Reps")
  z = np.polyfit(x, y, 1) 
  p = np.poly1d(z)
  #adds trendline to the graph
  plt.plot(x, p(x), linewidth=1)
  plt.plot(df.Time_secs, df.Repititions, '-o')
  plt.title("Reps over time")
  plt.show()
  
graph1()

# ------------------------------------------------------------------

print("\n\nWHAT-IF QUESTION 1")
print("What if the user had to do as many reps for a minute as possible, how many could they get?")
wf1_total_time = 60
wf1_average_time_rep = float(input("What is your average rep duration(seconds)? : "))
wf1_max_time_rep = float(input("What is your max rep duration(seconds)? : "))
wf1_formula = wf1_total_time / (wf1_average_time_rep + wf1_max_time_rep / 2)
print(f"The user could get around {round(wf1_formula)} reps in a minute \n")

# ------------------------------------------------------------------

print("WHAT-IF QUESTION 2")
print("What if the user does 8 reps how long will it take")
wf2_reps = 8
wf2_average_time_rep = float(input("How long does it take you to do one rep (seconds): "))
wf2_max_time_rep = float(input("What is your maximum time for any rep (seconds) : ")) 
wf2_formula = 8 * (wf2_average_time_rep + wf2_max_time_rep / 2)
print(f"It will take around {wf2_formula} seconds")

# graphical format final requiement
Rep_range = [1,2,3,4,5,6,7,8,9,10]
Seconds_range = [wf2_average_time_rep,wf1_average_time_rep,5,10,15,20,25,30,35,40]

# ------------------------------------------------------------------

# what-if based graph
def graph2():
  plt.figure(figsize=(5, 4))
  plt.plot(Rep_range, Seconds_range, linewidth=2)
  plt.title("Scale of rep duration")
  plt.xlabel('Rep range')
  plt.ylabel('Seconds range')
  plt.show()

# ------------------------------------------------------------------

progress = input("Would you like to see your progress (Y/N) : ")
if progress == "Y":
  graph2()
  print("\nEnd of Program")
else:
    print("\nEnd of Program")

  