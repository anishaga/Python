class Library:
    def __init__(self,bookList):
        self.bookList = bookList

    def displayAvailableBooks(self):
        print(f"Available Books Are As Follows:")
        if len(self.bookList) == 0:
            print("Sorry, No Books Are Available At The Moment :(")
        else:   
            for item in self.bookList:
                print(f"\t\t\t\t• {item}")
 
    def issueBook(self, bookName):
        if bookName in self.bookList:
            print(f"\n\t\t\t\t********* {bookName} Is Issued Succesfully *********")
            print("Please Take Care Of The Book And Return Within 30 Days To Avoid Fine\n")
            bookList.remove(bookName)
        else:
            print("\t\t\t\tSorry, This Book Is Not Available At The Moment :(\n")

    def returnBook(self,bookName):
        if bookName in self.bookList:
            print("This Book Is Not Issued Yet!!")
        else:
            bookList.append(bookName)
            print(f"\t\t\t\t********* {bookName} Is Returned Successfully *********")

class Student:
    def requestBook(self):
        self.bookName = input("Enter Book Name: ")
        return self.bookName
    
    def returnBook(self):
        self.bookName = input("Enter Book Name: ")
        return self.bookName

bookList = ["Mastering Bitcoin","Introduction To Machine Learning","Rich Dad Poor Dad", "Saymin Haykin", "Operating Systems"]
l1 = Library(bookList)
s1 = Student()

print ("****Welcome To Library Management System ****")

while (True):
    try:
        a = int(input('''MAIN MENU:\n\t\t\t\t➢  Enter '0' To Exit\n\t\t\t\t➢  Enter '1' To Get The List Of Available Books\n\t\t\t\t➢  Enter '2' To Get A Book Issued\n\t\t\t\t➢  Enter '3' To Return A Book:\nKindly Enter Your Choice: '''))
        
        if (a==0):
            print("**** Thanks For Using LMS, Have A Nice Day ****")
            break

        elif (a == 1):
            l1.displayAvailableBooks()
            
        elif (a==2):
            l1.issueBook(s1.requestBook())

        elif (a==3):
            l1.returnBook(s1.returnBook())
        else:
            raise Exception
    except Exception as e:
        print("\n!!!!!!!!!! INVALID INPUT !!!!!!!!!!\n")