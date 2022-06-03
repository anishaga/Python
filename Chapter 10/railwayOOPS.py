class RailwayForm:
    formType = "Railway Form"
    def printData(self):
        print(f"Passenger Name Is: {self.name}")
        print(f"Train Is: {self.train}")


harryApplication = RailwayForm()
harryApplication.name = "Harry"
harryApplication.train = "Rajdhani Express"

harryApplication.printData()
