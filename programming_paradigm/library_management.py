class Book :
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_cheked_out = False

    def borrow(self):
        if not self.is_cheked_out:
            self.is_cheked_out = True
            return True
        return False

    def return_book(self):
        if self.is_cheked_out:
            self.is_cheked_out = False
            return True
        return False