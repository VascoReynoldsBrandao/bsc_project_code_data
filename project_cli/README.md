# Project CLI

This guide will help you set up a Python virtual environment, install dependencies, and install the CLI tool.

## 1. Setup Virtual Environment

```bash
python3 -m venv venv
```

## 2. Activate Virtual Environment

- **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```
- **Windows:**
    ```bash
    venv\Scripts\activate
    ```

## 3. Deactivate Virtual Environment

```bash
deactivate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Install CLI

```bash
pip install .
```

Now you can use the CLI tool as described in the documentation.