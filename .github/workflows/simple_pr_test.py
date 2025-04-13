# .github/workflows/pr-test.yml
name: PR Hello World Test

on:
  pull_request:
    branches:
      - main  # or whatever your default branch is

jobs:
  hello-world-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Hello World
        run: echo "Hello, world!"