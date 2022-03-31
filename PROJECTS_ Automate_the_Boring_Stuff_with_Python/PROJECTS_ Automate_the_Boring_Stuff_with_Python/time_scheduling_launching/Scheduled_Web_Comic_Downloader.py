# Go to a webcomic and download all the images you don't already have on your computer

import requests, os, bs4, datetime, shelve, re

      
def go_to_previous_page(soup_obj):
    back_button = soup_obj.select('.prev a')
    if back_button == []:        
            print('End of pages.')
            return None
    else:        
        previous_page = 'http://www.lefthandedtoons.com' + back_button[0].get('href')
        return previous_page

def get_comic_date(soup_obj):
    '''extract from the page the image publication date'''
    try:
        comic_date = soup_obj.select('.comictitlearea')
        complet_comic_title = comic_date[0].getText()
        comic_date = re.search('\w+ \d+, \d{4}', complet_comic_title)    
        comic_date_obj = datetime.datetime.strptime(comic_date.group(), '%B %d, %Y')  
        return comic_date_obj
    except:
        return None

def get_shelf_date(shelf_obj):    
    '''loads from the computer the date of the most recent image downloaded'''
    try:
        date = shelf_obj['date']
    except KeyError:
        return None   
    return date

def download_image(soup_obj):
    '''download image from the webpage'''
    img_class = soup_obj.select('.comicimage')
    try:
        img_url = img_class[0].get('src')
        # Download the image.
        print(f'Downloading image {img_url}...')
        res = requests.get(img_url)
        res.raise_for_status()
    except requests.exceptions.MissingSchema:        
        print(f'ERROR TO DOWNLOAD: {img_url}')
    else:
        # Save the image to comics
        imageFile = open(os.path.join('comics', os.path.basename(img_url)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

url = 'http://www.lefthandedtoons.com/' # starting url
os.makedirs('comics', exist_ok=True) # store comics in
dates = []
comic_shelf = shelve.open('comic')
while url != None: 
    # Download the page.    
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    # Create soup object
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    
    page_date = get_comic_date(soup)
    shelf_date = get_shelf_date(comic_shelf)    
    dates.append(page_date)
    
    if shelf_date == None or page_date > shelf_date:
        download_image(soup)
        url = go_to_previous_page(soup)
    else:
        print('No news comics.')
        break
    
    
comic_shelf['date'] = dates[0] 
comic_shelf.close()