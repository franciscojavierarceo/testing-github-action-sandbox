import shutil

def main():
    if shutil.which("git"):
        use_scm_version = {"root": ".", "relative_to": __file__, "tag_regex": TAG_REGEX}
    else:
        use_scm_version = None
    
    print('it worked')

if __name__ == "__main__":
    main()
