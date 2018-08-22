""" This class is for generic loan stuff that shouldn't change."""

class Loan(): 

    def __init__(self, principal, rate, duration):
       self.principal = principal
       self.rate = rate
       self.duration = duration

    def calculate_monthly_payment(self):
        #                       ( MonthlyInterestRate * (1 + MonthlyInterestRate) ^ Duration  )
        # payment = Principal * ( ----------------------------------------------------------- )
        #                       (         ((1 + MonthlyInterestRate) ^ Duration) - 1          )

        monthly_interest_rate = self.calculate_monthly_rate()
        monthly_payment = self.principal * (monthly_interest_rate * 
            ((1 + monthly_interest_rate) ** self.duration)) / ( 
            ((1 + monthly_interest_rate) ** self.duration) - 1)

        return monthly_payment

    def calculate_monthly_rate(self):
        return self.rate / 12   # 12 == months per year

    def calculate_monthly_interest(self, balance):
        return balance * self.calculate_monthly_rate()

    def loan_schedule(self):
        monthly_payment = self.calculate_monthly_payment()
        total_interest = 0
        balance = self.principal
        payment_number = 1
        loan_schedule = {}

        while balance > 0.01:

            current_interest = self.calculate_monthly_interest(balance)
            balance += current_interest
            
            payment_towards_principal = monthly_payment - current_interest
            total_interest = total_interest + current_interest
            
            balance -= monthly_payment

            loan_schedule[payment_number] = {
                "payment_num": payment_number,
                "payment": round(monthly_payment, 2),
                "principal": round(payment_towards_principal, 2),
                "interest": round(current_interest, 2),
                "total_interest": round(total_interest, 2),
                "balance": round(balance, 2),
            }

            payment_number += 1
        
        return loan_schedule
