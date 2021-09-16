# Capitol Maps: Find your way around D.C.!

white_house_latitude = 38.897789 
white_house_longitude = -77.036562
downing_hall_latitude =	38.921669
downing_hall_longitude = -77.021361
union_station_latitude = 38.897698
union_station_longitude = -77.007200
dupont_circle_latitude = 38.909760
dupont_circle_longitude = -77.043479
k_street_latitude = 38.902649

your_location_latitude = float(input("Insert your latitude: "))
your_location_longitude = float(input("Insert your longitude: "))

#if latitude of your location > latitude of point X, you are north of point X 
#if latitude of your location < latitude of point X, you are south of point X
#if longitude of your location > longitude of point X, you are east of point X
#if longitude of your location < longitude of point X, you are west of point X

if your_location_latitude > k_street_latitude :
    print ("You are north of K St")
elif your_location_latitude < k_street_latitude :
    print ("You are south of K St")
else:
    print ("")
    
if your_location_latitude > white_house_latitude :
    print ("You are north of the White House")
elif your_location_latitude < white_house_latitude :
    print ("You are south of the White House")
else:
    print ("")
    
if your_location_longitude > white_house_longitude :
    print ("You are east of the White House")
elif your_location_longitude < white_house_longitude :
    print ("You are west of the White House")
else:
    print ("")

if your_location_latitude > downing_hall_latitude :
    print ("You are north of Downing Hall")
elif your_location_latitude < downing_hall_latitude :
    print ("You are south of Downing Hall")
else:
    print ("")
    
if your_location_longitude > downing_hall_longitude :
    print ("You are east of Downing Hall")
elif your_location_longitude < downing_hall_longitude :
    print ("You are west of Downing Hall")
else:
    print ("")

if your_location_latitude > dupont_circle_latitude :
    print ("You are north of Dupont Circle")
elif your_location_latitude < dupont_circle_latitude :
    print ("You are south of Dupont Circle")
else:
    print ("")
    
if your_location_longitude > dupont_circle_longitude :
    print ("You are east of Dupont Circle")
elif your_location_longitude < dupont_circle_longitude :
    print ("You are west of Dupont Circle")
else:
    print ("")
if your_location_latitude > union_station_latitude :
    print ("You are north of Union Station")
elif your_location_latitude < union_station_latitude :
    print ("You are south of Union Station")
else:
    print ("")
    
if your_location_longitude > union_station_longitude :
    print ("You are east of Union Station")
elif your_location_longitude < union_station_longitude :
    print ("You are west of Union Station")
else:
    print ("")
    
#calculating distance from downing hall
#if 1 degree latitude is equivalent to 69 miles, 1 mile difference is caused by 1/69 degrees difference in latitudes 
#if 1 degree latitude is equivalent to 69 miles, 1 mile difference is caused by 1/53 degrees difference in longitudes 

latitude_difference = your_location_latitude - downing_hall_latitude
longitude_difference = your_location_longitude - downing_hall_longitude

distance_latitude_wise = latitude_difference * 69
distance_longitude_wise = longitude_difference * 53

total_distance = ((distance_latitude_wise)**2 + (distance_longitude_wise)**2)**0.5
total_distance = round(total_distance,1)
upper_limit = round(total_distance + 0.1,1)
lower_limit = round(total_distance - 0.1,1)
print (f"You are {total_distance} miles from Downing Hall")
