

import math

class Form:
    color = "no color"
    coordinatesX = 0
    coordinatesY = 0
    name = 'Form'
    
    def prntForm(self):
        print(self.name,"color:",self.color,"\n",self.name,"coordinates:","(",self.coordinatesX,",",self.coordinatesY,")")
        
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
        print(self.name,"biggest sides:",self.biggestSide,"\n",self.name,"smaller sides:",self.smallerSide)
    
    def areaRectangle(self):
        return self.biggestSide * self.smallerSide
    
    def perimeterRectangle(self):
        return( self. biggestSide * 2 ) * ( self.smallerSide * 2 )
    
    def prntAreaRectangle(self):
        print(self.name,"area:",self.areaRectangle())
        
    def prntPerimeterRectangle(self):
        print(self.name,"perimeter:",self.perimeterRectangle())
        
    def escale(self, escale):
        self.biggestSide = self.biggestSide * escale
        self.smallerSide = self.smallerSide * escale
        

class Square(Form):
    sideSquare = 0
    name = 'Square'
    
    def prntSquare(self):
        print(self.name,"each side:",self.sideSquare)
    
    def areaSquare(self):
        return self.sideSquare**2
    
    def perimeterSquare(self):
        return self.sideSquare*4
    
    def prntAreaSquare(self):
        print(self.name,"area:",self.areaSquare())
        
    def prntPerimeterSquare(self):
        print(self.name,"perimeter:",self.perimeterSquare())
        
    def escale(self, escale):
        self.biggestSide = self.biggestSide * escale
        self.smallerSide = self.smallerSide * escale
     
     
class Ellipse(Rectangle):
    # biggestSide = 0   = a
    # smallerSide = 0   = b
    def prntEllipse(self):
        print(self.name,"biggest radio:",self.biggestSide,"\n",self.name,"smaller radio:",self.smallerSide)
        
    def areaEllipse(self):
        areaEllipse =  math.pi * self.biggestSide
        return "%.3f" % areaEllipse

    def prntAreaEllipseOrCircle(self):
        if self.biggestSide == self.smallerSide:
            circleArea = math.pi * (self.biggestSide**2)
            circleArea = ("%.3f" % circleArea)
            print('Circle area:',circleArea)
        else:
            print(self.name,"area:",self.areaEllipse())
        
    def perimeterEllipse(self):
        perimeterEllipse = math.pi * ( 3 * ( self.biggestSide + self.smallerSide ) ) - math.sqrt( ( 3 * self.biggestSide ) + self.smallerSide * ( self.biggestSide ) + ( 3 * ( self.smallerSide ) ) )
        return "%.3f" % perimeterEllipse
    
    def prntPerimeterEllipseOrCircle(self):
        if self.biggestSide == self.smallerSide:
            circlePerimeter = (2 * math.pi ) * (self.biggestSide)
            circlePerimeter = "%.3f" % circlePerimeter
            print('Circle perimeter:',circlePerimeter)
            
        else:
            print(self.name,"perimeter:",self.perimeterEllipse())
  

form1 = Form()
form2 = Rectangle()
form3 = Square()
form4 = Ellipse()

# form1.updateColor('green')
# form1.updateCoordinates(3,5)
# form1.prntForm()

# form2.updateColor('blue')
# form2.biggestSide = 4
# form2.smallerSide = 4
# form2.updateCoordinates(5,7)
# form2.prntRectangle()
# form2.prntAreaRectangle()
# form2.prntPerimeterRectangle()


# form3.updateColor('red')
# form3.updateCoordinates(6,9)
# form3.sideSquare = 8
# form3.prntSquare()
# form3.prntAreaSquare()
# form3.prntPerimeterSquare()

form4.name = 'Ellipse'
form4.biggestSide = 100
form4.smallerSide = 100
form4.prntEllipse()
form4.prntAreaEllipseOrCircle()
form4.prntPerimeterEllipseOrCircle()

