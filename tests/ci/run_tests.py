import os
import time
from github import Github
from github.Commit import Commit

from env_helper import GITHUB_REPOSITORY, GITHUB_SHA, GH_PERSONAL_ACCESS_TOKEN, GITHUB_RUN_URL

RETRY = 5


def get_commit(gh: Github, commit_sha: str, retry_count: int = RETRY) -> Commit:
    for i in range(retry_count):
        try:
            repo = gh.get_repo(GITHUB_REPOSITORY)
            commit = repo.get_commit(commit_sha)
            break
        except Exception as ex:
            if i == retry_count - 1:
                raise ex
            time.sleep(i)

    return commit


if __name__ == '__main__':
    assert GH_PERSONAL_ACCESS_TOKEN
    gh = Github(GH_PERSONAL_ACCESS_TOKEN)

    commit = get_commit(gh, GITHUB_SHA)

    commit.create_status(
        context="FOOBAR",
        description="This call create_status",
        state="failure",
        target_url=GITHUB_RUN_URL,
    )
    print(commit)

    print(GITHUB_SHA)
    print(GITHUB_RUN_URL)
