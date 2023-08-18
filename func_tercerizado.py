class Funcionario():
    
 

    def __init__(self,nome,nomeTercerizado,h_trabalhadas,h_trabalhadasTercerizado,valor_porH,valor_porH_ter,despesa_add):
        self.nome = nome
        self.nomeTercerizado = nomeTercerizado
        self.h_trabalhadas = h_trabalhadas
        self.h_trabalhadasTercerizado = h_trabalhadasTercerizado
        self.valor_porH = valor_porH
        self.valor_porH_ter = valor_porH_ter
        self.despesa_add = despesa_add
        
        
        
    def func(self,h_trabalhadas,valor_porH):
        pagamento = h_trabalhadas * valor_porH
        print(pagamento)
        
        
    def func_tercerizado(self,h_trabalhadas,valor_porH,despesa_add):
        adicional = 110/100 * despesa_add
        pagamento = h_trabalhadas * valor_porH + adicional
        print(pagamento)
        