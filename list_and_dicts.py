def run():
    my_list=[1,"Juarez",True, 21.12]
    my_dict={"Name":"Luis", "Lastname" : "juarez"}

    super_list=[{"Name":"Luis", "Age": "25", "Name":"Edgar", "Age": "22"}]

    super_dict={
        "Float nums": [1.2,2.3,3.4,4.5,5.6],
        "Integer nums": [1,2,3,4,5,6],
        "Par nums":[2,4,6,8]
    }
    #super diccionario
    for keys, value in super_dict.items():
        print(keys, " : ", value)
    #super lista
    for items in super_list:
        for k,v in items.items():
	        print(''.join(f"{k} {v}"))

if __name__=='__main__': #iniciar funcion alejectar archivo de python.
    run()