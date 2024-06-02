class Article:
    # Class variable to store all instances of Article
    all = []
    
    def __init__(self, author, magazine, title):
        # Instance variables for author, magazine, and title
        self.author = author
        self.magazine = magazine
        self.title = title
        # Append the new article to the class variable 'all'
        Article.all.append(self)

    @property
    def title(self):
        # Getter for the title property
        return self._title

    @title.setter
    def title(self, value):
        # Setter for the title property
        # Check if value is a string and the title has not been set before
        if isinstance(value, str) and not hasattr(self, 'title'):
            self._title = value

class Author:
    
    def __init__(self, name):
        # Instance variable for the name of the author
        self.name = name
  
    @property
    def name(self):
        # Getter for the name property
        return self._name
    
    @name.setter
    def name(self, value):
        # Setter for the name property
        # Check if value is a string and the name has not been set before
        if isinstance(value, str) and not hasattr(self, 'name'):
            self._name = value
        self._name = value 
    
    def articles(self):
        # Returns a list of all articles written by the author
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        # Returns a list of unique magazines the author has written for
        magazine = set([article.magazine for article in self.articles()])
        return list(magazine)

    def add_article(self, magazine, title):
        # Creates a new article written by the author
        return Article(self, magazine, title)

    def topic_areas(self):
        # Returns a list of unique magazine categories the author has written for
        topics = set([article.magazine.category for article in self.articles()]) 
        if len(topics) == 0:
            return None
        else:
            return list(topics)

class Magazine:

    def __init__(self, name, category):
        # Instance variables for the name and category of the magazine
        self.name = name
        self.category = category
        
    @property
    def name(self):
        # Getter for the name property
        return self._name

    @name.setter
    def name(self, value):
        # Setter for the name property
        # Check if the value is a string with length between 2 and 16 characters
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = value  

    def articles(self):
        # Returns a list of all articles in the magazine
        return [article for article in Article.all if article.magazine == self]
    
    @property
    def category(self):
        # Getter for the category property
        return self._category
    
    @category.setter
    def category(self, value):
        # Setter for the category property
        # Check if the value is a non-empty string
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def contributors(self):
        # Returns a list of unique authors who have written for the magazine
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        # Returns a list of titles of all articles in the magazine
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        # Returns a list of authors who have written more than two articles for the magazine
        contr_auth = {article.author for article in self.articles()}
        more_than_two = [author for author in contr_auth if sum(1 for art in self.articles() if art.author == author) > 2]
        if len(more_than_two) > 0:
            return more_than_two
        else:
            return None
