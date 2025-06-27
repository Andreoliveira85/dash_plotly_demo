# app.py
import dash
from dash import Dash

from components.layout import get_layout
from components.callbacks import register_callbacks
from utils.data_loader import load_data

# Load and store data once
df = load_data()

# Initialize app
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Global Indicators Dashboard"
app.layout = get_layout(df)

# Register callbacks
register_callbacks(app, df)

if __name__ == '__main__':
    import os
    app.run(
        debug=False,
        host="0.0.0.0",
        port = port=int(os.environ.get("PORT", 8050))
           )
