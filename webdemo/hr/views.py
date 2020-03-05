from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
import requests


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


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    return render(request,'list_countries.html',{'countries' : countries})


def country_info(request):
    code = request.GET["code"]
    # get info about country with code
    return render(request,'country_info.html', {})


def add_job(request):
    if 'jobid' in request.GET:
        # process data as request contains data
        jobid = request.GET['jobid']
        jobtitle =request.GET['jobtitle']
        minsalary = request.GET['minsalary']
        con = sqlite3.connect(r"e:\classroom\python\jan27\hr.db")
        cur = con.cursor()
        cur.execute("insert into jobs values(?,?,?)",
                    (jobid,jobtitle,minsalary))
        con.commit()
        cur.close()
        con.close()
        return render(request, "add_job.html",
                      {'message': "Job has been added succesfully!"})
        # return redirect("/hr/jobs")
    else:
        # Send empty form becuase it is first request
        return render(request,"add_job.html")
