from flask import Flask,request,render_template
import json
from werkzeug.security import generate_password_hash,check_password_hash
app=Flask(__name__)
@app.route('/')
def start():

          return render_template('login.html')
@app.route('/login',methods=['POST'])
def menu():
        nome=request.form.get('nome')
        senha=request.form.get('senha')
        qtd_senha=len(senha)
        hashed_password=generate_password_hash(senha)
        check_password_hash(hashed_password,senha)
        if not senha or not nome or qtd_senha>7:
                msg='preencha todos os campos'
                return render_template('login.html',msg=msg)
        else:
            dados={'nome':nome,
               'senha':hashed_password
               }
            try:
               with open('dados/logs.json','r') as arq:
                      lista=json.load(arq)
            except FileNotFoundError:
                 lista=[]
            lista.append(dados)
            with open('dados/logs.json','w') as arq:
                   json.dump(lista,arq,indent=4)
            return render_template('return.html',nome=nome)
if __name__=='__main__':
        app.run(debug=True)