# bsv-compat

Established (non-BRC) open BSV protocols for Python. Open-source, Open BSV License.
Companion to **bsv-brc** (the ratified BRC standards + overlay). This lib holds
the protocols that are NOT BRC and that the ecosystem is moving away from —
grouped so they can be deprecated together later without touching bsv-brc.

## Scope discipline (why this lib exists)
- **bsv-brc** = ratified BRC (22/24/52/94/104/105/87) + overlay engine/client +
  state_root. Forward-looking, canonical.
- **bsv-compat** (here) = Bitcom (B/MAP/AIP), BSM, and (planned) paymail.
  Established, non-BRC, transitional. paymail is being de-emphasised by BSVA;
  Bitcom/Bitcoin-Schema is expected to yield to overlay/BRC-100.
- Do NOT put BRC code here, and do NOT put peck-infra clients here (those default
  to peck endpoints → a peck-specific lib, not this neutral one).
- Compose py-sdk; never reimplement keys/tx/SPV. BSM rides on `bsv.compat.bsm`.

## Modules
- `bsv_compat.bitcom` — Bitcoin-Schema OP_RETURN: `op_return()`/
  `op_return_parts_to_script()` (pipe separator = 1-byte pushdata 0x01 0x7c, NOT
  raw 0x7c=OP_SWAP), `b_section`/`map_set`, `parse_script` (mirrors
  overlay.peck.to `readMapSection`), `push_data`/`decode_pushdata`, AIP via BSM
  (`bsm_sign`/`bsm_verify`/`bsm_recover_address`, `aip_section`, `aip_verify`).

## Tests
```bash
.venv/bin/python -m pytest -v < /dev/null   # or reuse bsv-brc's .venv2 with PYTHONPATH=src
```

## History
Extracted from bsv-brc 2026-06-03 (bitcom was unreleased there) to keep bsv-brc
strictly BRC. See bsv-brc-python for the BRC/overlay side.
