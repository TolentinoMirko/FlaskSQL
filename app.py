from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("search.html")

@app.route('/result', methods=['GET'])
def result():
    #1 collegamento al database
    import pandas as pd
    import pymssql
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'tolentino.mirko',password = 'xxx123##',database = 'tolentino.mirko')

    #2 invio query al database ricezione informazioni
    nomeprodotto =request.args['nomeprodotto']
    query = f"select * from production.products where product_name like '{nomeprodotto}%'"
    dfprodotti = pd.read_sql(query,conn)
    
    #3 visualizzare le info 

    
    
    return render_template('result.html', nomiColonne = dfprodotti.columns.values, dati = list(dfprodotti.values.tolist()))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)