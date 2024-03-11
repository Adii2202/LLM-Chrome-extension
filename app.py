from flask import Flask, request, jsonify
from flask_cors import CORS
import llm_service

app = Flask(__name__)
CORS(app, origins="*")


@app.route('/summary', methods=['POST'])
def summarytext():
    data = request.json
    sel_text = data.get('text')
    prompt = data.get('prompt') 

    if len(sel_text) > 10:
        generated_text = llm_service.generate_text(prompt, sel_text)
        if generated_text is not None:
            return jsonify({"summary": generated_text})
        else:
            return jsonify({'error': 'Failed to generate text'})
    else:
        return jsonify({'summary': "Please select long text"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
