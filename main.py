from application import Application
from controller.funcionario_controller import FuncionarioController
from flask import render_template, request, redirect, jsonify, flash

app = Application("prod")
funcionario_controller = FuncionarioController()

@app.app.route("/criar-funcionario", methods=["GET"])
def criar_funcionario_form():
    return render_template("funcionario-criar.html")

@app.app.route("/funcionarios", methods=["GET", "POST"])
def funcionarios():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        senha_confirm = request.form["senha-confirm"]

        try:
            funcionario_controller.criar(nome, email, senha, senha_confirm)
            return redirect("/funcionarios")
        except ValueError as error:
            flash(str(error), "error")
            return redirect("/criar-funcionario")    
    elif request.method == "GET":
        funcionarios_l = funcionario_controller.listar()
    
        return render_template("funcionario-listar.html", funcionarios=funcionarios_l)

@app.app.route("/deletar-funcionario", methods=["POST"])
def deletar_usuario():
    funcionario_id = request.form["funcionario_id"]
    funcionario_controller.deletar(funcionario_id)
    return redirect("/funcionarios")

if __name__ == "__main__":
    app.run()