from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def start():
          return render_template('login.html')
@app.route('/login',methods=['POST'])
def menu():
        nome=request.form['nome']
        senha=request.form['senha']
        return render_template('return.html',nome=nome,senha=senha)
if __name__=='__main__':
        app.run(debug=True)