from flask import Flask, jsonify, render_template

from database import load_jobs_from_db

app = Flask(__name__)


  
JOBS = load_jobs_from_db()

@app.route("/")
def hello_jovian():
  
  return render_template("index.html", jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4530, debug=True)
