resl=0
def run():
    nums=[1,2,3,4,5,6,7,8,9,10]
    nums_exp=[]
    for i in nums:
        resl=i**2
        nums_exp.append(resl)
    print(nums_exp)


if __name__=='__main__': #iniciar funcion alejectar archivo de python.
    run()