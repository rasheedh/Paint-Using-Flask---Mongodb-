from flask import Flask,request,session,g,redirect,url_for,render_template
import pickle
import json
import os
from pymongo import Connection

app=Flask(__name__)

@app.route("/<filename>")
def draw(filename):
	wholedata=[]
	fname=[]
	connect = Connection()
	db=connect.database
        cur = db.collection
	for row in cur.find():
		if unicode(filename)==row[u'filename']:
			wholedata= str(row[u'imagedata'])
	return render_template("paint11.html",lis=fname,imagedata=wholedata)
	

@app.route("/h/",methods=['POST'])
def h():
	fname=request.form['fnam']
	imagedata=request.form['image']
	connect = Connection()
	db=connect.database
        cur = db.collection	
	cur.insert({"filename":fname,"imagedata":imagedata})
	return redirect(url_for('hello'))
	
@app.route("/")
def hello():
	filename=[]
	wholedata=[]
	return render_template("paint11.html",lis=filename,imagedata=wholedata) 

if __name__=="__main__":
	app.run()
