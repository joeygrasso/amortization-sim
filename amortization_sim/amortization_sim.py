from .loan import Loan

class amortization_sim():
    """
    Main amortization_sim class
    Arguments:
        Loan - loan object
        additional_payment - additional amount towards principal
        duration - how many times should the additional principal be applied
        frequenzy - how often should the additional_payment be applied
        start_num - when should the additional payment begin being applied
    """
    def __init__(self, loan, additional_payment, duration, frequency, start_num):
        self.loan = loan
        self.additional_payment = additional_payment
        self.duration = duration
        self.frequency = frequency
        self.start_num = start_num

    def original_schedule(self):
        return self.loan.loan_schedule()

    def calculate_amoritzation_schedule(self):
        # Existing loan values
        p = self.loan.principal
        r = self.loan.calculate_monthly_rate
        d = self.loan.duration
        monthly_payment = self.loan.calculate_monthly_payment

        # Amortization Values
        amort_loan_schedule = {}
        total_interest = 0
        balance = p
        payment_number = 1
        extra_payment_duration_counter = self.duration
        apply_extra_payment = False

        while balance > 0.01:

            current_interest = self.loan.calculate_monthly_interest(balance)
            balance += current_interest

            if (payment_number == self.start_num) or (payment_number % self.frequency) == 0:
                # Begin applying additional principal
                apply_extra_payment = True

            if apply_extra_payment:
                payment_towards_principal = (monthly_payment + self.additional_payment) - current_interest
                extra_payment_duration_counter -= 1
                balance -= (monthly_payment + self.additional_payment)
            else:
                payment_towards_principal = monthly_payment - current_interest
                balance -= monthly_payment

            amort_loan_schedule[payment_number] = {
                "payment_num": payment_number,
                "payment": round(monthly_payment, 2),
                "principal": round(payment_towards_principal, 2),
                "interest": round(current_interest, 2),
                "total_interest": round(total_interest, 2),
                "balance": round(balance, 2),
            }

            payment_number += 1

        return amort_loan_schedule

    def compare_loan_interest(self):
        loan_schedule = self.original_schedule()
        amortized_schedule = self.calculate_amoritzation_schedule()
        #return loan_schedule[self.loan.duration]["total_interest"] - amortized_schedule[]
        pass
    
    def compare_loan_payment_num(self):
        loan_schedule = self.original_schedule()
        amortized_schedule = self.calculate_amoritzation_schedule()

        return loan_schedule[self.loan.duration]["payment_number"] - amortized_schedule["duration"]["payment_number"]
    
# Make these into tests with asserts
mortgage_loan = Loan(100000.0, .06, 360)
car_loan = Loan(11000, .0274, 36)

adjusted_car_loan = amortization_sim(car_loan, 100, 10, 1, 26)
print(car_loan.loan_schedule())
