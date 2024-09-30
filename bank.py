class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.admin_list = []
        self.account_list = []
        self.bank_balance: float = 0
        self.loan_feature = True
        self.loan_amount = 0