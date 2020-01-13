import os
import sys


def main():
    curr_dir = str(sys.argv[1])
    repo_name = curr_dir.split('\\')[-1]
    print(repo_name)


if __name__ == "__main__":
    main()
