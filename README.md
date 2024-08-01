# STRCT: Structure Creator Tool 🚀



<p align="center">
  <a href="https://badge.fury.io/py/strct-tool">
    <img src="https://badge.fury.io/py/strct-tool.svg" alt="PyPI version" />
  </a>
  <a href="https://pypi.org/project/strct-tool/">
    <img src="https://img.shields.io/pypi/pyversions/strct-tool.svg" alt="Python Versions" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
  </a>
  <a href="https://github.com/salah-alhajj/strct/actions">
    <img src="https://github.com/salah-alhajj/strct/workflows/Build/badge.svg" alt="Build Status" />
  </a>
  <a href="https://codecov.io/gh/salah-alhajj/strct">
    <img src="https://codecov.io/gh/salah-alhajj/strct/branch/main/graph/badge.svg" alt="codecov" />
  </a>
</p>

STRCT is a powerful and flexible command-line tool designed to streamline your project initialization process. Say goodbye to manual directory creation and hello to consistent, scalable project structures! 🎉

## 🌟 Features

- 🚀 Create project structures from predefined templates
- 🔧 Add custom templates from existing directories
- 🎯 Specify custom destination paths for your projects
- 📋 List and manage available templates
- 🔄 Cross-platform compatibility (Windows, macOS, Linux)

## 🚀 Quick Start

### Installation

You can install STRCT using pip:

```bash
pip install strct-tool
```

### Usage

After installation, you can use STRCT from the command line:

1. Create a new project structure:
   ```
   strct <structure_type> [destination_path]
   ```

2. List available templates:
   ```
   strct list
   ```

3. Add a new template:
   ```
   strct add <template_name> <source_path>
   ```

4. Delete a template:
   ```
   strct delete <template_name>
   ```

5. Get help:
   ```
   strct help
   ```

## 📚 Detailed Usage

### Creating a Project Structure

To create a new project structure, use the following command:

```bash
strct <structure_type> [destination_path]
```

- `<structure_type>`: The name of the template you want to use.
- `[destination_path]`: Optional. The path where you want to create the project. If not specified, the current directory will be used.

Example:
```bash
strct python-flask my_new_project
```

This command will create a new Flask project structure in a directory called `my_new_project`.

### Listing Available Templates

To see all available templates, use:

```bash
strct list
```

This will display a list of all templates you can use to create project structures.

### Adding a New Template

To add a new template based on an existing project structure:

```bash
strct add <template_name> <source_path>
```

- `<template_name>`: The name you want to give to your new template.
- `<source_path>`: The path to the existing project structure you want to use as a template.

Example:
```bash
strct add my-react-template ./existing-react-project
```

### Deleting a Template

To remove a template:

```bash
strct delete <template_name>
```

This will permanently remove the specified template.

## 🛠 How It Works

1. **Template Selection**: Choose from predefined or custom project templates.
2. **Structure Creation**: STRCT generates the directory structure and files based on the selected template.
3. **Customization**: Easily modify the created structure to fit your specific needs.
4. **Reusability**: Save time on future projects by reusing your templates.

## 🤝 Contributing

We welcome contributions from the community! Whether it's bug fixes, new features, or documentation improvements, your help is appreciated. Please see our [Contributing Guide](CONTRIBUTING.md) for more details on how to get started.

## 🐛 Reporting Issues

If you encounter any bugs or have feature requests, please file an issue on our [GitHub Issue Tracker](https://github.com/salah-alhajj/strct/issues). When reporting a bug, please include:

- Your operating system name and version
- Any details about your local setup that might be helpful in troubleshooting
- Detailed steps to reproduce the bug

## 🤔 FAQs

<details>
<summary>Can I use STRCT for any type of project?</summary>
Yes! STRCT is language-agnostic and can be used for any type of project structure.
</details>

<details>
<summary>How do I create custom templates?</summary>
Use the `strct add` command to create a new template from an existing directory structure.
</details>

<details>
<summary>Is STRCT suitable for team use?</summary>
Absolutely! STRCT helps maintain consistency across team projects by using shared templates.
</details>

<details>
<summary>Can I use STRCT in my CI/CD pipeline?</summary>
Yes, STRCT can be easily integrated into CI/CD pipelines to ensure consistent project structures across your builds.
</details>

## 📜 License

STRCT is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgements

- All our contributors and users
- The Python community for their invaluable tools and libraries

## 📬 Contact

For support or queries, please open an issue on our [GitHub repository](https://github.com/salah-alhajj/strct/issues).

---

<p align="center">
  Made with ❤️ by developers, for developers.
</p>