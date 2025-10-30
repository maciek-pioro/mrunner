try:
    import git
except ImportError:
    print("Please install GitPython")
    exit()


def ensure_clean_git(path=None, warning_only=False, **other_kwargs):
    repo = git.Repo(search_parent_directories=True) if path is None else git.Repo(path)
    if repo.is_dirty():
        print("\nGit repository is not clean!\n")
        if not warning_only:
            print("Exiting...")
            exit()
