# Prisma Cloud Code Security Custom Policies

A repository to store custom policy examples that do not belong as out-of-the-box policies for Code Security.

You can learn more about writing custom policies here: https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html

Also, leverage out-of-the-box policies from Checkov.


# Using Custom Policies with Checkov

This guide explains how to use custom policies with Checkov by incorporating them from external repositories. You can utilize custom policies either from the command line or using the pre-commit utility.  

## Using Custom Policies from the Command Line

To download a Git repository containing custom checks, use the following command:

```bash
checkov -d . --external-checks-git git@github.com:PaloAltoNetworks/pccs-custom-policies.git
```

### Work with subdirectory

If you only want to download a specific subdirectory from a GitHub repository, you can specify the subdirectory after a double-slash `//`.

```bash
checkov -d . --external-checks-git git@github.com:PaloAltoNetworks/pccs-custom-policies.git//python
```

## Using Custom Policies with the Pre-Commit Utility

### Installing Pre-Commit

You can install the pre-commit utility using pip. It is recommended to install it within a virtual environment to avoid conflicts with other packages.  
To install it in a virtual environment, follow these steps:

```bash
python3 -m venv pre-commit-env
source pre-commit-env/bin/activate
pip install pre-commit
```

### Creating a Pre-Commit Configuration File

To set up pre-commit for a project, create a `.pre-commit-config.yaml` file in the root of your project directory. An example configuration file for Checkov might look like this:

```yaml
repos:
- repo: https://github.com/bridgecrewio/checkov.git
  rev: '2.3.176' # Checkov Version
  hooks:
  - id: checkov
    args: ['--external-checks-git', 'git@github.com:PaloAltoNetworks/pccs-custom-policies.git//python', '--soft-fail']
```

### Installing Git Hooks
After creating the configuration file, run the following command to install the Git hooks:

```bash 
pre-commit install
```

Now, `pre-commit` will run the specified hooks every time you try to commit changes to your repository.