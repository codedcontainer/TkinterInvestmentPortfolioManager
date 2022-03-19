from SetDefaultData.Common import Common

class AllBalanceDefaultData:
    @staticmethod
    def purchasingPower():
        rbpp = Common.purchasingPower('robinhood_account')
        frpp = Common.purchasingPower('fidelity_account')
        return rbpp + frpp
     
    @staticmethod
    def accountBalance():
        rbab = Common.accountBalance('robinhood_account')
        frab = Common.accountBalance('fidelity_account')
        return rbab + frab
