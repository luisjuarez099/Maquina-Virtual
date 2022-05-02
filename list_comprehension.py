resl=0
def run():
    # nums_exp=[]
    # for i in range(0,21):
    #     resl=i**2
    #     if resl%3 ==0:
    #         continue
    #     nums_exp.append(resl)
    # nums_exp=[pow(i,2) for i in range(1,21) if i%3 !=0]
    nums_exp=[i for i in range(1,601) if i%4==0 and i%6==0 and i%9==0]
    print(nums_exp)

if __name__=='__main__': 
    run()