import random 
def inversion():
  inv = ["1st inversion" , "2nd inversion" , "3rd inversion"]
  return (random.choice(inv))

def main():
  chords = ["C Major" , "D Minor" , "E Minor" , "F Major" , "G7" , "A Minor" , "B diminished"]  
  cnum = int(input('Enter number of chords you would like in C Maj: '))
  for x in range(cnum):
    inv = inversion() 
    print(random.choice(chords)+ " " + inv) 

if __name__ == "__main__":
  main()