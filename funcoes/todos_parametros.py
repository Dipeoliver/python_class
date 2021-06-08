def todos_param(*args,**kwargs):
    print(f'args {args}')
    print(f'kwargs{kwargs}')

if __name__ == "__main__":
    todos_param(1,2,3)
    todos_param(1,2,4, tempo="12:00", legal=True)
    todos_param(1,2,[1,2,3], teste=False)

    # sempre tem de passar parametros posicionais e depoid nomeados
