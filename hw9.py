class Rectangle :
    def __init__(self, x1=0, y1=0, x2=0, y2=0) :
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def show (self) :
        print(f'좌측 상단 꼭지점이 ({self.__x1}, {self.__y1})이고 ', end ='')
        print(f'우측 하단 꼭지점이 ({self.__x2},{self.__y2})인 사각형입니다.', end ='')
    
    def getWidth(self) :
        if self.__x2 - self.__x1 < 0:
            return self.__x1 - self.__x2
        return self.__x2 - self.__x1
    
    def getHeight(self) :
        if self.__y1 - self.__y2 < 0 :
            return self.__y2 - self.__y1
        return self.__y1 - self.__y2  

    def getArea(self) :
        return self.getWidth() * self.getHeight()     
    
    def getPerimeter(self) :
        return 2 * (self.getWidth() + self.getHeight()) 
    
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')