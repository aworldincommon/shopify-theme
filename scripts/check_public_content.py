#!/usr/bin/env python3
"""Fail closed when likely private information appears in public theme files.

This scanner is intentionally local and deterministic. It reports file and line,
not the matched value, so a failure message does not repeat the sensitive data.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / ".privacy-allowlist"

PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("email address", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
    ("phone number", re.compile(r"(?i)\b(?:phone|telephone|tel\.?|mobile|whatsapp|telefone|telemóvel|telemovel)\s*[:#-]?\s*\+?\d[\d () .-]{6,}\d\b")),
    ("address with street number", re.compile(r"(?i)\b(?:address|morada|rua|street|avenue|avenida|av\.)\b[^\n]{0,100}\b\d{1,5}\b")),
    ("Portuguese NIF", re.compile(r"(?i)\b(?:nif|tax\s*id)\s*[:#-]?\s*\d{9}\b")),
    ("IBAN or bank identifier", re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b")),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("Shopify token", re.compile(r"\b(?:shpat|shpua|shpca|shppa)_[A-Za-z0-9_-]{20,}\b")),
    ("common API token", re.compile(r"\b(?:ghp|github_pat|sk_live|sk_test|xox[baprs])[-_][A-Za-z0-9_-]{12,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private network address", re.compile(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3})\b")),
)


def tracked_files() -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z"],
            check=True,
            capture_output=True,
        )
        names = [item for item in result.stdout.decode().split("\0") if item]
        return [ROOT / name for name in names]
    except (OSError, subprocess.CalledProcessError):
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def load_allowlist() -> list[re.Pattern[str]]:
    if not ALLOWLIST.exists():
        return []
    patterns = []
    for raw in ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            patterns.append(re.compile(line))
    return patterns


def is_binary(path: Path) -> bool:
    try:
        sample = path.read_bytes()[:8192]
    except OSError:
        return True
    return b"\0" in sample


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true", help="only return a status")
    args = parser.parse_args()

    allowlist = load_allowlist()
    findings: list[tuple[Path, int, str]] = []

    for path in tracked_files():
        if not path.exists() or is_binary(path):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(lines, 1):
            for kind, pattern in PATTERNS:
                match = pattern.search(line)
                if not match:
                    continue
                value = match.group(0)
                if any(allowed.search(value) for allowed in allowlist):
                    continue
                findings.append((path.relative_to(ROOT), line_number, kind))

    if findings:
        if not args.quiet:
            print("PUBLIC CONTENT CHECK FAILED")
            print("Likely private information was found. No matched values are printed.")
            for path, line_number, kind in findings:
                print(f"- {path}:{line_number}: {kind}")
            print("Review the file, remove the private value, or add an explicitly approved local pattern to .privacy-allowlist.")
        return 1

    if not args.quiet:
        print("PUBLIC CONTENT CHECK PASSED: no likely PII or credentials found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
