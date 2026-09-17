# invoice-cli

Turn a small YAML file of line items into a Markdown invoice. No database, no account, one command.

```bash
pip install -e .
invoice examples/acme-2026-09.yaml
```

```yaml
number: 2026-014
client: Acme Robotics
currency: USD
tax_rate: 0.09
items:
  - description: Backend consulting (hours)
    quantity: 12.5
    unit_price: 120
```

## Development

```bash
pip install -e . pytest
pytest -q
```

Issues are welcome. Bug reports work best in the shape "when X, should Y, actually Z" with a way to reproduce.

## License

MIT
