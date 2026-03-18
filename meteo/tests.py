from django.test import TestCaseimport dash
from dash import html, dcc
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

# Créer l'app Dash
app = DjangoDash('SimpleDash')  

# Exemple de graphique
villes = ['Bafoussam', 'Douala', 'Yaoundé']
temperatures = [25, 30, 28]

app.layout = html.Div([
    html.H1('Dashboard Météo'),
    dcc.Graph(
        figure=go.Figure([go.Bar(x=villes, y=temperatures)])
    )
])


# Create your tests here.
