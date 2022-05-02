def run():
    dict={}
    for i in range(1,11):
        if i%3==0:
            continue
        dict[i]=pow(i,3)
    print(dict)
if __name__=='__main__':
    run()