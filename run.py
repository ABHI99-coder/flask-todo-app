# run.py


from todo import db, create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True, host="0.0.0.0", port=5000)

from flask import url_for

@app.route('/test-static')
def test_static():
    return url_for('static', filename='style.css')

