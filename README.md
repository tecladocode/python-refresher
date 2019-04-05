# Course template

## Set up project

Make sure you have Python3.7 installed.

Then, in a terminal, run:

```
pipenv install
```

### Set up Git Hooks

We have a Git hook config that will run Black formatter on all modified files **before you commit**—that's in case you forget to do so yourself or don't have your IDE set up to format on save (which you should, Black is unintrusive!).

To set up the Git hook:

```
pipenv shell
pre-commit install
```

The first time you commit it may take a little longer than you'd hope, but subsequent commits will be quicker.

> Commits will **fail** if any files are formatted, but the files will still be formatted. This is so you are aware of the reformat and also so we don't accidentally reformat something we don't want to reformat.

If you want to run the commit without running the hook, do `git commit --no-verify`. This is highly discouraged, we should be aiming for consistent code, and using a formatter really helps us achieve that!

## allow_prereleases

The Pipfile has `allow_prereleases = "true"` because for Black this is required. Make sure when installing libraries that the latest stable version is used, but try to avoid using alpha and beta versions where possible.

There are times where it will be unavoidable to use prerelease versions of libraries used in a course to teach actual content. We should discuss them on an individual basis. The reason for this is that if we cover an alpha version of a library, it's likely it will change by the time the course is released.

## Creating course documentation

Internal course documentation (for recording purposes) should go in Notion ((https://www.notion.so/teclado/Course-Wikis-fdd4b72cb5f74e1a9d7172f03e5c24cd)[https://www.notion.so/teclado/Course-Wikis-fdd4b72cb5f74e1a9d7172f03e5c24cd]).

If there is documentation or files that students would benefit from having, they should be included in this repository alongside the code.
