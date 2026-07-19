# Security Policy

## Reporting
Report vulnerabilities privately to the repository owner through GitHub security advisories. Do not open a public issue for secrets, remote-code execution, model deserialization vulnerabilities, or exposed health information.

## Safe model loading
Only load checkpoints from trusted sources. PyTorch pickle-based checkpoints may execute code. Prefer `state_dict` files and verify checksums.

## Supported version
Version 1.x receives security fixes.
