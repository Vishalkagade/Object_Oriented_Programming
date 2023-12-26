class BalanceException(Exception):
    """
    Exception raised for insufficient balance in a bank account.

    Attributes:
        message -- explanation of the error
    """

    pass

class BankAccount:
    """
    A class representing a basic bank account.

    Attributes:
        balance (float): The current balance of the account.
        name (str): The name associated with the account.

    Methods:
        __init__: Initializes a new BankAccount object.
        get_balance: Prints the current balance of the account.
        deposit: Deposits a specified amount into the account.
        allowed_transaction: Checks if a transaction of a specified amount is allowed.
        withdraw: Withdraws a specified amount from the account.
        transfer: Transfers a specified amount to another account.
    """

    def __init__(self, initial_amount, account_name):
        """
        Initializes a new BankAccount object.

        Parameters:
            initial_amount (float): The initial balance of the account.
            account_name (str): The name associated with the account.
        """
        self.balance = initial_amount
        self.name = account_name
        # print(f"\nAccount '{self.name}' created with balance = ${self.balance:.2f}")

    def get_balance(self):
        """
        Prints the current balance of the account.
        """
        print(f"Account: {self.name} with balance: ${self.balance}")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Parameters:
            amount (float): The amount to be deposited.
        """
        self.balance = self.balance + amount
        print("Deposit complete")
        self.get_balance()

    def allowed_transaction(self, amount):
        """
        Checks if a transaction of a specified amount is allowed.

        Parameters:
            amount (float): The amount of the transaction.

        Raises:
            BalanceException: If the balance is insufficient for the transaction.
        """
        if self.balance < amount:
            raise BalanceException(f"\nAh, in the account {self.name}, you only have ${self.balance:.2f}")
        else:
            return

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        Parameters:
            amount (float): The amount to be withdrawn.
        """
        try:
            self.allowed_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal complete")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdrawal unsuccessful: {error}")

    def transfer(self, amount, account):
        """
        Transfers a specified amount to another account.

        Parameters:
            amount (float): The amount to be transferred.
            account (BankAccount): The destination account for the transfer.

        Raises:
            BalanceException: If the balance is insufficient for the transfer.
        """
        try:
            print("\n****************\nBeginning transaction")

            self.allowed_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)

            print("\nTransaction complete")

        except BalanceException as error:
            print(f"Transfer not possible due to incomplete balance: {error}")


class InterestAccount(BankAccount):
    """
    A class representing a bank account with interest.

    Methods:
        deposit: Deposits a specified amount into the account with interest.
    """

    def deposit(self, amount):
        """
        Deposits a specified amount into the account with interest.

        Parameters:
            amount (float): The amount to be deposited.
        """
        self.balance = self.balance + amount * 1.05
        print("Deposit complete")
        self.get_balance()


class SavingsAccount(InterestAccount):
    """
    A class representing a savings account.

    Attributes:
        bank_fees (int): The fees associated with the savings account.

    Methods:
        __init__: Initializes a new SavingsAccount object.
        withdraw: Withdraws a specified amount from the savings account.
    """

    def __init__(self, initial_amount, account_name):
        """
        Initializes a new SavingsAccount object.

        Parameters:
            initial_amount (float): The initial balance of the account.
            account_name (str): The name associated with the account.
        """
        super().__init__(initial_amount, account_name)
        self.bank_fees = 5

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the savings account.

        Parameters:
            amount (float): The amount to be withdrawn.
        """
        try:
            self.allowed_transaction(amount + self.bank_fees)
            self.balance = self.balance - amount
            self.get_balance()
        except BalanceException as error:
            print(f"Withdrawal not possible from {self.name} due to insufficient balance")
