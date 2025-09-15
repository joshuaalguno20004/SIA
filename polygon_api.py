from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def polygon_area(n, s):
    """Calculate area of a regular polygon with n sides of length s"""
    if n < 3 or n > 10:
        return None
    return (n * s * s) / (4 * math.tan(math.pi / n))

@app.route('/')
def home():
    return {"message": "Polygon Area API - Supports 3 to 10 sides"}

@app.route('/area', methods=['GET', 'POST'])
def get_area():
    try:
        if request.method == 'GET':
            n = int(request.args.get('sides'))
            s = float(request.args.get('length'))
        else:  # POST
            data = request.get_json()
            n = int(data.get('sides'))
            s = float(data.get('length'))

    except (TypeError, ValueError, AttributeError):
        return {"error": "Please provide valid 'sides' (int) and 'length' (float)"}, 400

    area = polygon_area(n, s)
    if area is None:
        return {"error": "Only polygons with 3 to 10 sides are supported"}, 400

    return {
        "sides": n,
        "length": s,
        "area": round(area, 4)
    }

if __name__ == '__main__':
    app.run(debug=True)
