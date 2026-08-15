#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = ["README.md", "SECURITY.md", "CONTRIBUTING.md", "LICENSE-STATUS.md", "DEPENDENCY-STATUS.md", "SPLUS.md", "docs/PROVENANCE.md", ".gitignore"]
checks = {"required_files": {p: (ROOT / p).exists() for p in required}}
checks["readme_has_sections"] = all(token in (ROOT / "README.md").read_text(encoding="utf-8", errors="replace").lower() for token in ("install", "usage"))
checks["no_tracked_env_files"] = not any(p.name in {".env", ".env.local", ".env.production"} for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts)
result = {"passed": all(checks["required_files"].values()) and checks["readme_has_sections"] and checks["no_tracked_env_files"], "checks": checks}
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
