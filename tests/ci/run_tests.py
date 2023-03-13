import os

# GITHUB_WORKSPACE /home/runner/work/github-action/github-action
# GITHUB_PATH /home/runner/work/_temp/_runner_file_commands/add_path_b78782f7-3b47-4fc0-a261-5dfe7304fb3f
# GITHUB_ACTION __run
# GITHUB_RUN_NUMBER 4
# RUNNER_NAME Hosted Agent
# GITHUB_REPOSITORY_OWNER_ID 15108950
# GITHUB_TRIGGERING_ACTOR qijun-niu-timeplus
# GITHUB_REF_TYPE branch
# PWD /home/runner/work/github-action/github-action/tests/ci
# GITHUB_REPOSITORY_ID 613345723
# GITHUB_ACTIONS true
# GITHUB_SHA ee6541939c231247790b4836802813e5e20b0119
# GITHUB_WORKFLOW_REF mrssss/github-action/.github/workflows/pull_request.yml@refs/heads/main
# GITHUB_REF refs/heads/main
# GITHUB_REF_PROTECTED false
# GITHUB_API_URL https://api.github.com
# GITHUB_STATE /home/runner/work/_temp/_runner_file_commands/save_state_b78782f7-3b47-4fc0-a261-5dfe7304fb3f
# GITHUB_ENV /home/runner/work/_temp/_runner_file_commands/set_env_b78782f7-3b47-4fc0-a261-5dfe7304fb3f
# GITHUB_EVENT_PATH /home/runner/work/_temp/_github_workflow/event.json
# GITHUB_EVENT_NAME push
# GITHUB_RUN_ID 4404753182
# GITHUB_STEP_SUMMARY /home/runner/work/_temp/_runner_file_commands/step_summary_b78782f7-3b47-4fc0-a261-5dfe7304fb3f
# GITHUB_ACTOR qijun-niu-timeplus
# GITHUB_RUN_ATTEMPT 1
# GITHUB_GRAPHQL_URL https://api.github.com/graphql
# GITHUB_ACTOR_ID 93511697
# GITHUB_WORKFLOW_SHA ee6541939c231247790b4836802813e5e20b0119
# GITHUB_REF_NAME main
# GITHUB_JOB build
# GITHUB_REPOSITORY mrssss/github-action
# GITHUB_RETENTION_DAYS 90
# GITHUB_ACTION_REPOSITORY
# GITHUB_BASE_REF
# GHCUP_INSTALL_BASE_PREFIX /usr/local
# CI true
# GITHUB_REPOSITORY_OWNER mrssss
# GITHUB_HEAD_REF
# GITHUB_ACTION_REF
# GITHUB_WORKFLOW CI
# DEBIAN_FRONTEND noninteractive
# GITHUB_OUTPUT /home/runner/work/_temp/_runner_file_commands/set_output_b78782f7-3b47-4fc0-a261-5dfe7304fb3f

if __name__ == '__main__':
    for (k, v) in os.environ.items():
        print(k, v)
