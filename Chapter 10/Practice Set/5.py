class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        list1 = []
        for i in range (1,seats+1):
            list1.append(i)
        self.seats = list1

    def getStatus(self):
        print(f"No. Of Seats Available In {self.name} Are: {len(self.seats)}")
    
    def getFare(self):
        print(f"Fare Of {self.name} Is: {self.fare}")

    def bookSeat(self,customerName):
        if(len(self.seats) > 0):
            print(f"***Thank You {customerName}, Your Ticket Is Booked Successfully***")
            print(f"\t\tYour Seat Number Is: {self.seats[-1]} ")
            print("\t\t  Happy Journey")
            self.seats.remove(self.seats[-1])
        else:
            print("Sorry The Train Is Fully Booked, Kindly Try In Tatkal")

    def cancelSeat(self,seatNum):
        if seatNum in self.seats:
            print("***Kindly Check Your Seat Number And Try Again***")
            print(f"No Booking Found For Seat Number {seatNum}.")  
        else:
            self.seats.append(seatNum)
            print("***Your Ticket Is Cancelled Successfully***")


train1 = Train("Gareeb Rath",1000,10)
# train2 = Train("Bombay Local",100,1000)
# train3 = Train("Maharaja Express",15000,45)

train1.getStatus()
train1.getFare()

train1.bookSeat("Anish")
train1.bookSeat("Anshu")
train1.bookSeat("Pratik")

train1.cancelSeat(9)

