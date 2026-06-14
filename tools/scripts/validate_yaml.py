"""
validate_yaml.py

Recursively checks all YAML files in the repository for parse errors and
prints a simple validation report.

Usage:
    python tools/scripts/validate_yaml.py
    python tools/scripts/validate_yaml.py path/to/check
"""

import os
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)


def validate_yaml_files(root_dir: str) -> tuple:
    """
    Recursively find and validate all .yaml and .yml files under root_dir.

    Returns:
        (passed, failed): lists of (path, error_message) tuples
    """
    passed = []
    failed = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories (e.g. .git)
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]

        for filename in filenames:
            if filename.lower().endswith((".yaml", ".yml")):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        yaml.safe_load(f)
                    passed.append(filepath)
                except yaml.YAMLError as exc:
                    failed.append((filepath, str(exc)))

    return passed, failed


def print_report(passed: list, failed: list) -> None:
    """Print a validation summary report."""
    total = len(passed) + len(failed)

    print(f"\nYAML Validation Report")
    print(f"{'=' * 40}")
    print(f"Files checked : {total}")
    print(f"Passed        : {len(passed)}")
    print(f"Failed        : {len(failed)}")
    print()

    if failed:
        print("FAILURES:")
        for filepath, error in failed:
            print(f"  [FAIL] {filepath}")
            print(f"         {error}")
        print()
    else:
        print("All YAML files are valid.")


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    root = os.path.abspath(root)

    print(f"Scanning for YAML files in: {root}")
    passed, failed = validate_yaml_files(root)
    print_report(passed, failed)

    if failed:
        sys.exit(1)
