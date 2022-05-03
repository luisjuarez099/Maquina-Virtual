from cmath import sqrt
import math
def run():
    dict_nums={i:math.sqrt(i) for i in range(1,6,1)}
    print(dict_nums)
def expo():
    nums_expo=[pow(i,2) for i in range(1,6,1)]
    print(nums_expo)
if __name__=='__main__':
    run()
    expo()