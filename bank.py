#This file is part bank_validation module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
import logging

HAS_BANKNUMBER = False
BANK_COUNTRIES = [('', '')]
try:
    import banknumber
    HAS_BANKNUMBER = True
    for country in banknumber.countries():
        BANK_COUNTRIES.append((country, country))
except ImportError:
    logging.getLogger('bank_validation').warning(
            'Unable to import banknumber. Bank code validation disabled.')

__all__ = ['BankAccountNumber']
__metaclass__ = PoolMeta


class BankAccountNumber:
    'Bank Account Number'
    __name__ = 'bank.account.number'
    bank_country = fields.Selection(BANK_COUNTRIES, 'Bank Country',
        help="Setting Bank country will enable validation of the Bank code.")

    @classmethod
    def __setup__(cls):
        super(BankAccountNumber, cls).__setup__()
        cls._error_messages.update({
                'invalid_bank_number': 'Invalid bank number in account "%s".',
                })

    @classmethod
    def validate(cls, accounts):
        for account in accounts:
            account.check_bank_number()

    def check_bank_number(self):
        '''
        Check the Bank number depending of the country.
        '''
        if not HAS_BANKNUMBER:
            return
        if not self.bank_country:
            return

        number = self.number.replace(' ','')
        if (not getattr(banknumber, 'check_code_'
                    + self.bank_country.lower())(number)):
            #Check if user doesn't have put country code in number
            if number.startswith(self.bank_country):
                number = number[len(self.bank_country):]
                self.write([self], {
                        'number': number,
                        })
            else:
                self.raise_user_error('invalid_bank_number', (self.rec_name,))
