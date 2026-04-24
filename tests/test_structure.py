"""
Tests for documentation structure.
"""
import pytest
from pathlib import Path


class TestDocStructure:
    """Verify required documentation files exist."""

    def test_readme_exists(self):
        """README.md should exist."""
        assert Path("README.md").exists(), "README.md not found"

    def test_architecture_docs_exist(self):
        """docs/architecture.md should exist."""
        assert Path("docs/architecture.md").exists(), "docs/architecture.md not found"

    def test_patterns_docs_exist(self):
        """docs/patterns.md should exist."""
        assert Path("docs/patterns.md").exists(), "docs/patterns.md not found"

    def test_ci_workflow_exists(self):
        """.github/workflows/ci.yml should exist."""
        assert Path(".github/workflows/ci.yml").exists(), "CI workflow not found"

    def test_validation_script_exists(self):
        """scripts/validate_structure.sh should exist."""
        assert Path("scripts/validate_structure.sh").exists(), "Validation script not found"

    def test_license_exists(self):
        """LICENSE should exist."""
        assert Path("LICENSE").exists(), "LICENSE not found"
