#F123 ABHAY YADAV
class Bank:

    @staticmethod
    def validate_account(acc_no):
        """Check if account number is valid (10 digits)"""
        return len(str(acc_no)) == 10

    @staticmethod
    def calculate_interest(principal, rate, time):
        """Calculate Simple Interest"""
        return (principal * rate * time) / 100


# Accessing static methods WITHOUT creating object
account = 1234567890

if Bank.validate_account(account):
    interest = Bank.calculate_interest(50000, 5, 2)
    print("Valid Account")
    print("Simple Interest:", interest)
else:
    print("Invalid Account")
