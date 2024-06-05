from flask import Flask
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Set up UPRN variable from environment
    app.config["UPRN"] = os.getenv("UPRN")

    with app.app_context():
        from app import routes

        routes.init_app(app)  # Pass the app object to routes.py

    return app
