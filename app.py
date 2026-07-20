import os
from flask import Flask

app = Flask(__name__)

@app.route('')
def hello_world()
    return '''
    html
        head
            titleGCP Automated Apptitle
            style
                body { font-family Arial, sans-serif; text-align center; margin-top 100px; background-color #f4f6f9; }
                h1 { color #34a853; }
                p { color #5f6368; font-size 18px; }
            style
        head
        body
            h1🚀 Welcome to my Automated Cloud Run App!h1
            pThis deployment was triggered automatically via GitHub Actions  Cloud Build CICD Pipeline.p
        body
    html
    '''

if __name__ == __main__
    # Cloud Run يمرر المنفذ تلقائياً عبر متغير البيئة PORT
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)