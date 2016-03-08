from __future__ import unicode_literals
from django.shortcuts import render
from models import Magazine


def fill_magazine(request):
    pass
    # current_year = 1997
    # current_month = 10
    #
    # for item in range(1, 223):
    #     Magazine(number=item, public_year=current_year, public_month=current_month).save()
    #     current_month += 1
    #     print(current_month)
    #     print(current_year)
    #     if current_month % 13 == 0:
    #         current_month = 1
    #         current_year += 1
