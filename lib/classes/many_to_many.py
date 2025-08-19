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
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        areas = [magazine.category for magazine in self.magazines()]
        return list(set(areas)) if areas else None
    
class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not(2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value 
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be of type str")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value
    
    