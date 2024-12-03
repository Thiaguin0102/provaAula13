class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self):
        valor = float(input("Digite o valor a ser depositado: "))
        self.saldo += valor

    def sacar(self):
        valor = float(input("Digite o valor a ser sacado: "))
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return f"Saldo restante: R${self.saldo}"
    
cliente1 = ContaBancaria("João", 1000.0)
cliente1.depositar()
cliente1.sacar()
print(cliente1.consultar_saldo())