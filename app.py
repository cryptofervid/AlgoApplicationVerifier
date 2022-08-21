from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from validationservice import verify_teal_application, get_all_applications, get_all_revisions_by_application, \
    verify_pyteal_application

app = Flask(__name__)


@app.route('/validationapi/applications')
def get_applications():
    return render_template('index.html', applications=get_all_applications(), verification_status="")


@app.route('/validationapi/applications/<id>/revisions')
def get_revisions_by_application(application_id: str):
    return jsonify(get_all_revisions_by_application(application_id))


@app.route('/validationapi/applications/verify', methods=['POST'])
def verify_application_revision():

    type = request.form['source_type']

    if type == "Teal":

        application_id = request.form['application_id']
        approval_url = request.form['approval_url']
        clear_state_url = request.form['clear_state_url']

        application_id = int(application_id)

        result = verify_teal_application(application_id, approval_url, clear_state_url)

    if type == "PyTeal":

        application_id = request.form['application_id']
        approval_url = request.form['approval_url']
        clear_state_url = request.form['clear_state_url']
        approval_method = request.form['approval_method']
        clear_state_method = request.form['clear_state_method']
        teal_version = request.form['teal_version']

        application_id = int(application_id)
        teal_version = int(teal_version)

        result = verify_pyteal_application(application_id, approval_url, clear_state_url, approval_method, clear_state_method, teal_version)

    if result:
        flash('Application verification passed', 'success')
    else:
        flash('Application verification failed', 'danger')

    return redirect(url_for('get_applications'))


