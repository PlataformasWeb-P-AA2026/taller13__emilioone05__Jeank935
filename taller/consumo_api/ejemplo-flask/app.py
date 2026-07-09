from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from config import usuario, clave

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'una-clave-secreta-000001'

token = 'd34e8cc02da88a9f83cf74ec31c6525bc10f8924'
API_URL = "http://localhost:8000/api"
headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }


def obtener_json(respuesta):
    if respuesta.status_code >= 400:
        return {
            "error": "Error al consumir la API",
            "estado": respuesta.status_code,
            "detalle": respuesta.text,
        }
    return json.loads(respuesta.content)


def mostrar_error_api(error):
    return "Error %s: %s" % (error["estado"], error["detalle"])


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/los/edificios")
def los_edificios():
    
    r = requests.get(f"{API_URL}/edificios/", headers=headers)
    # r = requests.get("http://127.0.0.1:8000/api/edificios/",
    #         auth=(usuario, clave))

    respuesta = obtener_json(r)
    if "error" in respuesta:
        return mostrar_error_api(respuesta)
    edificios = respuesta['results']
    numero_edificios = respuesta['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/los/departamentos")
def los_departamentos():
    """
    """
    r = requests.get(f"{API_URL}/departamentos/", headers=headers)
    respuesta = obtener_json(r)
    if "error" in respuesta:
        return mostrar_error_api(respuesta)
    datos = respuesta['results']
    numero = respuesta['count']
    return render_template("losdepartamentos.html", datos=datos,
    numero=numero)


@app.route("/crear/edificio", methods=["GET", "POST"])
def crear_edificio():
    if request.method == "POST":
        datos = {
            "nombre": request.form["nombre"],
            "direccion": request.form["direccion"],
            "ciudad": request.form["ciudad"],
            "tipo": request.form["tipo"],
        }
        r = requests.post(f"{API_URL}/edificios/", headers=headers, json=datos)
        respuesta = obtener_json(r)
        if "error" in respuesta:
            return mostrar_error_api(respuesta)
        return redirect(url_for("los_edificios"))

    return render_template("crear_edificio.html")


@app.route("/crear/departamento", methods=["GET", "POST"])
def crear_departamento():
    edificios_r = requests.get(f"{API_URL}/edificios/", headers=headers)
    edificios_respuesta = obtener_json(edificios_r)
    if "error" in edificios_respuesta:
        return mostrar_error_api(edificios_respuesta)

    if request.method == "POST":
        datos = {
            "nombre_completo_propietario": request.form["nombre_completo_propietario"],
            "costo_departamento": request.form["costo_departamento"],
            "numero_cuartos": request.form["numero_cuartos"],
            "edificio": request.form["edificio"],
        }
        r = requests.post(f"{API_URL}/departamentos/", headers=headers, json=datos)
        respuesta = obtener_json(r)
        if "error" in respuesta:
            return mostrar_error_api(respuesta)
        return redirect(url_for("los_departamentos"))

    return render_template(
        "crear_departamento.html",
        edificios=edificios_respuesta["results"],
    )


# @app.route("/lostelefonosdos")
# def los_telefonos_dos():
#     """
#     """
#     r = requests.get("http://127.0.0.1:8000/api/numerost/",
#             auth=(usuario, clave))
#     datos = json.loads(r.content)['results']
#     numero = json.loads(r.content)['count']
#     datos2 = []
#     for d in datos:
#         datos2.append({'telefono':d['telefono'], 'tipo':d['tipo'],
#         'estudiante': obtener_estudiante(d['estudiante'])})
#     return render_template("lostelefonosdos.html", datos=datos2,
#     numero=numero)

# funciones ayuda

# def obtener_estudiante(url):
#     """
#     """
#     r = requests.get(url, auth=(usuario, clave))
#     nombre_estudiante = json.loads(r.content)['nombre']
#     apellido_estudiante = json.loads(r.content)['apellido']
#     cadena = "%s %s" % (nombre_estudiante, apellido_estudiante)
#     return cadena


if __name__ == "__main__":
    app.run(debug=True, port=5000)
