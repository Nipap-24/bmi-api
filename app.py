from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    data = request.json
    weight = float(data['weight'])
    height = float(data['height']) / 100  # แปลง cm เป็น m
    bmi = weight / (height ** 2)

    return jsonify({'bmi': round(bmi, 2)})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Route สำหรับหน้าแรก
@app.route('/')
def home():
    return "Welcome to BMI API! Use /bmi with POST method to calculate BMI."

# Route สำหรับคำนวณ BMI
@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    data = request.json
    weight = float(data['weight'])
    height = float(data['height']) / 100  # แปลง cm เป็น m
    bmi = weight / (height ** 2)
    return jsonify({'bmi': round(bmi, 2)})

if __name__ == '__main__':
    app.run(debug=True)
