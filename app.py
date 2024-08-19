from flask import Flask
from routes import main_bp
import os

app = Flask(__name__)

with app.app_context():
    
    app.register_blueprint(main_bp)

if __name__ == '__main__':
    port_number = int(os.environ.get('FLASK_RUN_PORT', 5000))
    app.run(host='0.0.0.0', port=port_number)
