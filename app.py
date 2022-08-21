from flask import Flask, jsonify, request, render_template, redirect, url_for
from validationservice import verify_application, get_all_applications, get_all_revisions_by_application

app = Flask(__name__)


@app.route('/validationapi/applications')
def get_applications():
    return render_template('index.html', applications=get_all_applications(), verification_status="")


@app.route('/validationapi/applications/<id>/revisions')
def get_revisions_by_application(application_id: str):
    return jsonify(get_all_revisions_by_application(application_id))


@app.route('/validationapi/applications/verify', methods=['POST'])
def verify_application_revision():
    application_id = request.form['application_id']
    approval_url = request.form['approval_url']
    clear_state_url = request.form['clear_state_url']

    result = verify_application(application_id, approval_url, clear_state_url)
    return redirect(url_for('get_applications'))


