from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth,routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title="Car Price Prediction API")

app.add_middleware(LoggingMiddleware)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Car Price Prediction API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
                color: #222;
                background: #f7f7f7;
            }
            main {
                max-width: 760px;
                margin: 0 auto;
                background: #fff;
                padding: 28px;
                border: 1px solid #ddd;
                border-radius: 8px;
            }
            h1 {
                margin-top: 0;
                color: #111;
            }
            a {
                color: #0b66c3;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            code {
                background: #eee;
                padding: 2px 6px;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <main>
            <h1>Car Price Prediction API</h1>
            <p>This FastAPI service predicts used car prices from vehicle details.</p>

            <h2>Available Routes</h2>
            <ul>
                <li><code>POST /login</code> - get a JWT access token</li>
                <li><code>POST /predict</code> - predict a car price</li>
                <li><a href="/docs">Swagger API Docs</a></li>
                <li><a href="/metrics">Prometheus Metrics</a></li>
            </ul>
        </main>
    </body>
    </html>
    """


# link endpoints
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags=['Prediction'])

# monitoring using Prometheus
Instrumentator().instrument(app).expose(app)

# add exception handler
register_exception_handlers(app)
