#!/usr/bin/env python3

class Book:
    # pass
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    # @property
    # def title(self):
    #     return self._title

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count,(int)):
            self._page_count=page_count
        else:
            print("page_count must be an integer")

    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    #title= property(get_title,set_page_count)
        
    
        