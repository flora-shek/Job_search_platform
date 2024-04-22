from flask import Flask, jsonify, render_template, request

from database import load_jobs_from_db, load_job_from_db,add_application_to_db,load_applications_from_db

from hcaptcha import verify_hcaptcha,site_key

app = Flask(__name__)

JOBS = load_jobs_from_db()

@app.route("/")
def hello_jovian():
  
  return render_template("index.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/api/application/<id>")
def show_application(id):
  job = load_applications_from_db(id)
  if not job:
    return "Not Found",404
  return jsonify(job)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  
  if not job:
    return "Not Found",404
  return render_template("jobpage.html",job = job,site_key = site_key)
  
@app.route("/job/<id>/apply", methods=["post"])
def apply_to_job(id):
  token = request.form.get('g-recaptcha-response')
  if verify_hcaptcha(token):
      data = request.form
      job = load_job_from_db(id)
      add_application_to_db(id,data)
      return render_template("application.html",application = data,job = job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4530, debug=True)
