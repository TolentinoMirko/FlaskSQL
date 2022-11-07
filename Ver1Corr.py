from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
import pymssql



@app.route('/', methods=['GET'])
def home():
    return render_template("Ver1Corr/home.html")

@app.route('/ricerca', methods=['GET'])
def ricerca():
    nomestore = request.args['store']
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'tolentino.mirko',password = 'xxx123##',database = 'tolentino.mirko')
    query = f"SELECT sf.first_name,sf.last_name FROM sales.stores as st INNER JOIN sales.staffs as sf on sf.store_id = st.store_id WHERE st.store_name = '{nomestore}'"
    df = pd.read_sql(query,conn)
    dati = list(df.values.tolist()) #nella lista saranno contenute i dati in base allo store scelto dall'utente
    if dati == []: #controlla se la lista è vuota
         return render_template("Ver1Corr/error.html")
    else:

        return render_template("Ver1Corr/risultati.html", nomiColonne = df.columns.values,dati = list(df.values.tolist()))




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)