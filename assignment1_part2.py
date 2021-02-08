
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def display(self):
        return self.title + ', written by ' + self.author

book_1 = Book('John Steinbeck', 'Of Mice and Men')
book_2 = Book('Harper Lee', 'To Kill a Mockingbird')

if __name__ == "__main__":
    print(book_1.display())
    print(book_2.display())