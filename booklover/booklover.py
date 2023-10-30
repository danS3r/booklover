import pandas as pd

class BookLover:
    '''Create a BookLover object'''

    def __init__(self, name, email, fav_genre, num_books=0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]}) ):
            
            self.name = str(name)
            self.email = str(email)
            self.fav_genre = str(fav_genre)
            self.num_books = int(num_books)
            self.book_list = book_list
            
            
    def add_book(self, book_name, rating):
        
        assert isinstance(book_name, str), "Expected string for name."
        book_rating = int(rating)
        
        if ((rating < 0) | (rating > 5)):
            print(f"{rating} is outside bounds! Please rate 0 to 5.")
        else:
        
            if any(self.book_list.book_name == book_name):
                print(f"{book_name} already exists in the list.")
            else:
                new_book = pd.DataFrame({
                    'book_name': [book_name], 
                    'book_rating': [book_rating]
                })

                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
       
            
    def has_read(self, book_name):
            
        assert isinstance(book_name, str), "Name not a string"
            
        if any(self.book_list.book_name == book_name):
            #print(f"{book_name} is in the book list.")
            return True
        else:
            return False
            
            
    def num_books_read(self):
            
        return self.book_list.shape[0]
    
            
    def fav_books(self):
            
        favs = self.book_list[self.book_list['book_rating'] > 3]
            
        return favs
    
            
        