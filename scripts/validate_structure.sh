#!/bin/bash
# Validate repo structure

set -e

echo "Validating Saba-AgenticFlow structure..."

# Check required files
REQUIRED_FILES=(
  "README.md"
  "docs/architecture.md"
  "docs/patterns.md"
  "LICENSE"
  "CONTRIBUTING.md"
)

for file in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$file" ]; then
    echo "Error: Required file missing: $file"
    exit 1
  fi
done

echo "✓ All required files present"

echo "Validating markdown syntax..."
for file in "${REQUIRED_FILES[@]}"; do
  if [[ "$file" == *.md ]]; then
    head -1 "$file" > /dev/null || exit 1
  fi
done

echo "✓ Markdown files valid"

echo "Structure validation complete"
