from Backend import db_helper

import os
import sys

print(__file__)


def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-08-02")
    assert len(expenses) == 6
    assert expenses[0]['amount'] == 50
    assert expenses[0]['category'] == "Entertainment"
    assert expenses[0]['notes'] == "Movie tickets"


def test_fetch_expenses_for_date_invalid_data():

    expenses = db_helper.fetch_expenses_for_date("999-08-02")

    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("2099-08-05" ,"2099-08-10" )
    assert len(summary) == 0
