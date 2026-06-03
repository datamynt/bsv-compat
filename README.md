# bsv-compat

Established (non-BRC) open BSV protocols for Python.

The companion to [`bsv-brc`](https://github.com/datamynt/bsv-brc-python):
`bsv-brc` implements the forward-looking, ratified **BRC** standards (BRC-22/24/
52/94/104/105/87 plus the overlay model); `bsv-compat` holds the established,
widely-deployed BSV application protocols that are **not** BRC standards — and
that the ecosystem is gradually moving away from. Keeping them in one place
means they can evolve, and eventually be deprecated, without touching the
canonical BRC library.

Both compose the official [py-sdk](https://github.com/bsv-blockchain/py-sdk)
(`bsv-sdk` on PyPI) — they don't reimplement keys/transactions/SPV.

| Module | Protocol | What |
|--------|----------|------|
| `bsv_compat.bitcom` | B / MAP / AIP / BSM | Bitcoin-Schema `OP_RETURN` builder + parser + authorship |

> **Status note.** These protocols are "compat" for a reason: paymail is being
> de-emphasised by the BSV Association, and the Bitcom/Bitcoin-Schema data model
> is expected to give way to the overlay / BRC-100 approach over time. Use them
> for interop with the existing ecosystem; reach for `bsv-brc` for the path
> forward.

## Install

```bash
pip install bsv-compat
```

## Example — build and parse a Bitcoin-Schema OP_RETURN

```python
from bsv_compat import bitcom

# Build OP_FALSE OP_RETURN with B (data) + MAP (attributes). The "|" section
# separator is emitted as the correct 1-byte pushdata (0x01 0x7c) — a raw 0x7c
# is OP_SWAP and silently breaks every parser that splits on "|".
script = bitcom.op_return(
    bitcom.b_section("hello world", media_type="text/plain"),
    bitcom.map_set({"app": "peck.to", "type": "post"}),
)

parsed = bitcom.parse_script(script)
parsed.map.app          # "peck.to"
parsed.map.fields       # {"app": "peck.to", "type": "post"}

# AIP authorship (the wallet usually signs; verify on read):
ok = bitcom.aip_verify(signed_data, address, signature)
```

## Roadmap

- [x] Bitcom: B / MAP / AIP build + parse; BSM sign/verify/recover
- [ ] paymail (bsvalias discovery, p2p payment destination, PKI) — the next
  large hand-rolled surface to consolidate

## Development

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -v
```

## License

[Open BSV License](LICENSE)
