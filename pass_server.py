#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/change-pass/<new_pass>', methods=['GET'])
def get_task(new_pass):
    file = open('secret.pass', 'w')
    for i in range(0,len(new_pass)):
        file.write(new_pass[i])
        file.write(' ')
    file.close()
    return "Pass changed!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
