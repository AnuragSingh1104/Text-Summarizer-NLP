import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    long_description=f.read()

    __version__="0.0.0"

    REPO_NAME="Text-Summarizer-NLP"
    AUTHOR_USER_NAME="Anurag Singh"
    SRC_REPO="textSummarizer"


    setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        description="A small python package for NLP app",
        long_description="long_description",
        long_description_content_type="text/markdown",
        url=f"https://github.com/AnuragSingh1104/Text-Summarizer-NLP",
        project_urls={
            "Bug Tracker": f'https://github.com/AnuragSingh1104/Text-Summarizer-NLP/issues',
        },
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
    )