
from parth import Parth

if __name__ == "__main__":
    i = 20
    j = 30
    parth = Parth(x=i,y=j,fieldid=2)

    for x in range(0,i+1):
        for y in range(0,j+1):
            print(parth.getNextTile())