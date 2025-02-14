from flask import Flask, render_template, request, jsonify
import openai
import requests

app = Flask(__name__)

OPENAI_API_KEY = "your_openai_api_key"

def ai_skip_trace(name, last_known_location):
    prompt = f"""
    You are an AI-powered skip tracing expert.
    - The individual: {name}
    - Last known location: {last_known_location}

    Step 1: Identify possible new locations based on common migration patterns.
    Step 2: Suggest family members, associates, or social media connections that could help.
    Step 3: Provide databases or techniques to verify new leads.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI-powered skip tracing expert."},
                  {"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )

    return response["choices"][0]["message"]["content"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        last_known_location = request.form["location"]
        result = ai_skip_trace(name, last_known_location)
        return jsonify({"result": result})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
