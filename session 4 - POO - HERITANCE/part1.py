
class Form:
    color = "No color"
    coordinatesX = 0
    coordinatesY = 0
    name = 'Form'
    
    def prntForm(self):
        print(self.name,"data: \n""color:",self.color,"\n" "coordinates:","(",self.coordinatesX,",",self.coordinatesY,")")
        
    def updateColor(self, color):
        self.color = color
    
    def updateCoordinates(self, coordinatesX, coordinatesY):
        self.coordinatesX = coordinatesX
        self.coordinatesY = coordinatesY
        
class Rectangle(Form):
    biggestSide = 0
    smallerSide = 0
    name = 'Rectangle'
    
    def prntRectangle(self):
        print(Form.prntForm(self),"Biggest sides: ",self.biggestSide,"\n""smaller sides:",self.smallerSide)
    
    def areaRectangle(self):
        return self.biggestSide * self.smallerSide
    
    def perimeterRectangle(self):
        return( self. biggestSide * 2 ) * ( self.smallerSide * 2 )
    
    def prntAreaRectangle(self):
        print("Rectangle area: ",self.areaRectangle())
        
    def prntPerimeterRectangle(self):
        print("Rectangle perimeter: ",self.perimeterRectangle())
        
    def escale(self, escale):
        self.biggestSide = self.biggestSide * escale
        self.smallerSide = self.smallerSide * escale
        

class Square(Rectangle):
    sideSquare = 0
    name = 'Square'
    
    def prntSquare(self):
        print(Rectangle.prntForm(self),self.name,"side:",self.sideSquare,"each side")
    
    def areaSquare(self):
        return self.sideSquare**2
    
    def perimeterSquare(self):
        return self.sideSquare*4
    
    def prntAreaSquare(self):
        print("Square area: ",self.areaSquare())
        
    def prntPerimeterSquare(self):
        print("Square perimeter: ",self.perimeterSquare())
        
    def escale(self, escale):
        self.biggestSide = self.biggestSide * escale
        self.smallerSide = self.smallerSide * escale
        
form1 = Form()
form2 = Rectangle()
form3 = Square()

form1.updateColor('green')
form1.updateCoordinates(3,5)
form1.prntForm()

form2.updateColor('blue')
form2.biggestSide = 4
form2.smallerSide = 4
form2.updateCoordinates(5,7)
# form2.perimeterRectangle()
# form2.areaRectangle()
form2.prntRectangle()
form2.prntAreaRectangle()
form2.prntPerimeterRectangle()


form3.updateColor('red')
form3.updateCoordinates(6,9)
form3.sideSquare = 8
# form3.areaSquare()
# form3.perimeterSquare()
form3.prntSquare()
form3.prntAreaSquare()
form3.prntPerimeterSquare()

