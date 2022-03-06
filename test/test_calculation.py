from unittest import result
import pytest
from re import sub
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    print("Creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(500)

@pytest.mark.parametrize("num1,num2,result",[
    (500,500,1000),
    (31,69,100),
    (100, -90,10)
])
def test_add(num1,num2,result):
    print("We are testing add function")
    # result = add(num1,num2)
    assert add(num1,num2)==result


def test_subtract():
    print("We are testing subtract function")
    result = subtract(100,20)
    assert result==80


def test_multiply():
    print("We are testing multiply function")
    result = multiply(100,20)
    assert result==2000


def test_divide():
    print("We are testing divide function")
    result = divide(100,20)
    assert result==5

def test_bank_set_initial_amount(bank_account):
    # bank_account = BankAccount(50)
    assert bank_account.balance == 500


def test_bank_default_amount(zero_bank_account):
    # zero_bank_account = BankAccount()
    assert zero_bank_account.balance == 0

def test_bank_withdraw(bank_account):
    #bank_account = BankAccount(500)
    bank_account.withdraw(100)
    assert bank_account.balance == 400

def test_bank_deposite():
    bank_account = BankAccount(500)
    bank_account.deposit(100)
    assert bank_account.balance == 600

def test_collect_interest(bank_account):
    # bank_account = BankAccount(500)
    bank_account.collect_interest()
    assert round(bank_account.balance,2) == 550



@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

    
def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(2000)