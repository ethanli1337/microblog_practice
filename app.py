import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv 
import os 


def create_app():

    app = Flask(__name__)
    db_url=os.getenv("DATABASE_URL")
    client=MongoClient(db_url)
    app.db=client.microblog


    todos = [("Get milk", False), 
            ("Learn programing", True)
             ]
    # entries=[]

    # @app.route("/", methods=['GET', 'POST'])
    # def home():
    #     print([e for e in app.db.entries.find({})])
    #     if request.method=="POST":
    #         entry_content=request.form.get("content")
    #         formatted_date=datetime.datetime.today().strftime("%Y-%m-%d")
    #         app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

    #     entries_with_date=[
    #         (
    #             entry["content"], 
    #             entry["date"], 
    #             datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            
    #         )
    #         for entry in app.db.entries.find({})
    #     ]

    #     return render_template("home.html", entries=entries_with_date)
    

    # @app.route("/jinja", methods=['GET', 'POST'])
    # def todo():
    #     return render_template("home2.html", todos=["Get milk", "Learn programming"])

    @app.route("/")
    def todo():
        return render_template("home2.html", todos=todos)
    return app
