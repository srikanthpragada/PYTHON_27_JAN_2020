from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
import requests
from .forms import  JobForm


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
    if request.method == "POST":
        # process data as request contains data
        jobid = request.POST['jobid']
        jobtitle =request.POST['jobtitle']
        minsalary = request.POST['minsalary']
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
        # Send empty form because it is GET request
        return render(request,"add_job.html")


def delete_job(request):
    if request.method == "POST":
        # process data as request contains data
        jobid = request.POST['jobid']
        con = sqlite3.connect(r"e:\classroom\python\jan27\hr.db")
        cur = con.cursor()
        cur.execute("delete from jobs where id = ?", (jobid,))
        count = cur.rowcount
        con.commit()
        cur.close()
        con.close()
        if count == 1:
           return redirect("/hr/jobs")
        else:
           return render(request, "delete_job.html",
                         {'jobid' : jobid, 'message' : 'Job Id Not Found!'})
    else:
        # Send empty form because it is GET request
        return render(request,"delete_job.html")


def update_job(request):
    if request.method == "GET":
        f = JobForm()
        return render(request,'update_job.html',{'form' : f})
    else:  # POST
        pass


