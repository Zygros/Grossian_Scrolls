# Repository Quality Standard

## Purpose
This repository follows the Zygros Professional Repository Standard: clear scope, reproducible evidence, explicit implementation status, provenance, security hygiene, and separation of archival material from executable claims.

## Status vocabulary
- **Implemented** — runnable implementation exists and the documented path executes.
- **Prototype** — partial/local/stubbed implementation; not production-hardened.
- **Designed** — architecture/specification exists without sufficient implementation evidence.
- **Historical** — preserved source material; not a statement of current capability.
- **Verified** — independently inspectable evidence supports the stated claim.
- **Unverified** — claim retained pending sufficient evidence.

## Release gate
No repository-level claim should be described as production-ready, independently verified, secure, benchmarked, or otherwise definitive unless the README links to the corresponding reproducible artifact, test, benchmark, or independent verification record.

## Required hygiene
- Keep secrets and credentials out of Git.
- Identify third-party/upstream material clearly.
- Prefer reproducible commands over screenshots or assertions.
- Record material architectural or evidence changes in versioned documentation.
- Keep historical material distinguishable from current implementation.
