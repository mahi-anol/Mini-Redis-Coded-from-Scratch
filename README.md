# mini-redis-from-first-principal

# Mini Redis by Mahi

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/mahi-anol/mini-redis-from-first-principal/python-tests.yml)](https://github.com/mahi-anol/mini-redis-from-first-principal/actions)
[![Coverage](https://img.shields.io/badge/coverage-0%25-red)]() <!-- replace with coverage badge if available -->

A **minimal Redis clone implemented from scratch in Python**, supporting the main Redis functionalities such as `SET`, `GET`, `DEL`, `EXPIRE`, lists, and pub/sub. Designed for learning, experimentation, and automated testing.

---

## Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Testing](#testing)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- Core Redis commands:
  - `SET`, `GET`, `DEL`, `EXPIRE`
  - List operations: `LPUSH`, `LPOP`
  - Pub/Sub: `PUBLISH`, `SUBSCRIBE`
- TCP server that can be connected via **telnet** or programmatically
- Automated tests with **pytest**
- Editable installation for development (`pip install -e .`)

---

## Installation

### Clone the repository

```bash
git clone https://github.com/mahi-anol/mini-redis-from-first-principal.git
cd mini-redis-from-first-principal
