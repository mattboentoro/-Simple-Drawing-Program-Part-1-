import re
import sys
import math

class Drawing:
    def Linewidth(self,Amount):
        print(Amount+" setlinewidth")
    def Color(self,R,G,B):
        print(R+" "+G+" "+B+" setrgbcolor")
    def RotatePoints(self,X,Y,OriX,OriY,Degree):
        Result1=OriX+math.cos(math.radians(Degree))*(X-OriX)-math.sin(math.radians(Degree))*(Y-OriY)
        Result2=OriY+math.sin(math.radians(Degree))*(X-OriX)+math.cos(math.radians(Degree))*(Y-OriY)
        return Result1,Result2
    def RotateTranslateScale(self,X,Y,Transformation):
        Index=len(Transformation)-1
        while len(Transformation)>0:
            if (Transformation[Index]=="rotate"):
                for i in range(len(X)):
                    Result1,Result2=self.RotatePoints(X[i],Y[i],float(0),float(0),float(Transformation[Index+1]))
                    X[i]=Result1
                    Y[i]=Result2
                for i in range(2):
                    Transformation.pop()
                Index=len(Transformation)-1
            elif (Transformation[Index]=="translate"):
                for i in range(len(X)):
                    Result=X[i]+float(Transformation[Index+1])
                    X[i]=float(Result)
                    Result=Y[i]+float(Transformation[Index+2])
                    Y[i]=float(Result)
                for i in range(3):
                    Transformation.pop()
                Index=len(Transformation)-1
            elif (Transformation[Index]=="scale"):
                for i in range(len(X)):
                    Result=float(Transformation[Index+1])*(X[i])
                    X[i]=float(Result)
                    Result=float(Transformation[Index+1])*(Y[i])
                    Y[i]=float(Result)
                for i in range(2):
                    Transformation.pop()
                Index=len(Transformation)-1
            else:
                Index-=1
        print(str(X[0])+" "+str(Y[0])+" "+"moveto")
        for i in range(1,len(X)):
            print(str(X[i])+" "+str(Y[i])+" "+"lineto")
        if len(X)>2:
            print(str(X[0])+" "+str(Y[0])+" "+"lineto")
    def Rect(self,X,Y,Width,Height,Transformation,Fill):
        FinalLinePointsX=[]
        FinalLinePointsY=[]
        FinalLinePointsX.append(X)
        FinalLinePointsY.append(Y)
        FinalLinePointsX.append(FinalLinePointsX[len(FinalLinePointsX)-1]+Width)
        FinalLinePointsY.append(FinalLinePointsY[len(FinalLinePointsY)-1])
        FinalLinePointsX.append(FinalLinePointsX[len(FinalLinePointsX)-1])
        FinalLinePointsY.append(FinalLinePointsY[len(FinalLinePointsY)-1]+Height)
        FinalLinePointsX.append(FinalLinePointsX[len(FinalLinePointsX)-1]-Width)
        FinalLinePointsY.append(FinalLinePointsY[len(FinalLinePointsY)-1])
        self.RotateTranslateScale(FinalLinePointsX,FinalLinePointsY,Transformation)
        if (Fill==True):
            print("fill")
        else:
            print("stroke")
    def Line(self,X1,Y1,X2,Y2,Transformation):
        FinalLinePointsX=[]
        FinalLinePointsY=[]
        FinalLinePointsX.append(X1)
        FinalLinePointsX.append(X2)
        FinalLinePointsY.append(Y1)
        FinalLinePointsY.append(Y2)
        self.RotateTranslateScale(FinalLinePointsX,FinalLinePointsY,Transformation)
    def Tri(self,X,Y,R,Transformation,Fill):
        self.Ngon(X,Y,R,3,Transformation,Fill)
    def Square(self,X,Y,R,Transformation,Fill):
        self.Ngon(X,Y,R,4,Transformation,Fill)
    def Penta(self,X,Y,R,Transformation,Fill):
        self.Ngon(X,Y,R,5,Transformation,Fill)
    def Hexa(self,X,Y,R,Transformation,Fill):
        self.Ngon(X,Y,R,6,Transformation,Fill)
    def Ngon(self,X,Y,R,N,Transformation,Fill):
        FinalLinePointsX=[]
        FinalLinePointsY=[]
        FinalLinePointsX.append(X+R)
        FinalLinePointsY.append(Y)
        Degree=360/int(N)
        for i in range(1,int(N)):
            Xnew,Ynew=self.RotatePoints(FinalLinePointsX[i-1],FinalLinePointsY[i-1],X,Y,Degree)
            FinalLinePointsX.append(Xnew)
            FinalLinePointsY.append(Ynew)
        self.RotateTranslateScale(FinalLinePointsX,FinalLinePointsY,Transformation)
        if (Fill==True):
            print("fill")
        else:
            print("stroke")
