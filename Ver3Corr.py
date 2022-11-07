from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
import pymssql


@app.route('/', methods=['GET'])
def home():
   return redirect(url_for("InfoUser"))

@app.route('/BestCustomers', methods=['GET'])
def BestCustomers():
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'tolentino.mirko',password = 'xxx123##',database = 'tolentino.mirko')
    query = ""
    return render_template("Ver3Corr/home.html")
   


















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)