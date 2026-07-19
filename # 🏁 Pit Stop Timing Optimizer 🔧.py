# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️

race_time_in_minut = float(input("write the race time = "))
total_pit = float(input("write the total pit = "))
avg_pit_stop_in_minut = float(input("write the avg stop pit = "))
#then
total_pit_stop_time = total_pit * avg_pit_stop_in_minut
presentage_of_race_spent_in_pit = round((total_pit_stop_time / race_time_in_minut) * 100 , 2 )
#final
print(f""" hi bro there is your
 Total pit stop time in minuts  = {total_pit_stop_time} 
 Percentage of race time spent in pits = {presentage_of_race_spent_in_pit}""")
#if
if presentage_of_race_spent_in_pit > 5 :
    print("You need a new pit crew")    
