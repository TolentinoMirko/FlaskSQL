from flask import Flask, render_template, request,redirect,url_for,Response
app = Flask(__name__)
import pandas as pd
import pymssql
import matplotlib.pyplot as plt
conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'tolentino.mirko',password = 'xxx123##',database = 'tolentino.mirko')



@app.route('/', methods=['GET'])
def home():
    return render_template("eserciziSQL/home.html")

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args['scelta']
    if scelta == "es1":
        return redirect(url_for("prodxcat"))
    elif scelta == "es2":
        return redirect(url_for("ordxstore"))
    else:
        return redirect(url_for("elencoprod"))

#_________________________________________________________________________________

@app.route('/prodxcat', methods=['GET'])
def prodxcat():
    query = 'select category_name, count(*) as num_prod from production.products inner join production.categories on products.category_id = categories.category_id group by category_name'
    df = pd.read_sql(query,conn)

    return render_template("eserciziSQL/prodxcat.html",NomiColonne =df.columns.values, dati =list(df.values.tolist()),)

#_________________________________________________________________________________

@app.route('/ordxstore', methods=['GET'])
def ordxstore():
    query2 = 'Select brand_name, count (*) as num_prod From production.products Inner join production.brands on production.products.brand_id = production.brands.brand_id Group by brand_name order by num_prod asc '
    df2 = pd.read_sql(query2,conn)

    return render_template("eserciziSQL/ordxstore.html",NomiColonne2 =df2.columns.values, dati2 =list(df2.values.tolist()))

#_________________________________________________________________________________


@app.route('/elencoprod', methods=['GET'])
def elencoprod():
    nomeprodotto =request.args['nomeprodotto']
    query3 = f"select * from production.products where product_name like '{nomeprodotto}%'"
    df3 = pd.read_sql(query3,conn)

    return render_template("eserciziSQL/elencoprod.html",NomiColonne3 =df3.columns.values, dati3 =list(df3.values.tolist()))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)