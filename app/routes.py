from datetime import datetime
from flask import render_template
from app.api_handler import get_collection_data
from app.utils import (
    date_formatter,
    next_bin_date,
    next_recycling_date,
    next_collection,
)


def init_app(app):  # Accept the app object as an argument
    @app.route("/")
    def index():
        uprn = app.config["UPRN"]  # Get UPRN from app config
        bin_data = get_collection_data(uprn)
        next_bin = date_formatter(next_bin_date(bin_data))
        next_recycling = date_formatter(next_recycling_date(bin_data))
        next_bin_type = next_collection(bin_data)
        current_date = date_formatter(datetime.now().date())

        return render_template(
            "index.html",
            next_bin=next_bin,
            next_recycling=next_recycling,
            next_bin_type=next_bin_type,
            current_date=current_date,
        )
