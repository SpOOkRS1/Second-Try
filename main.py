# As of April 13th everything is working and this is the last line of code that has been written. If anything is broken after this repl sucks. I won't be editing this anymore, this will serve as a template for my next project
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
