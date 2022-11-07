from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
import pymssql

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for("InfoUser"))

@app.route('/InfoUser', methods=['GET'])
def InfoUser():
   return render_template("Ver2Corr/home.html")


@app.route('/Informazioni', methods=['GET'])
def Informazioni():
    nomecliente = request.args['nome']
    cognomecliente = request.args['cognome']
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'tolentino.mirko',password = 'xxx123##',database = 'tolentino.mirko')
    query = f"SELECT * FROM sales.customers WHERE sales.customers.first_name = '{nomecliente}' and sales.customers.last_name = '{cognomecliente}'"
    df = pd.read_sql(query,conn)
    dati = list(df.values.tolist()) 
    if dati == []: 
         return render_template("Ver1Corr/error.html")
    else:

        return render_template("Ver2Corr/infouser.html", nomiColonne = df.columns.values,dati = list(df.values.tolist()))

        












if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)