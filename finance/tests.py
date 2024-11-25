from django.test import TestCase

from .models import BankAccount, Transactions
from users.models import User
from erp.models import Company


class BankAccountTestCase(TestCase):
    def setUp(self):
        # Create a Company instance
        self.company = Company.objects.create(fantasia='Test Company')

        # Create BankAccount instances
        self.bank_account = BankAccount.objects.create(
            company=self.company,
            name='Main Account',
            agencia='1234',
            conta='567890',
            saldo=1000.50,
        )

    def test_bank_account_creation(self):
        '''Test that the BankAccount instance is created properly.'''
        self.assertEqual(self.bank_account.name, 'Main Account')
        self.assertEqual(self.bank_account.agencia, '1234')
        self.assertEqual(self.bank_account.conta, '567890')
        self.assertEqual(self.bank_account.saldo, 1000.50)
        self.assertEqual(self.bank_account.company, self.company)  

    def test_default_saldo(self):
        '''Test that the default saldo is 0.'''
        new_account = BankAccount.objects.create(
            company=self.company,
            name='Secondary Account',
        )
        self.assertEqual(new_account.saldo, 0)              

    def test_nullable_fields(self):
        '''Test that nullable fields can accept None.'''
        new_account = BankAccount.objects.create(
            company=self.company,
            name='Null Fields Account',
            agencia=None,
            conta=None,
        )
        self.assertIsNone(new_account.agencia)
        self.assertIsNone(new_account.conta)     

    def test_string_representation(self):
        '''Test the __str__ method.'''
        self.assertEqual(str(self.bank_account), 'Main Account')           

    def test_uuid_auto_generation(self):
        '''Test that the UUID is generated automatically.'''
        self.assertIsNotNone(self.bank_account.id)    

    def test_cascade_deletion(self):
        '''Test that deleting a company deletes its bank accounts.'''
        self.company.delete()
        self.assertEqual(BankAccount.objects.count(), 0)            


class TransactionsTestCase(TestCase):
    def setUp(self):
        # Create a Company instance
        self.company = Company.objects.create(fantasia='Test Company')
        # Create a BankAccount instance
        self.conta = BankAccount.objects.create(
            company=self.company, name='Main Account',
        )
        # Create a User instance
        self.user = User.objects.create(email='hugo@django.com')

        #Create a Transactions instance
        self.transaction = Transactions.objects.create(
            tipo='entrada',
            valor=100,
            conta=self.conta,
            contato='Hugo Cordeiro Belém',
            descricao='teste',
            categoria='teste',
            created_by=self.user,
            linked=None,
        )

    def test_transaction_creation(self):
        '''Test that the Transaction instance is created properly.'''
        self.assertEqual(self.transaction.tipo, 'entrada')
        self.assertEqual(self.transaction.valor, 100)
        self.assertEqual(self.transaction.conta, self.conta)
        self.assertEqual(self.transaction.contato, 'Hugo Cordeiro Belém')
        self.assertEqual(self.transaction.descricao, 'teste')          
        self.assertEqual(self.transaction.categoria, 'teste')
        self.assertEqual(self.transaction.created_by, self.user)
        self.assertIsNone(self.transaction.linked)        

    def test_nullable_fields(self):
        '''Test that nullable fields can accept None.'''
        new_transaction = Transactions.objects.create(
            tipo='entrada',
            valor=100,
            conta=self.conta,
            contato=None,
            descricao='Teste',
            categoria=None,
            created_by=self.user,
            linked=None,
        )

    def test_string_representation(self):
        '''Test the __str__ method.'''
        self.assertEqual(str(self.transaction), 'teste')           

    def test_uuid_auto_generation(self):
        '''Test that the UUID is generated automatically.'''
        self.assertIsNotNone(self.transaction.id)           

    def test_account_protect_deletion(self):
        '''Test that it only deletes a bank account if it has no transaction.'''
        self.transaction.delete()
        self.conta.delete()
        self.assertEqual(Transactions.objects.count(), 0)

    def test_user_cascade_deletion(self):
        '''Test that deleting a user deletes its transactions.'''
        self.user.delete()
        self.assertEqual(Transactions.objects.count(), 0)        

    def test_linked_transactions(self):
        '''Test linking of transactions.tipo 'transferir'.'''
        self.enviar = Transactions.objects.create(
            tipo='tansferir',
            valor=100,
            conta=self.conta,
            contato='Hugo Cordeiro Belém',
            descricao='enviar',
            categoria='transferir',
            created_by=self.user,
            linked=None,
        )

        self.assertEqual(self.enviar.linked, None)

        self.receber = Transactions.objects.create(
            tipo='tansferir',
            valor=100,
            conta=self.conta,
            contato='Hugo Cordeiro Belém',
            descricao='receber',
            categoria='transferir',
            created_by=self.user,
            linked=self.enviar,
        )        
        
        self.assertEqual(self.enviar.linked, self.receber)
