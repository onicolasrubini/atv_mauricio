class Contribuintes():
    
    
    def __init__(self,nomePessoaFis,nomePessoaJuri,rendaAnual_Pfisica,rendaAnual_Pjuri,gastoSaude,numDeFunc):
       self.nomePessoaFis = nomePessoaFis
       self.nomePessoaJuri = nomePessoaJuri
       self.rendaAnual_Pfisica = rendaAnual_Pfisica
       self.rendaAnual_Pjuri = rendaAnual_Pjuri
       self.gastoSaude = gastoSaude
       self.numDeFunc = numDeFunc
       
       
    def conta_pessoaFis(self,renda):
        
        if self.rendaAnual_Pfisica <= 20000:
            renda = 15/100 * self.rendaAnual_Pfisica
            print(renda)
            
            
        elif self.rendaAnual_Pfisica > 20000:
            renda = (25/100 * self.rendaAnual_Pfisica) - (50/100 * self.gastoSaude)
            print(renda)
            
    
    def conta_pessoaJuri(self,imposto):
        
        if self.numDeFunc <= 10:
            imposto = 16/100 * self.rendaAnual_Pjuri
            print(imposto)
        
        
        elif self.numDeFunc > 10:
            imposto = 14/100 * self.rendaAnual_Pjuri
            print(imposto)