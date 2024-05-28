#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    author_1 = Author("Carry Bradshaw")
    author_2 = Author("Nathaniel Hawthorne")
    magazine_1 = Magazine("Vogue", "Fashion")
    Article(author_1, magazine_1, "How to wear a tutu with style")
    Article(author_2, magazine_1, "Dating life in NYC")
    print(magazine_1.contributors())
    print(magazine_1.article_titles())
    print(magazine_1.contributing_authors())
    print(Magazine.top_publisher())
    

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
