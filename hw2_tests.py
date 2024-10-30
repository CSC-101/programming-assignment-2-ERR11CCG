import data
import hw2
import unittest


# Write your test cases for each part below.
#Part 1 
 
class TestCases(unittest.TestCase):
p1 = Point(2, 2)
p2 = Point(10, 10)
rectangle = create_rectangle(p1, p2)
print(rectangle)

p1 = Point(3, 5)
p2 = Point(8, 5)
rectangle = create_rectangle(p1, p2)
print(rectangle)

    # Part 2
d1 = Duration(3, 20)  
d2 = Duration(4, 0)   
print(shorter_duration_than(d1, d2))  

d3 = Duration(5, 0)
d4 = Duration(4, 30)
print(shorter_duration_than(d3, d4))  


    # Part 3
song1 = Song("Artist1", "Song1", Duration(3, 30))
song2 = Song("Artist2", "Song2", Duration(2, 45))
song3 = Song("Artist3", "Song3", Duration(4, 10))
songs_list = [song1, song2, song3]

max_duration = Duration(3, 0)

short_songs = songs_shorter_than(songs_list, max_duration)
print(short_songs)


    # Part 4
song1 = Song("Decemberists", "June Hymn", Duration(4, 30))
song2 = Song("Broken Bells", "October", Duration(3, 40))
song3 = Song("Kansas", "Dust in the Wind", Duration(3, 29))
song4 = Song("Local Natives", "Airplanes", Duration(3, 58))

songs_list = [song1, song2, song3, song4]


playlist = [0, 2, 1, 3, 0]  


total_duration = running_time(songs_list, playlist)
print(total_duration)
 


    # Part 5

city_links = [
    ['san luis obispo', 'santa margarita'],
    ['san luis obispo', 'pismo beach'],
    ['atascadero', 'santa margarita'],
    ['atascadero', 'creston']
]
route = ['san luis obispo', 'santa margarita', 'atascadero']
print(validate_route(city_links, route))  


route = ['san luis obispo', 'atascadero']
print(validate_route(city_links, route))  


    # Part 6





if __name__ == '__main__':
    unittest.main()
