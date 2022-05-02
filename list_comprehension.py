resl=0
def run():
    '''
    Usamos una list comprehension para conocer los numeros
    divisibles entre 4 , 6 y 9 hasta llegar al mil.
    '''
    nums_exp=[i for i in range(1,601) if i%4==0 and i%6==0 and i%9==0]
    print(nums_exp)

if __name__=='__main__': 
    run()
