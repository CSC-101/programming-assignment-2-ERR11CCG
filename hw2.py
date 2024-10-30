import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: Point, p2: Point) -> Rectangle:
    top_left_x = min(p1.x, p2.x)
    top_left_y = max(p1.y, p2.y)
    bottom_right_x = max(p1.x, p2.x)
    bottom_right_y = min(p1.y, p2.y)
    top_left = Point(top_left_x, top_left_y)
    bottom_right = Point(bottom_right_x, bottom_right_y)
    return Rectangle(top_left, bottom_right)

# Part 2
    def shorter_duration_than(d1: Duration, d2: Duration) -> bool:
    total_seconds_d1 = d1.minutes * 60 + d1.seconds
    total_seconds_d2 = d2.minutes * 60 + d2.seconds
    return total_seconds_d1 < total_seconds_d2


# Part 3
def songs_shorter_than(songs: list[Song], max_duration: Duration) -> list[Song]:
    shorter_songs = []
    for song in songs:
        if shorter_duration_than(song.duration, max_duration):
            shorter_songs.append(song)
    return shorter_songs


# Part 4
def running_time(songs: list[Song], playlist: list[int]) -> Duration:
    total_minutes = 0
    total_seconds = 0
    for song_index in playlist:
        if 0 <= song_index < len(songs):
            song_duration = songs[song_index].duration
            total_minutes += song_duration.minutes
            total_seconds += song_duration.seconds
    total_minutes += total_seconds // 60
    total_seconds = total_seconds % 60

    return Duration(total_minutes, total_seconds)


# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    for i in range(len(route) - 1):
        city1, city2 = route[i], route[i + 1]
        
        if [city1, city2] not in city_links and [city2, city1] not in city_links:
            return False
    
    return True


# Part 6
from typing import List, Optional

def longest_repetition(numbers: List[int]) -> Optional[int]:
    if not numbers:
        return None
    
    max_length = 1
    max_start_index = 0
    current_length = 1
    current_start_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = current_start_index
            current_length = 1
            current_start_index = i

   
    if current_length > max_length:
        max_length = current_length
        max_start_index = current_start_index

    return max_start_index
