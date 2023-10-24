from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Islamabad, Pakistan',
  'Salary': '210,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Islamabad, Pakistan',
  'Salary': '210,000'
}, {
  'id': 3,
  'title': 'Data Analyst',
  'location': 'Islamabad, Pakistan',
  'Salary': '210,000'
}, {
  'id': 4,
  'title': 'Data Analyst',
  'location': 'Islamabad, Pakistan',
  'Salary': '210,000'
}, {
  'id': 5,
  'title': 'Data Analyst',
  'location': 'Islamabad, Pakistan',
  'Salary': '210,000'
}]


@app.route("/")
def hello_world():
  return render_template('index.html', jobs=JOBS, company_name='SAM')


@app.route("/api/services")
def list_services():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
