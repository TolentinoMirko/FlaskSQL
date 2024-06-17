from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/accedi', methods=['GET'])
def result():
    #1 collegamento al database
    import pandas as pd
    import pymssql
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'tolentino.mirko',password = 'xxx123##',database = 'tolentino.mirko')

    #2 invio query al database ricezione informazioni
    user_name =request.args['user']
    password = request.args['pass']
    query = f"select * from accesso where user='{user}%' and password = '{pass}%'"

    df = pd.read_sql(query,conn)
    dati = list(df.values.tolist()) #nella lista saranno contenute i dati in base allo store scelto dall'utente
    if dati == []: #controlla se la lista è vuota
         return render_template("error.html")
    else:
        return render_template("continuo.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
