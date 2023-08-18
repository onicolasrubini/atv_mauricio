class Funcionario():
    
 

    def __init__(self,nome,h_trabalhadas,valor_porH,despesa_add):
        self.nome = nome
        self.h_trabalhadas = h_trabalhadas
        self.valor_porH = valor_porH
        self.despesa_add = despesa_add
        
        
    def func(self,h_trabalhadas,valor_porH):
        pagamento = h_trabalhadas * valor_porH
        print(pagamento)
        
        
    def func_tercerizado(self,h_trabalhadas,valor_porH,despesa_add):
        adicional = 110/100 * despesa_add
        pagamento = h_trabalhadas * valor_porH + adicional
        print(pagamento)
        