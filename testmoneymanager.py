import unittest

from moneymanager import MoneyManager

class TestMoneyManager(unittest.TestCase):

    def setUp(self):
        # Create a test BankAccount object
        self.enduser = MoneyManager()

        # Provide it with some initial balance values        
        self.enduser.user_balance = 5000.0

    def test_legal_deposit_works(self):
        # Your code here to test that depsositing money using the account's
        # 'deposit_funds' function adds the amount to the balance.
        amount = 500.0
        expected = 5500.0
        actual = self.enduser.take_money(amount)
        self.assertAlmostEqual(expected, actual, 'failed test for depost!')
    def test_illegal_deposit_raises_exception(self):
        # Your code here to test that depositing an illegal value (like 'bananas'
        # or such - something which is NOT a float) results in an exception being
        # raised.
        amount = 'lock'
        expected = 'The entry_type is not valid'
        actual = self.enduser.take_money(amount)
        self.assertEqual(expected, actual, 'Exception R!!!')

    def test_legal_entry(self):
        # Your code here to test that adding a new entry with a a legal amount subtracts the
        # funds from the balance.
        entry = 'rent'
        amount = 500.0
        expected = 4500.0
        actual = self.enduser.user_entry(amount, entry)
        self.assertEqual(expected, actual, "failed")
        

    def test_illegal_entry_amount(self):
        # Your code here to test that withdrawing an illegal amount (like 'bananas'
        # or such - something which is NOT a float) raises a suitable exception.
        amount = 'money'
        entry = 'rent'
        expected = 'The entry_type is not valid'
        actual = self.enduser.user_entry(amount, entry)
        self.assertEqual(expected, actual, "Error raised!!!")

        
    def test_illegal_entry_type(self):
        # Your code here to test that adding an illegal entry type (like 'bananas'
        # or such - something which is NOT a float) raises a suitable exception.
        amount = 500.0
        entry = 'bananas'
        expected = 'The entry_type is not valid'
        actual = self.enduser.user_entry(amount, entry)
        self.assertEqual(expected, actual, "Error raised!!!")

    def test_insufficient_funds_entry(self):
        # Your code here to test that you can only spend funds which are available.
        # For example, if you have a balance of 500.00 dollars then that is the maximum
        # that can be spent. If you tried to spend 600.00 then a suitable exception
        # should be raised and the withdrawal should NOT be applied to the user balance
        # or the user's transaction list.
        amount = 6000.0
        entry = 'rent'
        expected = 'The entry_type is not valid'
        actual = self.enduser.user_entry(amount, entry)
        self.assertEqual(expected, actual, "Insufficient Fund!!")

## Run the unit tests in the above test case
unittest.main()       
