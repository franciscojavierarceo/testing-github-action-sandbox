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
    else:
        use_scm_version = None
        print('boo shutil no worked')


if __name__ == "__main__":
    main()
