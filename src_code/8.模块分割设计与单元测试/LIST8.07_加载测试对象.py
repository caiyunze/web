class TestBankAccount(unittest.TestCase):

    def _getTarget(self):
        from bankaccount import BankAccount
        return BankAccount

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    #...（ 略 ）...
