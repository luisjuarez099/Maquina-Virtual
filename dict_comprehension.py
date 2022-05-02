def run():
    nums_exp={i: pow(i,3) for i in range(1,20)  if i%3 != 0 }
    print(nums_exp)

if __name__=='__main__':
    run()