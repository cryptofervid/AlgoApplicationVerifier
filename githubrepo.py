import requests


class GithubCodeRepository:
    def __init__(self, url: str):
        self.url = url
        self.raw_url = self.get_url_for_code()
        self.commit_url = ''
        self.commit_id = ''

    def get_url_for_code(self):
        url = self.url
        url = url.replace("github.com", "raw.githubusercontent.com")
        url = url.replace("/blob/", "/")
        return url

    def get_url_for_commit(self):
        url = self.url
        url_components = url.split("/")
        user = url_components[3]
        user_repo = url_components[4]
        branch = url_components[6]

        commit_url = "https://api.github.com/repos/{}/{}/commits/{}"
        commit_url = commit_url.format(user, user_repo, branch)
        return commit_url

    def get_raw_code(self):
        response = requests.get(self.raw_url)
        response_text = ''

        if response.status_code == requests.codes.ok:
            response_text = response.text

        self.get_latest_commit_info()

        return response_text

    def get_latest_commit_info(self):
        fetch_commit_info_url = self.get_url_for_commit()
        response = requests.get(fetch_commit_info_url)

        if response.status_code == requests.codes.ok:
            response_json = response.json()
            self.commit_id = response_json['sha']

            if "/main/" in self.url:
                self.commit_url = self.url.replace("/main/", "/" + self.commit_id + "/")
            elif "/master/" in self.url:
                self.commit_url = self.url.replace("/master/", "/" + self.commit_id + "/")
            else:
                self.commit_url = self.url

