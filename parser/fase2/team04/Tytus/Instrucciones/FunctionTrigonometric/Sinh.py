import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion

class Sinh(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.DOUBLE_PRECISION),linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        """ resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función sinh("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        try:
            return math.sinh(resultado)
        except ValueError as c:
            error = Excepcion('22003',"Semántico","La entrada está fuera de rango",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error """
        return math.sinh(self.valor)
            
    def getCodigo(self, tabla, arbol):
        result = self.valor.getCodigo(tabla, arbol)        
        value_list = []
        
        value_list.append(result['dir'])
        value_list.append(f"\"{self.strGram}\"")
        value_list.append(self.linea)
        value_list.append(self.columna)
        
        native_result = arbol.getExpressionCode(value_list, 'sinh')
        
        codigo = result['codigo']
        codigo += native_result['codigo']
        
        return {'codigo': codigo, 'dir': native_result['dir']}
    
    def toString(self):
        return f"SINH({self.valor})"