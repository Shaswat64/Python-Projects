# Library Management

# Create:

# Book
# BorrowedBook(Book)
# LateBorrowedBook(BorrowedBook)

# Requirements:

# Store book details.
# BorrowedBook stores borrowed days.
# LateBorrowedBook calculates late fine.
# Create methods to:
# calculate fine
# display borrowing summary
# calculate total payment
# Ensure fine is charged only after the allowed borrowing period.


# Library Management System (Detailed Explanation)

# You need to create three classes using multilevel inheritance.

# Book
#    ↓
# BorrowedBook
#    ↓
# LateBorrowedBook

# Each child class inherits everything from its parent and adds new attributes and behaviors.


from datetime import datetime


class Book:
    def __init__(self, title, author, ISBNum, price):
        self.title = title
        self.author = author
        self.ISBN = ISBNum
        self.price = price


class BorrowedBook(Book):
    def __init__(
        self,
        title,
        author,
        ISBNum,
        price,
        borrowedBy,
        borrowedOn,
        dueDate,
        allowedDays,
    ):
        self.borrower_name = borrowedBy
        self.borrow_date = borrowedOn
        self.due_date = dueDate
        self.allowed_days = allowedDays
        super().__init__(title, author, ISBNum, price)


class LateBorrowedBook(BorrowedBook):
    def __init__(
        self,
        title,
        author,
        ISBNum,
        price,
        borrowedBy,
        borrowedOn,
        dueDate,
        allowedDays,
        returnDate,
        fine_,
        damage,
    ):

        self.return_date = returnDate
        self.fine_per_day = fine_
        self.damage_charge = damage
        self.total_fine = 0
        self.total_amount = 0
        super().__init__(
            title,
            author,
            ISBNum,
            price,
            borrowedBy,
            borrowedOn,
            dueDate,
            allowedDays,
        )

    def lateDays(self):
        due_date = datetime.strptime(self.due_date, "%Y-%m-%d")
        return_date = datetime.strptime(self.return_date, "%Y-%m-%d")
        actual_late_days = (return_date - due_date).days
        fine_days = max(0, actual_late_days - self.allowed_days)
        self.fine_days = fine_days
        return max(0, fine_days)

    def fine(self):
        late_days = self.lateDays()
        self.total_fine = late_days * self.fine_per_day
        return self.total_fine

    def total_payment(self):
        self.fine()
        self.total_amount = self.total_fine + self.damage_charge
        return self.total_amount

    def display_summary(self):
        self.lateDays()
        self.total_payment()
        return f"""

             ______BOOK INFORMATION______
                Title : {self.title}
                Author: {self.author}
                ISBN  : {self.ISBN}
                PRICE : {self.price}

                
              ____BORROWER INFORMATION_____
                Borrower name: {self.borrower_name}
                Borrowed date: {self.borrow_date}
                Late Days    : {self.fine_days}
                Due date     : {self.due_date}
                Return date  : {self.return_date}
                Total fine   : {self.total_fine}
                Damage charge: {self.damage_charge}
                Total payment: {self.total_amount}
            """


obj = LateBorrowedBook(
    "Muna Madan",
    "Laxmi Prasad Devkota",
    1234,
    670,
    "Mahedra Sapkota",
    "2026-06-03",
    "2026-06-20",
    10,
    "2026-07-23",
    230,
    30,
)

print(obj.display_summary())
