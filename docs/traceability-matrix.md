| MCP-Fed Feature / Field | Purpose | NIST 800-53 Rev 5 Control(s) |
|-------------------------|---------|------------------------------|
| `audit_log` verb        | Immutable log of agent/tool calls, timestamp, request & response hashes | **AU-2**, **AU-3**, **AU-12**, **SI-11** |
| `signed_response` (JWS) | Cryptographic integrity + non-repudiation of tool output | **AU-10**, **SC-12**, **PE-20** |
| `pii_tag`               | Flags data that contains PII/PHI/FISMA; drives redaction | **AC-19**, **SI-12**, **SC-28** |
| `impact_level`          | Marks IL2–IL6 sensitivity for cross-domain enforcement | **AC-4**, **SC-8**, **SC-51** |
| `tool_perms`            | Least-privilege scope list for each tool action | **AC-2**, **AC-6**, **IA-3** |
| PII/PHI middleware (Presidio) | Runtime detection & masking | **SI-10**, **SC-16** |
| CloudWatch / JSONL audit sinks | Centralized, immutable log storage w/ Object Lock | **AU-9**, **SI-4** |
| ECDSA-P256 signature default | FIPS-approved crypto algorithm | **SC-13**, **SC-17** |

**Appendix A** of the whitepaper will reference this table verbatim to satisfy FedRAMP High traceability requirements.
