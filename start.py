import os
from src.github_library import GH_Library
from src.github_analysis import GraphAnalysis


def main():
    gh_lib=GH_Library(os.getcwd())
    gh_lib.get_library()
    gh_analyse=GraphAnalysis(gh_lib)
    gh_analyse.analyze()

if __name__ == "__main__":
    main()