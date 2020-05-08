{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs24 \cf0 def Quad(a,b,c):\
  xFirst=(-b+(b**2-4*a*c)**0.5)/(2*a)\
  xSecond=(-b-(b**2-4*a*c)**0.5)/(2*a)\
  return xFirst,xSecond\
\
def sumofABC(x,y,z):\
  summation=x+y+z\
  return summation\
\
def main():\
  i = float(input('Enter a: '))\
  j = float(input('Enter b: '))\
  k = float(input('Enter c: '))\
  x1,x2=Quad(i,j,k)\
  print("x1= ",x1,"x2= ",x2)\
  sigma=sumofABC(i,j,k)\
  print("Sum of a b c is ",sigma)\
\
if __name__ == "__main__":\
  main()\
}