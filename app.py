from flask import Flask, request, render_template
import openai
import os
from flask import send_from_directory

openai.api_key = os.getenv("OPENAI_API_KEY")  # Provided by Render

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4.1",
                messages=[{"role": "user", "content": user_prompt}]
            )
            response_text = response.choices[0].message.content.strip()
        except Exception as e:
            response_text = f"Error: {e}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
