from cmath import sqrt
import math
def run():
    nums_exp={i:math.sqrt(i) for i in range(1,21)}
    print(nums_exp)

if __name__=='__main__':
    run()