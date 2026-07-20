import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Welcome to my Automated GCP Web App!</h1>"

if __name__ == '__main__':
    # الحصول على المنفذ من البيئة السحابية، والافتراضي هو 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)