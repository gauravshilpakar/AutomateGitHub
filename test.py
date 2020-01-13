import os


def main():
    curr_dir = os.getcwd()
    repo_name = curr_dir.split('\\')[-1]
    print(repo_name)


if __name__ == "__main__":
    main()
