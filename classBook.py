class Bookstore:
    def __init__(self,  book_title, author, price, no):
        self.book = book_title
        self.author  = author
        self.price = price
        self.no = no

    def get_book(self):
        return f"{self.book}  |  {self.author}  |  {self.price}  |  {self.no}"
        
def books():
    book_1 = Bookstore("The Subtle Art Of Not Giving a f*ck", "Mark Mason", 299, 200)
    book_2 = Bookstore("Programming with C", "Byron Gottfried" , 500, 12)
    book_3 = Bookstore("The Diary of Anne Frank","Anne Frank", 359, 300 ) 
    Bookst = [book_1, book_2, book_3]

    for book in Bookst:
        
        print(book.get_book())
        print("----------------------------------------------------------------")

books()

