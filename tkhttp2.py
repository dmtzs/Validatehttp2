try:
    from biblios import metodos
except ImportError as eImp:
    print(f"The following ERROR ocurred: {eImp}")

if __name__== "__main__":
    mainTitleApp= "HTTP2 Vlidator"
    titleApp= "http2 webpage validator"
    
    try:
        met= metodos.funciones(titleApp, mainTitleApp)
        met.GUI()
    except KeyboardInterrupt:
        print("Se presionó Ctrl + C")
    except Exception as ex:
        print(f"Ocurrió el siguiente ERROR: {ex}")
    finally:
        print("Finalizando programa")