from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta + []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    def adicionar_contas(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento 
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente 
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente )
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente 
    @property
    def historico(self):
        return self._historico
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ operação falhou! voçê nãotem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor 
            print("\n@@@ saque realizado com sucesso. @@@")

        else: 
            print("operação falhou! o valor informado é valido. @@@")

            return False 
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor 
            print("\n@@@ Deposito realizado com sucesso! @@@")
        else:
            print("\n@@@ Operaçâo falhou! o valor informado é invalido. @@@")
            return False
        return True

class ContaCorrente(Conta):
     def __init__(self, numero, cliente, limite=500, limite_saques=3):
         super().__init__(numero, cliente)
         self.limite = limite
         self.limite_saques = limite_saques
     def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao ["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print("\n@@@ operação falhou! o valor do saque excedeu o limite . @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Numero maximo de saques excedido. @@@")

        else:
            return super().sacar(valor)
        
        return False

     def __str__(self):
         return f"""\
             Agência:\t{self.agencia}
             C/C:\t\t{self.numero}
             Titular:\t{self.cliente.nome}
            """
 ##
 ##[0] depositar
 ##[1] sacar 
 ##[2] extrato
 # #[3] sair

class Historico:
    def __init__(self):
        self._transacoes = []
    @property
    def transacoes(self):
        return self._transacoes
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                    "tipo": transacao.__class__.__name__,
                    "valor": transacao.valor,
                    "data": datatime.now().strftime
                    ("%d-%m-%y %H : %M %s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
     pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar (self, conta ):
        sucesso_trasacao = conta.sacar(self.valor)

        if sucesso_trasacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    def registrar (self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



def menu():
    menu = """\n
    ------------------menu---------------
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova conta
    [lc]\t Listar contas 
    [nu]\t Novo usuario
    [q]\t Sair
    -------------------------------------
=>"""
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados - [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):

    if not cliente.contas:
        print("\n@@@ cliente não possui conta! @@@")
        return
    
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("informe seu cpf: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ cliente não encontrado @@@")
        return
    valor = float(input("informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
       print("\n@@@ cliente não encontrado @@@")  
       return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print("\n ========== EXTRATO ==========")
    transacoes = conta.historico.transacoes 

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentacoes"
    else:
        for transacao in transacao:
         extrato = f'\n{transacao["tipo"]}:\n\tR$
            {transacao['valor']:.2f}'

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print("================================")

def criar_cliente(clientes):

    cpf = input("informe seu cpf: ")
    cliente = filtra
    r_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ ja existe cliente com esse cpf! @@@")
        return
    
    nome = input("informe o nome clompleto: ")
    data_nascimento = input("informe sua data de nascimento: ")
    endereco = input ("informe seu endereço (logradouro, nro - bairro - cidade/sigla estado):  ")

    cliente = PessoaFisica (nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    cliente.append(cliente)

    print("\n=== cliente criaado com sucesso!===")
    
def criar_conta(nuemro_conta, clientes, contas):
    cpf = input("informe seu cpf: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not clientes:
        print("\n@@@ Cliente não encontrado, fluxo de criaçao de conta encerrado! @@@")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contaas.aooend(conta)

    print("\n=== conta criada com sucesso ====")

def listar_contas(contas):
    for conta in contas:
        print("-" + 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break

        else:
            print("\n@@@ operação invalida, por favor selecione novamente a operação desejada. @@@")
main()













#while True: 

 #   opcao = input(lista)
#
 #   if opcao == "0":
  #      valor = float(input("informe o deposito: "))
#
 #       if valor > 0: 
  #          saldo += valor 
   #         extrato += f'Depósito: R$ {valor:.2f}\n'
    #    else:
     #      print("operaçao falhou, o valor dado foi invalido")
    #elif opcao == "1":

  #      valor = float(input("informe o saque: "))

#        excedeu_saldo = valor >= saldo
        
 #       excedeu_limite = valor >= limite 

  #      excedeu_saque = numeros_saques >= LIMITE_SAQUES

   #     if excedeu_saldo:
    #        print("Operação falhou, voçê não tem saldo suficiente")
        
     #   if excedeu_limite:
      #      print("Operação falhou, o valor de saque excede o limite")
#        
#        if excedeu_saque:
 ##           print("Operação falhou, voçê excedeu o limites de saques diarios")

   #     elif valor > 0:
    #        saldo -= valor
     #       extrato += (f"saque: R${valor:.2F}\n")
      #      numeros_saques += 1

##  
    #elif opcao == "2":
      #  print ("\n===========EXTRATO===========")
       # print("Não foram realizadas movimentações. ") if not extrato else extrato
        #print(f'\nSaldo: R$ {saldo:.2f}') 
        #print("================================")
    #elif opcao == "3":
    #    break

   # else:
        #print("Operação invalida, por favor selecione operação desejada")
##






















