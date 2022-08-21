from dbhelper import get_db_connection


class Application:
    def __init__(self, id, status):
        self.id = id
        self.status = status
        self.revisions = []

    def save(self):
        conn = get_db_connection()
        conn.execute('INSERT INTO application (id, status) VALUES (?,?) ON CONFLICT (id) DO '
                     'UPDATE SET status = ?', (self.id, self.status, self.status))
        conn.commit()
        conn.close()


class Revision:
    def __init__(self, application, status, date, commit_id, approval_url, clear_state_url):
        self.commit_id = commit_id
        self.application = application
        self.status = status
        self.date = date
        self.approval_url = approval_url
        self.clear_state_url = clear_state_url

    def save(self):
        conn = get_db_connection()
        conn.execute('INSERT INTO revision (application, status, validation_time, commit_id, '
                     'approval_url, clear_state_url) VALUES (?,?,?,?,?,?) ON CONFLICT (commit_id) DO '
                     'UPDATE SET status = ?, validation_time = ?, approval_url = ?, clear_state_url = ? '
                     , (self.application, self.status, self.date, self.commit_id, self.approval_url,
                        self.clear_state_url, self.status, self.date, self.approval_url,
                        self.clear_state_url))
        conn.commit()
        conn.close()
