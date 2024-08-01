# STRCT: Structure Creator Tool 🚀

<p align="center">
  <a href="https://badge.fury.io/py/strct">
    <img src="https://badge.fury.io/py/strct.svg" alt="PyPI version" />
  </a>
  <a href="https://pypi.org/project/strct/">
    <img src="https://img.shields.io/pypi/pyversions/strct.svg" alt="Python Versions" />
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

Supercharge your project initialization with the power of STRCT! 🐍💨

## 🌟 Features

- 🚀 Automatically create project structures from predefined templates
- 📁 Add custom templates from existing directories
- 🎯 Specify custom destination paths for your projects
- 📋 List and manage available templates
- 🔧 Cross-platform compatibility (Windows, macOS, Linux)

## 🚀 Quick Start

### Installation

```bash
pip install strct
```

### Usage

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

## 🛠 How It Works

1. **Template Selection**: Choose from predefined or custom project templates.
2. **Structure Creation**: STRCT generates the directory structure and files based on the selected template.
3. **Customization**: Easily modify the created structure to fit your specific needs.
4. **Reusability**: Save time on future projects by reusing your templates.

## 🔧 Configuration

The `settings.yaml` file in your project root controls the STRCT behavior:

```yaml
templates:
  path: '~/.strct/templates'

exclude:
  files:
    - '.DS_Store'
    - 'Thumbs.db'
  dirs:
    - '.git'
    - '__pycache__'

# ... (other settings)
```

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

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

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