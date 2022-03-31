import requests, os, bs4
import pyinputplus as pypi

class ImgurImgDownloader:

    def __init__(self, search, num_saves=None):
        self.search = search
        self.url = 'https://imgur.com/'
        self.num_saves = num_saves

    def main(self):
        self.dir = os.makedirs('imgur_imgs', exist_ok=True)        
        self.search_topic()
        self.find_imgs()
        self.how_much()
        
        if not len(self.photos_elem) < 1:            
            self.download_imgs()
        else:
            print('No images were found.')
   
    def search_topic(self):
        self.topic_url = f'https://imgur.com/search/score?q={self.search}'
        res = requests.get(self.topic_url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    def find_imgs(self):
        self.photos_elem = self.soup.select('.image-list-link img')

    def how_much(self):
        if self.num_saves == None or self.num_saves > len(self.photos_elem):
            self.num_saves = len(self.photos_elem)

    def download_imgs(self):
        for index in range(self.num_saves):
            try:
                img_url = 'https:' + self.photos_elem[index].get('src')
                print(f'Downloading image {img_url}...')
                res_img = requests.get(img_url)
                
                res_img.raise_for_status()
            except requests.exceptions.MissingSchema:
                continue
            else:
                self.save_img(res_img, img_url)

    def save_img(self, res_img, img_url):        
        try:
            image_file = open(os.path.join('imgur_imgs', os.path.basename(img_url)), 'wb')            
            for chunk in res_img.iter_content(100000):
                image_file.write(chunk)            
            image_file.close()
        except:
            print('Error saving file')            
        else:
            print('File stored successfully')
        
            
if __name__ == '__main__':
    search = pypi.inputStr(prompt='Enter the TOPIC you wanna search for: ')
    times = pypi.inputInt(prompt='[01-60]How many IMGS you want: ', min=1, lessThan=61)
    
    spam = ImgurImgDownloader(search, times)
    spam.main()