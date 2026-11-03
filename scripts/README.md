# Scripts APP-MOODLE

| Script | Função |
|--------|--------|
| `baixar-jsdoc.py` | Baixa **todas** as versões do [JSDoc Moodle](https://jsdoc.moodledev.io/) → `../jsdoc/` (módulos + `*_amd_src_*.js`) |
| `limpar-devdocs.py` | Limpa clone `../devdocs/` (só MD 4.5–5.2) |

```bash
./scripts/baixar-jsdoc.py --list
./scripts/baixar-jsdoc.py              # todas as branches do site
./scripts/limpar-devdocs.py --clone
```