def Tokenize(command):
    Token1=[]
    for i in range (0,len(command)):
        command[i]=command[i].replace("("," ")
        command[i]=command[i].replace(")"," ")
    for i in range (0,len(command)):
        a=command[i].split()
        for i1 in range(0,len(a)):
            Token1.append(a[i1])
    return Token1
def Draw(command):
    print("%!PS-Adobe-3.1")
    Array=[]
    Transformation=[]
    Index=0
    Token=Tokenize(command)
    DrawCommand=Drawing()
    while len(Token)>0:
        if (Token[0]=="linewidth"):
            DrawCommand.Linewidth(Token[1])
            for i in range(2):
                Token.pop(0)
        elif(Token[0]=="color"):
            DrawCommand.Color(Token[1],Token[2],Token[3])
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="rotate"):
            Transformation.append("rotate")
            Transformation.append(Token[1])
            for i in range(2):
                Token.pop(0)
        elif(Token[0]=="translate"):
            Transformation.append("translate")
            Transformation.append(Token[1])
            Transformation.append(Token[2])
            for i in range(3):
                Token.pop(0)
        elif(Token[0]=="scale"):
            Transformation.append("scale")
            Transformation.append(Token[1])
            for i in range(2):
                Token.pop(0)
        elif(Token[0]=="rect"):
            DrawCommand.Rect(float(Token[1]),float(Token[2]),float(Token[3]),float(Token[4]),Transformation,False)
            for i in range(5):
                Token.pop(0)
        elif(Token[0]=="filledrect"):
            DrawCommand.Rect(float(Token[1]),float(Token[2]),float(Token[3]),float(Token[4]),Transformation,True)
            for i in range(5):
                Token.pop(0)
        elif(Token[0]=="line"):
            DrawCommand.Line(float(Token[1]),float(Token[2]),float(Token[3]),float(Token[4]),Transformation)
            print("stroke")
            for i in range(5):
                Token.pop(0)
        elif(Token[0]=="tri"):
            DrawCommand.Tri(float(Token[1]),float(Token[2]),float(Token[3]),Transformation,False)
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="filledtri"):
            DrawCommand.Tri(float(Token[1]),float(Token[2]),float(Token[3]),Transformation,True)
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="square"):
            DrawCommand.Square(float(Token[1]),float(Token[2]),float(Token[3]),Transformation,False)
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="filledsquare"):
            DrawCommand.Square(float(Token[1]),float(Token[2]),float(Token[3]),Transformation,True)
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="penta"):
            DrawCommand.Penta(float(Token[1]),float(Token[2]),float(Token[3]),Transformation,False)
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="filledpenta"):
            DrawCommand.Penta(float(Token[1]),float(Token[2]),float(Token[3]),Transformation,True)
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="hexa"):
            DrawCommand.Hexa(float(Token[1]),float(Token[2]),float(Token[3]),Transformation,False)
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="filledhexa"):
            DrawCommand.Hexa(float(Token[1]),float(Token[2]),float(Token[3]),Transformation,True)
            for i in range(4):
                Token.pop(0)
        elif(Token[0]=="ngon"):
            DrawCommand.Ngon(float(Token[1]),float(Token[2]),float(Token[3]),int(float(Token[4])),Transformation,False)
            for i in range(5):
                Token.pop(0)
        elif(Token[0]=="filledngon"):
            DrawCommand.Ngon(float(Token[1]),float(Token[2]),float(Token[3]),int(float(Token[4])),Transformation,True)
            for i in range(5):
                Token.pop(0)
    print("showpage")
text=sys.stdin.read().splitlines()
Draw(text)
