from image_pixel_coordinate import image_pixel_coordinate
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def calculate():
    data = request.get_json(force=True)
    dim = data['dimension']
    corner_points = data['corner points']
    solution = image_pixel_coordinate(dim, corner_points)
    return jsonify(solution)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
