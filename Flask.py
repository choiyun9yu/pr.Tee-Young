from flask import Flask

app=Flask()

@app.route('/', method=['GET', "POST"])
def main():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)