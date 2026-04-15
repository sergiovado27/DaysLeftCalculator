from flask import Flask, render_template_string, request
from datetime import date

app = Flask(__name__)

# Diseño visual de la aplicación
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Días</title>
    <style>
        body { font-family: -apple-system, system-ui, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f0f2f5; }
        .card { background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; max-width: 400px; width: 90%; }
        h2 { color: #1a73e8; margin-bottom: 1.5rem; }
        input[type="date"] { padding: 12px; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; margin-bottom: 1rem; width: 80%; }
        input[type="submit"] { background: #1a73e8; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 1rem; cursor: pointer; transition: background 0.3s; }
        input[type="submit"]:hover { background: #1557b0; }
        .resultado { margin-top: 1.5rem; padding: 1rem; border-radius: 8px; font-weight: bold; background: #e8f0fe; color: #1967d2; }
    </style>
</head>
<body>
    <div class="card">
        <h2>📅 Mi App de Días</h2>
        <form method="POST">
            <input type="date" name="target_date" required>
            <br>
            <input type="submit" value="Calcular Días">
        </form>
        {% if mensaje %}
            <div class="resultado">{{ mensaje }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    mensaje = ""
    if request.method == 'POST':
        try:
            target_str = request.form.get('target_date')
            target_date = date.fromisoformat(target_str)
            today = date.today()
            days = (target_date - today).days
            
            if days > 0:
                mensaje = f"Faltan {days} días para el objetivo."
            elif days == 0:
                mensaje = "¡Es hoy! El día ha llegado."
            else:
                mensaje = f"Esa fecha ya pasó hace {abs(days)} días."
        except Exception:
            mensaje = "Por favor, selecciona una fecha válida."
            
    return render_template_string(HTML_TEMPLATE, mensaje=mensaje)

# Esto permite que Vercel maneje la app como una función
app = app