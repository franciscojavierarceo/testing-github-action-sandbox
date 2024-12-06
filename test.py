from setuptools_scm import get_version

# Retrieve and print the SCM version



import re
import shutil

TAG_REGEX = re.compile(
    r"^(?:[\/\w-]+)?(?P<version>[vV]?\d+(?:\.\d+){0,2}[^\+]*)(?:\+.*)?$"
)

def main():
    if shutil.which("git"):
        use_scm_version = {"root": ".", "relative_to": __file__, "tag_regex": TAG_REGEX}
        print('yay shutil worked')
        print(f"use scm version = {use_scm_version}")
        scm_version = get_version(root='.', relative_to=__file__, tag_regex=TAG_REGEX)
        print(f"SCM Version: {scm_version}")

    else:
        use_scm_version = None
        print('boo shutil no worked')


if __name__ == "__main__":
    main()
