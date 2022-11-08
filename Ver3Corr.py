from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
import pymssql


@app.route('/', methods=['GET'])
def home():
   return redirect(url_for("BestCustomers"))

@app.route('/BestCustomers', methods=['GET'])
def BestCustomers():
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'tolentino.mirko',password = 'xxx123##',database = 'tolentino.mirko')
    query = "SELECT TOP 10 customers.customer_id, customers.first_name, customers.last_name ,SUM(list_price) as spesa_totale FROM sales.customers INNER JOIN sales.orders ON sales.customers.customer_id = sales.orders.customer_id INNER JOIN sales.order_items ON sales.order_items.order_id = sales.orders.order_id GROUP BY customers.customer_id, customers.first_name, customers.last_name ORDER BY SUM(list_price) DESC"
    #nel group by aggiungo l'id(chiave),nome e cognome(così mostreremo anche loro) 
    df = pd.read_sql(query,conn)
    return render_template("Ver3Corr/home.html",nomiColonne = df.columns.values,dati = list(df.values.tolist()))
   

@app.route('/TotaleOrdini', methods=['GET'])
def TotaleOrdini(valore):
   return
















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)