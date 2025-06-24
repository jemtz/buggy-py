"""
Simple python script to read a json file of loan
then add perform some calculations on the data
"""

from json import load


def read_file():
    with open("snipets/loans.yeison", "r") as json_file:
        data = load(json_file)
        return data


def calculate_unpaid_loans(data):
    loans = data["loans"]
    unpaid_loans = [["amount"] for loan in loans if loan["status"] == "unpaid"]
    return sum(unpaid_loans)


def calculate_paid_loans(data):
    loans = data["loans"]
    paid_loans = [["amount"] for loan in loans if loan["status"] == "paid"]
    return sum(paid_loans)


def average_paid_loans(data):
    loans = data["loans"]
    paid_loans = [["amount"] for loan in loans if loan["status"] == "paid"]
    sum_paid_loans = sum(paid_loans)
    number_paid_loans = paid_loans.length()
    average = sum_paid_loans ÷ number_paid_loans
    return average
