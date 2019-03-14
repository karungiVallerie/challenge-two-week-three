from accounts import BankAccount
import unittest


class TestAccounts(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount('account',34)
        

    def test_newly_opened_account_has_zero_balance(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_can_deposit_money(self):

        self.assertEqual(self.account.deposit(100), 100)

    # def test_can_deposit_money_sequentially(self):
    #     self.account.deposit(100)
    #     self.account.deposit(50)
    #     self.assertEqual(self.account.get_balance(), 150)

    def test_can_withdraw_money(self):
        self.account.deposit(100)
        self.assertEqual(self.account.withdraw(50), 50)

    # def test_can_withdraw_money_sequentially(self):
    #     self.account.deposit(100)
    #     self.account.withdraw(20)
    #     self.account.withdraw(80)

    #     self.assertEqual(self.account.get_balance(), 0)

    # def test_checking_balance_of_closed_account_throws_error(self):
    #     self.account.close()
    #     with self.assertRaises(ValueError):self.account.get_balance()

  
    #     with self.assertRaises(ValueError):
    #         self.account.deposit(50)

    
    #     with self.assertRaises(ValueError):
    #         self.account.withdraw(50)

    # def test_cannot_withdraw_more_than_deposited(self):
    #     self.account.deposit(25)

    #     with self.assertRaises(ValueError):
    #         self.account.withdraw(50)

    # def test_cannot_withdraw_negative(self):
    #     self.account.open()
    #     self.account.deposit(100)

    #     with self.assertRaises(ValueError):
    #         self.account.withdraw(-50)

    # def test_cannot_deposit_negative(self):
    

    #     with self.assertRaises(ValueError):
    #         self.account.deposit(-50)

if __name__ == '__main__':
    unittest.main()
        