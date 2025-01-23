# Repository-Link

## Overview

This Python script fetches GitHub repositories and generates a Mermaid graph visualization.

## Prerequisites

- Python 3.7+
- `requests` library
- google-generativeai library
- Custom LLM module wrapping Gemini Google Generative AI module.

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install requests google-generativeai
   ```

## Usage

Run the script:
```bash
python main.py
```

1. Enter GitHub username when prompted
2. Script will fetch repositories
3. Generate Mermaid graph code
4. Paste the generated code in README.md

## Configuration

Modify script parameters:
- Adjust `per_page` for repository fetch limit
- Customize LLM prompt in `main()` function
