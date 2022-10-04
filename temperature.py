# ISIP, Angel Mary M._Q27

from flask import Flask, jsonify, request

app = Flask(__name__)
temperature=[
    {
        "temp_id": "0",
        "date": "10/01/2022",
        "temperature": "25 °C"
    },

    {
        "temp_id": "1",
        "date": "10/02/2022",
        "temperature": "27 °C"
    }
]

@app.route('/temperature', methods=['GET'])
def displayTemperature():
    return jsonify(temperature)

@app.route('/temperature/<int:index>', methods=['GET'])
def displayById(index):
    return jsonify(temperature[index])

@app.route('/temperature', methods=['POST'])
def addTemperature():
    temp = request.get_json()
    temperature.append(temp)
    return {'id':len(temperature)},200

@app.route('/temperature/<int:index>', methods=["DELETE"])
def deleteTemperature(index):
    temperature.pop(index)
    return 'Temperature was successfully deleted', 200

if __name__ == '__main__':
    app.run()