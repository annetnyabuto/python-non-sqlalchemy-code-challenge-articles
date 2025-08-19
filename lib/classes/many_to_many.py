class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name 
    
    @property
    def name(self):
        return self._name # name can not change after author is instantiated
    
    def articles(self):
        pass
    class Magazine:
        def __init__(self, name, category):
            self.name = name
            self.category = category
        @property
        def name(self):
            self._name
        @name.setter
        def name(self, value):
            if not isinstance(value, str):
                raise TypeError("Name must be of type str")
            if not(2 <= len(value) <= 16):
                raise ValueError("Name must be between 2 and 16 characters")
            self._name = value  

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass