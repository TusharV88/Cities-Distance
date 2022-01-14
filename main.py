# Find the distance between two cities
from geopy.geocoders import Nominatim
from geopy import distance


# Google Maps
def maps_dir(startPoint, destPoint):
    
    try:
        geocoder = Nominatim(user_agent='Nuvia')

        start_coord = geocoder.geocode(startPoint)
        dest_coord = geocoder.geocode(destPoint)
        print('Start : ', start_coord)
        print('Destination : ', dest_coord)


        start_location = (start_coord.latitude, start_coord.longitude) 
        dest_location = (dest_coord.latitude, dest_coord.longitude) 
        total = distance.great_circle(start_location, dest_location).km
        print(f'Total Distance :  {round(total, 2)}Km')

        # return round(total, 2)

    except Exception as e:
        return 'none'


maps_dir('new delhi', 'mumbai')




