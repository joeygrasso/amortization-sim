from loan import Loan

class amortization_sim():
    def __init__(self, Loan, additional_payment, duration, frequency, start_date):
        self.loan = Loan
        self.additional_payment = additional_payment
        self.duration = duration
        self.frequency = frequency
        self.start_date = start_date

    def original_schedule(self):
        return self.Loan.loan_schedule()

    def calculate_amoritzation_schedule(self):
        # Copy code from calculate schedule and add logic for additional payment info
        pass

    def compare_loan_interest(self):
        loan_schedule = original_schedule()
        amortized_schedule = calculate_amoritzation_schedule()
        return loan_schedule[self.loan.duration]["total_interest"] - amortized_schedule[""]
        pass
    
    def compare_loan_payment_num(self):
        loan_schedule = original_schedule()
        amortized_schedule = calculate_amoritzation_schedule()

        return loan_schedule[self.loan.duration]["payment_number"] - amortized_schedule["duration"]["payment_number"]
    
# Make these into tests with asserts
mortgage_loan = Loan(100000.0, .06, 360)
car_loan = Loan(11000, .0274, 36)