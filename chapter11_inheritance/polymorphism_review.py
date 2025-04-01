class Media:
    def __init__(self, filename):
        self._filename = filename
    
    def display(self):
        print(f"Displaying media: {self._filename}")

class Audio(Media):
    def display(self):
        print(f"Playing audio: {self._filename}")

class Video(Media):
    def display(self):
        print(f"Playing video: {self._filename}")

class Image(Media):
    def display(self):
        print(f"Displaying image: {self._filename}")

media_items = [
    Audio("song.mp3"),
    Video("movie.mp4"),
    Image("picture.jpg")
]

for item in media_items:
    item.display()