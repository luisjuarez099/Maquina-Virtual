resl=0
def run():
    nums_exp=[i for i in range(1,601) if i%4==0 and i%6==0 and i%9==0]
    print(nums_exp)

if __name__=='__main__': 
    run()
