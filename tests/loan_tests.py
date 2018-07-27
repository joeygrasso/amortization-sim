import unittest
import amortization_sim

class LoanTestSet(unittest.TestCase):


    def test_loan_object(self):
        loan = loan.Loan(25000, .05, 36)
        self.assertEqual(loan.principal, 2000)