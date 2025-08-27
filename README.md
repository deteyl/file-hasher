# File Hasher Tool

A command-line interface (CLI) tool built with Python for calculating file checksums/hashes. Essential for digital forensics, verifying file integrity, and comparing files.

## Features

*   **Multiple Algorithms:** Supports all hashing algorithms available in your Python environment (MD5, SHA1, SHA256, SHA512, etc.).
*   **User-Friendly CLI:** Easy-to-use commands with helpful prompts and error messages.
*   **Flexible Output:** Option to output only the raw hash for use in scripts and automation.
*   **Cross-Platform:** Works on Windows, macOS, and Linux.

## Supported Algorithms

This tool uses Python's `hashlib`, so it supports all algorithms available on your system (e.g., `md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `blake2b`, `blake2s`, `sha3_224`, `sha3_256`, `sha3_384`, `sha3_512`). To see the full list for your environment, use the `list-algorithms` command.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/deteyl/file-hasher.git
    cd file-hasher
    ```

2.  **(Recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The tool provides two main commands: `calculate-hash` and `list-algorithms`.

### Calculate a File Hash

Use the `calculate-hash` command to compute the hash of a file.

**Basic Syntax:**
```bash
python hasher.py calculate-hash --file <path-to-file> [--algorithm <algorithm-name>] [--quiet]
