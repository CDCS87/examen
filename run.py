from flask import Flask, request, render_template
app = Flask(__name__)

# Datos de usuarios registrados
usuarios = {
    "juan": "admin",
    "pepe": "user"
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre1 = request.form.get('nombre1')
        edad = int(request.form.get('edad', 0))
        pintura = int(request.form.get('pintura', 0))

        # Pintura a precio normal
        precio_unitario = 9000
        total_sin_descuento = pintura * precio_unitario

        # Determinar el descuento según la edad
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        # Calcular el total con descuento
        descuento_aplicado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_aplicado

        # Redondear los valores
        total_sin_descuento = round(total_sin_descuento, 2)
        descuento_aplicado = round(descuento_aplicado, 2)
        total_con_descuento = round(total_con_descuento, 2)

        # Pasar los valores a la plantilla
        return render_template(
            'ejercicio1.html',
            nombre1=nombre1,
            edad=edad,
            pintura=pintura,
            total_sin_descuento=total_sin_descuento,
            descuento_aplicado=descuento_aplicado,
            total_con_descuento=total_con_descuento,
            enviado=True
        )

    # Renderizar formulario inicial
    return render_template('ejercicio1.html', enviado=False)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in usuarios and usuarios[username] == password:
            if username == "juan":
                mensaje = f"Bienvenido Administrador {username}"
            else:
                mensaje = f"Bienvenido Usuario {username}"
            return render_template('ejercicio2.html', mensaje=mensaje, autenticado=True)
        else:
            error = "Usuario o contraseña incorrectos"
            return render_template('ejercicio2.html', error=error)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
