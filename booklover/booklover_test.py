import unittest
import pandas as pd
    
import booklover

class BookLoverTestSuite(unittest.TestCase):
    '''module for testing BookLover'''

    
    def test_1_add_book(self):
        '''add a book and test if it is in `book_list`'''
        
        book_name = "War of the Worlds"
        rating = 4
        
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book(book_name, rating)
        print(test_object.book_list)
        
        #test
        self.assertTrue(any(test_object.book_list.book_name == book_name))
        
        
    def test_2_add_book(self):
        
        '''add the same book twice. Test if it's in `book_list` only once.'''
        
        book_name = "War of the Worlds"
        rating = 4
        
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book(book_name, rating)
        test_object.add_book(book_name, rating)
        
        #test
        expected = 1
        self.assertEqual(test_object.book_list[test_object.book_list['book_name'] == book_name].shape[0], expected)
        
        
    def test_3_has_read(self):
        '''pass a book in the list and test if the answer is `True`.'''
        
        # test independent of add_book
        test_list = pd.DataFrame({'book_name':["Jane Eyre", "Fight Club"], 'book_rating':[4, 3]})
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi", 2, test_list)
        
        # test
        self.assertTrue(test_object.has_read("Jane Eyre"))
        
        
    def test_4_has_read(self):
        '''Pass a book NOT in the list and use assert False to test if the answer is True'''
        
        # test independent of add_book
        test_list = pd.DataFrame({'book_name':["Jane Eyre", "Fight Club"], 'book_rating':[4, 3]})
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi", 2, test_list)
        
        # test
        self.assertFalse(test_object.has_read("War of the Worlds"))
        
    
    def test_5_num_books_read(self):
        '''Add some books to the list, and test num_books matches expected.'''
        
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        
        #test
        expected = 2
        self.assertEqual(test_object.num_books_read(), expected)
        
        
    def test_6_fav_books(self):
        '''Add some books with ratings to the list, making sure some of them have rating > 3. '''
        
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("Memo", 1)
        
        #test
        favs = test_object.fav_books()
        
        self.assertFalse(any(favs.book_rating < 4))
        
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)