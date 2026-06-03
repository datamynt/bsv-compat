# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-06-03

### Added
- Initial release, extracted from `bsv-brc` to keep that library strictly
  scoped to ratified BRC standards.
- `bsv_compat.bitcom` — Bitcoin-Schema `OP_RETURN`: `op_return()` /
  `op_return_parts_to_script()` builders (the `|` section separator emitted as
  the correct 1-byte pushdata `0x01 0x7c`, fixing the raw-`0x7c` / `OP_SWAP`
  bug), `b_section` / `map_set`, `parse_script` (mirrors overlay.peck.to's
  `readMapSection`), `push_data` / `decode_pushdata`, and AIP authorship over
  BSM (`bsm_sign` / `bsm_verify` / `bsm_recover_address`, `aip_section`,
  `aip_verify`). Composes `bsv-sdk`'s `bsv.compat.bsm`.
