import os
from io import BytesIO
from flask import Flask, render_template, request, send_file, abort
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York',
    'salary': '$150,000'
}, {
    'id': 2,
    'title': 'Data scientist',
    'location': 'New Delhi',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'DevOps Engineer',
    'location': 'Bengaluru',
}, {
    'id': 4,
    'title': 'Cloud Engineer',
    'location': 'Remote',
    'salary': 'Rs. 21,00,0000'
}, {
    'id': 5,
    'title': 'Full-Stack Developer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}, {
    'id': 6,
    'title': 'Python Developer',
    'location': 'Pune',
    'salary': 'Rs. 8,00,000'
}]


@app.route("/")
def hello_career():
    return render_template("home.html", jobs=JOBS, company='sa')



@app.route("/apply/<int:job_id>")
def apply_job(job_id):
    job = next((job for job in JOBS if job["id"] == job_id), None)
    return render_template("apply_form.html", job=job)



@app.route("/apply/<int:job_id>/success" , methods=['POST'])
def apply_success(job_id):
   job = next((job for job in JOBS if job["id"] == job_id), None)
   if request.method == 'POST':
        job_id_no = job_id
        job_title = job["title"]
        applicant_name = request.form.get('aname')
        applicant_email = request.form.get('email')
        applicant_phno = request.form.get('phone')
        resumex = request.files['resume']
        coverletter = request.form.get('cover')
        resume= resumex.read()
        resumeFilename = resumex.filename

        cursor = mysql.connection.cursor()
        cursor.execute('''
        INSERT INTO userinfo (job_id_no, job_title, applicant_name, applicant_email, applicant_phno, resume, resumeFilename, coverletter)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', (job_id_no, job_title, applicant_name, applicant_email, applicant_phno, resume, resumeFilename, coverletter))
        
        mysql.connection.commit()
        cursor.close()

   return render_template("apply-successful.html", job =job)


@app.route('/download/<int:upload_id>')
def download_resume(upload_id):
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT resume, resumeFilename FROM userinfo WHERE id = %s ''', (upload_id,))
    result = cursor.fetchone()
    cursor.close()

    if result is None:
        abort(404)
    resume = result[0]
    resumeFilename = result[1]

    resume_io = BytesIO(resume)
    return send_file(resume_io, download_name=resumeFilename, as_attachment=True)


@app.route("/contact")
def contact_email():
    return render_template("email.html")

if __name__ == "__main__":
  app.run(debug=True)


# REF: https://geekpython.in/create-and-integrate-mysql-database-with-flask-app