# dpreader

Dump contents of Tascam DP-006 backup files

## Set up, type-check and install

```bash
python -m pip install --upgrade pip
python -m pip install .[dev]
mypy --install-types --non-interactive
mypy dpreader.py dpreader
isopy wrap dpreader .\dpreader.py .
```

## Licence

[MIT License](LICENSE)
