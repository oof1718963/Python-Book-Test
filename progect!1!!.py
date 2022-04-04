class book: 
    def __init__(self, name,year,author,price):
        self.book_name = name
        self.book_year = year
        self.book_author = author
        self.book_price = price
        
        
    def add_book(self):
        
        print("Name : " + self.book_name)
        print("Year : " + str(self.book_year))
        print("Author : " + self.book_author)
        print("Price : " + str(self.book_price))
        print("Book added")
        print("                                                                      ")
        print("______________________________________________")
        print("                                                                      ")
        
book1 = book("Big Shot","October 26, 2021","Jeff Kinney","7.50$")
book1.add_book()

book2 = book("Big Nate Strikes Again","March 10, 2015","Lincoln Peirce","4.50$")
book2.add_book()
