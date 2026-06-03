"""
bsv-compat — established (non-BRC) open BSV protocols for Python.

The companion to ``bsv-brc``: where ``bsv-brc`` implements the
forward-looking ratified BRC standards (BRC-22/24/52/94/104/105/87 +
the overlay model), ``bsv-compat`` holds the established, widely-deployed
BSV application protocols that are *not* BRC standards and that the
ecosystem is gradually moving away from — kept together so they can
evolve, and eventually be deprecated, without touching the canonical
BRC library.

Modules:
    bitcom — Bitcoin-Schema OP_RETURN: B (data) + MAP (Magic Attribute
             Protocol) + AIP (Author Identity Protocol), plus the BSM
             (Bitcoin Signed Message) primitives AIP rides on.

Composes the official ``bsv-sdk`` (py-sdk). License: Open BSV.
"""

from bsv_compat import bitcom

__version__ = "0.1.0"

__all__ = ["__version__", "bitcom"]
