## Development

Use the generator script to rebuild the Ansible collection from the OpenAPI/Swagger spec.

### Generate Collection

Run the command below from the repository root:

```bash
python3 scripts/generate_collection.py --spec openapi.json --output zeqk/databasus
```

What this command does:

- Reads the API spec from `openapi.json`.
- Regenerates `galaxy.yml`, module files, and the collection README.
- Writes output into `zeqk/databasus`.

### Notes

- Re-run this command every time `openapi.json` changes.
- Generated files are overwritten to keep the collection in sync with the API spec.
