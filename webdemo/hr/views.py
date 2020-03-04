from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def welcome(request):
    return render(request, 'welcome.html')


def list_jobs(request):
    con = sqlite3.connect(r"e:\classroom\python\jan27\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs")
    jobs = cur.fetchall()
    cur.close()
    con.close()
    return render(request, 'list_jobs.html', {"jobs": jobs})
