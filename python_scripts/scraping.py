from wiki import get_song_html

from bs4 import BeautifulSoup

def get_class_contents(song_title,artist, class_name):
    # Get the html
    html= get_song_html(song_title,artist)
    if(html):
        # Parse the HTML
        soup = BeautifulSoup(html, 'html.parser')
        # Find the element with the specified class
        element = soup.find(class_=class_name)
        if element:
            # Get the contents of the element and all its child tags
            contents = element.find_all(text=True, recursive=True)
            return contents
    return None

duration = get_class_contents("Waterloo Sunset","The Kinks", "duration")
# genre = get_class_contents("Waterloo Sunset","The Kinks","genre")
print(duration)
# print(genre)