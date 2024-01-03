from flask import Flask, request, jsonify, render_template # <- ; :D

app = Flask(__name__)

@app.route("/get-user<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
    }

    return render_template('frontend/load_url.html', user_data=jsonify(user_data)), 200
    # return jsonify(user_data), 200
    # render_template isn't defined; not anymore oh it seems to work now

@app.route("/")
def returnindex():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)