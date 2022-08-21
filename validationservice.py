from algohelper import AlgoTealHelper
from githubrepo import GithubCodeRepository
from dbhelper import get_db_connection
from typing import List, Dict, Any
from model import Application, Revision
import datetime


def get_all_applications() -> List[Dict[str, Any]]:
    return_value = []
    application_dict = {}

    conn = get_db_connection()
    project_rows = conn.execute('SELECT application.id, application.status, r.application, r.status, '
                                'r.validation_time, r.commit_id, r.approval_url, r.clear_state_url  '
                                'FROM application INNER JOIN revision r on application.id = r.application ORDER BY '
                                'r.validation_time DESC').fetchall()
    conn.close()

    for row in project_rows:
        application_id = row[0]
        if application_id not in application_dict:
            application = Application(row[0], row[1])
            application_dict[application.id] = application

        revision = Revision(row[2], row[3], row[4], row[5], row[6], row[7])
        application.revisions.append(revision)

    for application in application_dict.values():
        return_value.append(application.__dict__)

    return return_value


def get_all_revisions_by_application(application_id: str) -> List[Dict[str, Any]]:
    revisions = []

    conn = get_db_connection()
    commit_rows = conn.execute('SELECT * FROM revision WHERE application = ?', application_id).fetchall()
    conn.close()

    for row in commit_rows:
        revisions.append(Revision(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).__dict__)

    return revisions


def verify_approval_code(algo_teal_helper: AlgoTealHelper, approval_repo: GithubCodeRepository) -> bool:
    approval_code = approval_repo.get_raw_code()

    generated_approval_bytecode = algo_teal_helper.teal_to_bytecode(approval_code)

    if generated_approval_bytecode == algo_teal_helper.approval:
        return True
    else:
        return False


def verify_clear_state_code(algo_teal_helper: AlgoTealHelper, clear_state_repo: GithubCodeRepository) -> bool:
    clear_state_code = clear_state_repo.get_raw_code()

    generated_clear_state_bytecode = algo_teal_helper.teal_to_bytecode(clear_state_code)

    if generated_clear_state_bytecode == algo_teal_helper.clear:
        return True
    else:
        return False


def verify_application(application_id: str, approval_url: str, clear_state_url: str) -> Dict:
    algo_teal_helper = AlgoTealHelper(application_id)
    algo_teal_helper.download_teal_bytecode()

    approval_repo = GithubCodeRepository(approval_url)
    approval_comparison_result = verify_approval_code(algo_teal_helper, approval_repo)

    clear_state_repo = GithubCodeRepository(clear_state_url)
    clear_state_comparison_result = verify_clear_state_code(algo_teal_helper, clear_state_repo)

    status = 'Unverified'

    if approval_comparison_result is True and clear_state_comparison_result is True:
        status = 'Verified'

    application = Application(application_id, status)
    application.save()

    utc_time = datetime.datetime.utcnow()
    revision = Revision(application_id, status, utc_time.strftime('%Y-%m-%d %H:%M:%S'), approval_repo.commit_id,
                        approval_repo.commit_url, clear_state_repo.commit_url)
    revision.save()

    return {"status": status}
