def get_by_name(name):
    if name == "print_neptune_link":
        from mrunner.plugins import neptune_link
        return neptune_link.print_neptune_link

    if name == "ensure_clean_git":
        from mrunner.plugins import git_utils
        return git_utils.ensure_clean_git

    raise RuntimeWarning(
        rf"Plugin {name} not found. Please remove it from the callback list."
    )
