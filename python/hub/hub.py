"""
    hub.py - PiHub server
    Author: Hoanh An (hoanhan@bennington.edu)
    Date: 05/29/18
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test():
    """
    Test endpoint.
    """
    if request.method == 'GET':
        response = {
            'key': 'value',
        }
    elif request.method == 'POST':
        response = request.get_json()

    return jsonify(response)


if __name__ == '__main__':
    app.run()
