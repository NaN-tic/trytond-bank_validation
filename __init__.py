#This file is part bank_validation module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .bank import *

def register():
    Pool.register(
        BankAccountNumber,
        module='bank_validation', type_='model')
