from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL


class ObtenerSql(InstruccionPL):
    def __init__(self, cadena , tipo, linea, columna, strGram):
        InstruccionPL.__init__(self, tipo, linea, columna, strGram)        
        self.cadena =  cadena
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #ejecucion de una funcion

    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        print('ejecutar cadena desde sql: Crear Metodo ')
