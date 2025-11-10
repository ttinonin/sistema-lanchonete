from application import Application
from controller.funcionario_controller import FuncionarioController
from controller.cliente_controller import ClienteController
from controller.lanche_controller import LancheController
from controller.bebida_controller import BebidaController
from controller.pedido_controller import PedidoController
from flask import render_template, request, redirect, jsonify, flash, session

app = Application("prod")
funcionario_controller = FuncionarioController()
cliente_controller = ClienteController()
lanche_controller = LancheController()
bebida_controller = BebidaController()
pedido_controller = PedidoController()

@app.app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        try:
            funcionario = funcionario_controller.login(email, senha)
            session["usuario_id"] = funcionario.id
            return redirect("/funcionarios")
        except ValueError as e:
            flash(str(e), 'error')
            return redirect("/login")

@app.app.route("/logout")
def logout():
    session.pop("usuario_id", None)

    return redirect("/login")

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
def deletar_funcionario():
    funcionario_id = request.form["funcionario_id"]
    funcionario_controller.deletar(funcionario_id)
    return redirect("/funcionarios")

@app.app.route("/criar-cliente", methods=["GET"])
def criar_cliente_form():
    return render_template("cliente-criar.html")

@app.app.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]

        try:
            cliente_controller.criar(nome, telefone, endereco)
            return redirect("/clientes")
        except ValueError as error:
            flash(str(error), "error")
            return redirect("/criar-cliente")    
    elif request.method == "GET":
        clientes_l = cliente_controller.listar()
    
        return render_template("cliente-listar.html", clientes=clientes_l)

@app.app.route("/deletar-cliente", methods=["POST"])
def deletar_cliente():
    cliente_id = request.form["cliente_id"]
    cliente_controller.deletar(cliente_id)
    return redirect("/clientes")

@app.app.route("/criar-lanche", methods=["GET"])
def criar_lanche_form():
    return render_template("lanche-criar.html")

@app.app.route("/lanches", methods=["GET", "POST"])
def lanches():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        descricao = request.form["descricao"]

        try:
            lanche_controller.criar(nome, preco, descricao)
            return redirect("/lanches")
        except ValueError as error:
            flash(str(error), "error")
            return redirect("/criar-lanche")    
    elif request.method == "GET":
        lanches_l = lanche_controller.listar()
    
        return render_template("lanche-listar.html", lanches=lanches_l)

@app.app.route("/deletar-lanche", methods=["POST"])
def deletar_lanche():
    lanche_id = request.form["lanche_id"]
    lanche_controller.deletar(lanche_id)
    return redirect("/lanches")

@app.app.route("/criar-bebida", methods=["GET"])
def criar_bebida_form():
    return render_template("bebida-criar.html")

@app.app.route("/bebidas", methods=["GET", "POST"])
def bebidas():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        litragem = request.form["litragem"]

        try:
            bebida_controller.criar(nome, preco, litragem)
            return redirect("/bebidas")
        except ValueError as error:
            flash(str(error), "error")
            return redirect("/criar-bebida")    
    elif request.method == "GET":
        bebidas_l = bebida_controller.listar()
    
        return render_template("bebida-listar.html", bebidas=bebidas_l)

@app.app.route("/deletar-bebida", methods=["POST"])
def deletar_bebida():
    bebida_id = request.form["bebida_id"]
    bebida_controller.deletar(bebida_id)
    return redirect("/bebidas")

@app.app.route("/criar-pedido")
def criar_pedido():
    cleintes_l = cliente_controller.listar()
    lanches_l = lanche_controller.listar()
    bebidas_l = bebida_controller.listar()

    return render_template("criar-pedido.html", clientes=cleintes_l, lanches=lanches_l, bebidas=bebidas_l)

@app.app.route("/pedidos", methods=["GET", "POST"])
def pedidos():
    if request.method == "POST":
        cliente_id = request.form['cliente_id']
        lanches_ids = request.form.getlist('lanches[]')
        bebidas_ids = request.form.getlist('bebidas[]')
        funcionario_id = session.get("usuario_id")
        
        valor_total = 0

        for id in lanches_ids:
            lanche = lanche_controller.buscar(int(id))
            valor_total += lanche.preco

        for id in bebidas_ids:
            bebida = bebida_controller.buscar(int(id))
            valor_total += bebida.preco

        pedido_controller.criar(cliente_id, funcionario_id, valor_total, bebidas_ids, lanches_ids)
        return redirect("/pedidos")
    elif request.method == "GET":
        pedidos_l = pedido_controller.listar()

        return render_template("pedido-listar.html", pedidos=pedidos_l)

@app.app.route("/pedidos/<int:id>")
def single_pedido(id):
    pedido = pedido_controller.buscar(id)
    items = pedido_controller.buscar_pedido_items(id)

    return render_template("single-pedido.html", pedido=pedido, items=items)

if __name__ == "__main__":
    app.run()