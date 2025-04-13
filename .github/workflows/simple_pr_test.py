name: PR Hello World Test

on:
  pull_request:
    branches:
      - main

jobs:
  hello-world-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Check for non-docs changes
        id: check_changes
        run: |
          CHANGED_FILES=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
          echo "Changed files:"
          echo "$CHANGED_FILES"

          NON_DOCS_CHANGED=$(echo "$CHANGED_FILES" | grep -vE '^docs/' || true)

          if [[ -z "$NON_DOCS_CHANGED" ]]; then
            echo "only_docs=true" >> "$GITHUB_OUTPUT"
          else
            echo "only_docs=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Run Hello World
        if: steps.check_changes.outputs.only_docs == 'false'
        run: echo "Hello, world! Running tests..."

      - name: Skip Message
        if: steps.check_changes.outputs.only_docs == 'true'
        run: echo "Skipping tests since only docs/ were changed."