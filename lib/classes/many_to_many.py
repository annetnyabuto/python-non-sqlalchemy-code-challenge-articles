class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return getattr(self, '_author', None)
    
    @author.setter
    def author(self, value):
        if value.__class__.__name__ != 'Author':
            raise TypeError("Author must be of type Author")
        self._author = value
    
    @property
    def magazine(self):
        return getattr(self, '_magazine', None)
    
    @magazine.setter
    def magazine(self, value):
        if value.__class__.__name__ != 'Magazine':
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type string")
        if not name:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name 
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list({article.magazine for article in Article.all if article.author == self})
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        categories = {article.magazine.category for article in Article.all if article.author == self}
        return list(categories) if categories else None
    
class Magazine:
    all = []
    
    def _validate_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
    
    def _validate_category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be of type str")
        if not value:
            raise ValueError("Category must be longer than 0 characters")
    
    def __init__(self, name, category):
        self._validate_name(name)
        self._validate_category(category)
        self._name = name
        self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._validate_category(value)
        self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})
    
    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None
    
    def contributing_authors(self):
        author_counts = {}
        for article in Article.all:
            if article.magazine == self:
                author_counts[article.author] = author_counts.get(article.author, 0) + 1
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_counts = {}
        for article in Article.all:
            magazine_counts[article.magazine] = magazine_counts.get(article.magazine, 0) + 1
        return max(magazine_counts, key=magazine_counts.get)