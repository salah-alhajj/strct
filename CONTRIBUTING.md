# Contributing to STRCT

First off, thank you for considering contributing to STRCT! 🎉 It's people like you that make STRCT such a great tool.

## 📜 Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please take a moment to read it before proceeding.

## 🤝 How Can I Contribute?

### Reporting Bugs 🐛

This section guides you through submitting a bug report for STRCT. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

- Use a clear and descriptive title for the issue to identify the problem.
- Describe the exact steps which reproduce the problem in as many details as possible.
- Provide specific examples to demonstrate the steps.
- Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.
- Explain which behavior you expected to see instead and why.
- Include screenshots and animated GIFs which show you following the described steps and clearly demonstrate the problem.
- If the problem wasn't triggered by a specific action, describe what you were doing before the problem happened.

### Suggesting Enhancements 💡

This section guides you through submitting an enhancement suggestion for STRCT, including completely new features and minor improvements to existing functionality.

- Use a clear and descriptive title for the issue to identify the suggestion.
- Provide a step-by-step description of the suggested enhancement in as many details as possible.
- Provide specific examples to demonstrate the steps or point out the part of STRCT which the suggestion is related to.
- Describe the current behavior and explain which behavior you expected to see instead and why.
- Explain why this enhancement would be useful to most STRCT users.
- List some other project structure tools where this enhancement exists, if applicable.

### Your First Code Contribution 🚀

Unsure where to begin contributing to STRCT? You can start by looking through these `beginner` and `help-wanted` issues:

- Beginner issues - issues which should only require a few lines of code, and a test or two.
- Help wanted issues - issues which should be a bit more involved than `beginner` issues.

### Pull Requests 🔧

- Fill in the required template
- Do not include issue numbers in the PR title
- Include screenshots and animated GIFs in your pull request whenever possible.
- Follow the [Python](https://www.python.org/dev/peps/pep-0008/) style guide.
- Include thoughtfully-worded, well-structured [Pytest](https://docs.pytest.org/) tests in the `./tests` folder. Run them using `pytest`.
- Document new code based on the [Documentation Styleguide](#documentation-styleguide)
- End all files with a newline

## Styleguides

### Git Commit Messages 📝

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- Consider starting the commit message with an applicable emoji:
    - 🎨 `:art:` when improving the format/structure of the code
    - 🐎 `:racehorse:` when improving performance
    - 📝 `:memo:` when writing docs
    - 🐛 `:bug:` when fixing a bug
    - 🔥 `:fire:` when removing code or files
    - 💚 `:green_heart:` when fixing the CI build
    - ✅ `:white_check_mark:` when adding tests
    - 🔒 `:lock:` when dealing with security
    - ⬆️ `:arrow_up:` when upgrading dependencies
    - ⬇️ `:arrow_down:` when downgrading dependencies

### Python Styleguide 📐

All Python code is linted with [Flake8](https://flake8.pycqa.org/) and formatted with [Black](https://black.readthedocs.io/).

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Use type hints for function arguments and return values.
- Use docstrings for functions and classes.
- Prefer list comprehensions over `filter()` and `map()` when appropriate.

### Documentation Styleguide 📚

- Use [Markdown](https://daringfireball.net/projects/markdown/) for documentation.
- Reference functions and classes appropriately.
- Provide examples in documentation when applicable.

## Additional Notes

### Issue and Pull Request Labels 🏷️

This section lists the labels we use to help us track and manage issues and pull requests.

- `beginner` - Less complex issues which would be good first issues to work on for users who want to contribute to STRCT.
- `help-wanted` - Issues we need or would love help from the community to resolve.
- `bug` - Confirmed bugs or reports that are very likely to be bugs.
- `enhancement` - Feature requests.
- `performance` - Related to performance improvements.
- `documentation` - Related to any type of documentation.

Thank you for contributing to STRCT! 🙏