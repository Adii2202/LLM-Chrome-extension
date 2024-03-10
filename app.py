from flask import Flask, request, jsonify
from flask_cors import CORS
import llm_service

app = Flask(__name__)
CORS(app)

@app.route('/summary', methods=['POST'])
def summarytext():
    data = request.json()
    sel_text = data.get('text')

    if len(sel_text) > 10:
        summary = llm_service.generate_text(sel_text)
        return jsonify({"summary": summary})
    else:
        return jsonify({'summary': "Please select long text"})
if __name__ == "__main__":
    app.run(debug=True)
