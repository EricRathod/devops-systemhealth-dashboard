import platform
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template

from config import Config


def create_app(test_config=None):
    """Create and configure the Flask application."""

    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    @app.route("/")
    def home():
        """Display the system health dashboard."""

        system_information = {
            "application": Config.APP_NAME,
            "status": "Operational",
            "version": Config.APP_VERSION,
            "environment": Config.APP_ENV,
            "python_version": platform.python_version(),
            "operating_system": platform.system(),
            "checked_at": datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S UTC"
            ),
        }

        return render_template(
            "index.html",
            system_information=system_information,
        )

    @app.route("/health")
    def health():
        """Return the application health status."""

        return jsonify(
            {
                "status": "healthy",
                "service": "devops-system-health-dashboard",
                "environment": Config.APP_ENV,
                "version": Config.APP_VERSION,
            }
        ), 200

    @app.route("/api/info")
    def application_info():
        """Return application information."""

        return jsonify(
            {
                "application": Config.APP_NAME,
                "version": Config.APP_VERSION,
                "environment": Config.APP_ENV,
                "python_version": platform.python_version(),
                "operating_system": platform.system(),
            }
        ), 200

    @app.errorhandler(404)
    def page_not_found(error):
        """Return JSON when a route does not exist."""

        return jsonify(
            {
                "error": "Not Found",
                "message": "The requested endpoint does not exist.",
            }
        ), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        """Return JSON for unexpected server errors."""

        return jsonify(
            {
                "error": "Internal Server Error",
                "message": "An unexpected error occurred.",
            }
        ), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=Config.DEBUG,
    )