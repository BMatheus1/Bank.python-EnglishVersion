import os


#           BANK ACCOUNT CLASS AND ITS FUNCTIONS


class BankAccount:
    clients = []

    def __init__(self, name, balance, cpf, profession):
        self._name = name.strip().title()
        self._balance = f'${balance:.2f}'
        self._cpf = self.format_cpf(cpf)
        self._profession = profession.strip().title()
        self._active = False
        
        BankAccount.clients.append(self)

    @staticmethod
    def format_cpf(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    def __str__(self):
        return f'{self._name} | {self._balance} | {self._cpf} | {self._profession}'
    
    @classmethod
    def list_clients(cls):
        print(
            f'{'Client Name'.ljust(25)} | '
            f'{'Account Balance'.ljust(25)} | ' 
            f'{'CPF'.ljust(25)} | '
            f'{'Profession'.ljust(25)} | ' 
            f'{'Status'}'
        )

        for client in cls.clients:
            print(f'{client._name.ljust(25)} | {client._balance.ljust(25)} | {client._cpf.ljust(25)} | {client._profession.ljust(25)} | {client.active} | ')

    @classmethod
    def create_account(cls):
       while True:     
            try:
                name = input('\nEnter account holder name: ').title()
                balance = float(input('Enter initial balance: '))
                cpf = input('Enter CPF: ')
                profession = input('Enter profession: ')
                cls(name, balance, cpf, profession)
                
                print('\nNew client successfully added ✔️.')
                break
            except ValueError:
                print('\nInvalid entry. \n')

    @property
    def active(self):
        return 'Active ✔️' if self._active else 'Inactive ❌'

    def toggle_account_status(self):
        self._active = not self._active



#           GENERAL FUNCTIONS


def main():
    choose_option()

def clear_screen():
    os.system('cls')

def show_title():
    print(''' 
╔═══╗───╔╗──────────╔╗
║╔═╗║──╔╝╚╗─────────║║
║╚══╦╦═╩╗╔╬══╦╗╔╦══╗║╚═╦══╦═╗╔══╦══╦═╦╦══╗
╚══╗╠╣══╣║║║═╣╚╝║╔╗║║╔╗║╔╗║╔╗╣╔═╣╔╗║╔╬╣╔╗║
║╚═╝║╠══║╚╣║═╣║║║╔╗║║╚╝║╔╗║║║║╚═╣╔╗║║║║╚╝║
╚═══╩╩══╩═╩══╩╩╩╩╝╚╝╚══╩╝╚╩╝╚╩══╩╝╚╩╝╚╩══╝
''')

def return_to_menu():
    while True: 
        choice = input('\nReturn to main menu? (y/n): ').lower()  
        if choice == 'y':
            return
            
        elif choice == 'n':
            clear_screen()
            print('\nExiting system.\n')
            exit()
            
        else:
            print('\nInvalid option. ')
        
def main_menu():

    print('1 - Add new client')
    print('2 - List clients')
    print('3 - Activate/Deactivate account')
    print('4 - Exit')

def choose_option():
    while True:
        clear_screen()
        show_title()
        main_menu()

        option = input('\nChoose an option: ')
        if option == '1':
            BankAccount.create_account()
            return_to_menu()

        elif option == '2':
            BankAccount.list_clients()
            return_to_menu()

        elif option == '3':
            cpf = input('\nEnter CPF of client to toggle account status: ')
            cpf = BankAccount.format_cpf(cpf)

            found = False
            
            for client in BankAccount.clients:
                if client._cpf == cpf:
                    client.toggle_account_status()
                    print(f'\nAccount status for {client._name} (CPF {client._cpf}) changed to {client.active}')
                    found = True
                    
            if not found:
                print('\nClient not found.')

            return_to_menu()

        elif option == '4':
            clear_screen()
            print('\nExiting system.\n')
            break

        else:
            print('\nInvalid option.')



#           FIXED CLIENTS


client1 = BankAccount('José da Silva', 5000, '02155075011', 'pedreiro')
client2 = BankAccount('Carlos Silva', 1200, '03166098066', 'operador de produção')
client3 = BankAccount('Mariana Oliveira', 3200, '14598732044', 'enfermeira')
client4 = BankAccount('Ricardo Pereira', 7800, '30945612088', 'analista de sistemas')
client5 = BankAccount('Fernanda Costa', 2100, '87530944012', 'secretária')
client6 = BankAccount('Bruno Matias', 950, '22490877055', 'vendedor')
client7 = BankAccount('Patrícia Santos', 4300, '98712456033', 'professora')
client8 = BankAccount('Leonardo Rocha', 5100, '66723389014', 'motorista')
client9 = BankAccount('Amanda Freitas', 1500, '80211945007', 'esteticista')
client10 = BankAccount('Thiago Menezes', 2750, '41988233090', 'designer gráfico')
client11 = BankAccount('Juliana Ramos', 3600, '58321099011', 'advogada')
client12 = BankAccount('Marcelo Nogueira', 8900, '91044312056', 'engenheiro civil')


if __name__ == '__main__':
    main()
