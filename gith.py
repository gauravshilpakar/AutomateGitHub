from github import Github
import os

username = "gauravshilpakar"
password = "MHEECHA1lamo"
g = Github(username, password).get_user()


def main():
    curr_dir = os.getcwd()
    repo_name = curr_dir.split('\\')[-1]
    g.create_repo(repo_name)


if __name__ == "__main__":
    main()
