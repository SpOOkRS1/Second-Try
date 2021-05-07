# As of April 29th Error: "no such table named chore" 
from website import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')