import requests, bs4
import pyinputplus as pypi

class CheckBrokenLinks:
    '''
    Given the URL of a web page, will attempt to download
    every linked page on the page, and find out which are broken
    '''

    def __init__(self, main_url):
        self.main_url = main_url
        self.urls_to_check = []
        self.broken_links = []

    def main(self):
        '''Call others functions'''
        if self.download_main_page():        
            self.get_links()
            self.complement_links()            
            self.check_valid_links()
            self.print_broken_links()
        else:
            self.invalid_link()

    def download_main_page(self):
        '''Try to download the main page'''
        try:
            res = requests.get(self.main_url)
            res.raise_for_status()
            self.soup = bs4.BeautifulSoup(res.text, 'html.parser')
        except:
            return False
        else:
            return True
    
    def invalid_link(self):
        print(f'INVALID LINK: {self.main_url}')
      
    def get_links(self):
        '''Get all link from the main page'''
        links_a_tag = self.soup.select('a')
        for url in links_a_tag:
            self.urls_to_check.append(url.get('href'))

    def complement_links(self):
        '''Complet partial links'''
        for index, url in enumerate(self.urls_to_check):
            if not url.startswith('http'):
                self.urls_to_check[index] = f'{self.main_url}/{url}'

    def check_valid_links(self):
        '''search for invalid links'''
        for url in self.urls_to_check:
            print(f'CHECKING: {url}...')
            res = requests.get(url)
            if res.status_code == 404:
                self.broken_links.append(url)
    
    def print_broken_links(self):        
        '''Print result'''
        if self.broken_links:
            print('\nTHESE ARE THE BROKEN LINKS:')
            for broken_link in self.broken_links:
                print(f'BROKEN LINK: {broken_link}')
        else:
            print('\nTHERE ARE NO BROKEN LINKS ON THIS WEB PAGE!')

if __name__ == '__main__':
    url = pypi.inputStr(prompt='ENTER FULL LINK: ')
    execute = CheckBrokenLinks(url)
    execute.main()