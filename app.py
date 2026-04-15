from flask import Flask, render_template_string, request
from datetime import date

app = Flask(__name__)

# Este es el diseño de tu interfaz (HTML sencillo)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora de Días</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; }
        input { padding: 10px; margin: 10px; }
        .resultado { font-weight: bold; color: blue; font-size: 1.2em; }
    </style>
</head>
<body>
    <h2>📅 Calculadora de Días</h2>
    <form method="POST">
        <label>Elige la fecha objetivo:</label><br>
        <input type="date" name="target_date" required>
        <br>
        <input type="submit" value="Calcular">
    </form>
    {% if days is not none %}
        <div class="resultado">
            {{ mensaje }}
        </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    days = None
    mensaje = ""
    if request.method == 'POST':
        today = date.today()
        # Recibimos la fecha del calendario
        target_str = request.form.get('target_date')
        target_date = date.fromisoformat(target_str)
        
        days = (target_date - today).days
        
        if days > 0:
            mensaje = f"Faltan {days} días para el objetivo."
        elif days == 0:
            mensaje = "¡Es hoy!"
        else:
            mensaje = f"Pasó hace {abs(days)} días."
            
    return render_template_string(HTML_TEMPLATE, days=days, mensaje=mensaje)