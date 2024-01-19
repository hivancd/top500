import wikipedia

def get_song_html(song_title, artist):
    try:
        # Construct the page title
        page_title = f"{song_title} {artist} song"
        
        # Search for the page
        search_results = wikipedia.search(page_title)
        if (len(search_results) != 0):
            # Get the page
            # print(search_results)
            
            page = wikipedia.page(search_results[0])
            print(page)
            return(page.html())
        else:
            return None
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation pages
        # You can either ignore them or handle them as per your requirement
        print('\n\n\ndisambiguation\n\n\n')
        return None
    except wikipedia.exceptions.PageError as e:
        # Handle page not found error
        print('\n\n\npage not found\n\n\n')
        return None

# Example usage
# song_title = "Bad guy"
# artist = "Billie Eilish"
# html = get_song_html(song_title, artist)
# print(html)
