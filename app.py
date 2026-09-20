import os
from flask import Flask,jsonify,send_from_directory
def create_app():
 a=Flask(__name__,static_folder="static",static_url_path="/static")
 @a.get("/")
 def home():return send_from_directory(a.static_folder,"index.html")
 @a.get("/api/health")
 def health():return jsonify(status="ok",version="1.2.0")
 return a
app=create_app()
if __name__=="__main__":app.run(host="127.0.0.1",port=int(os.getenv("PORT",5050)))
