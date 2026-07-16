# AGENTS

## Scope and role
- Act as an expert in Ansible collection development and Python.
- Optimize for correctness, idempotency, and maintainability.
- Keep changes minimal and focused on the requested behavior.

## Non-negotiable generation rule
- This repository is generator-driven.
- Make functional changes in `scripts/generate_collection.py`.
- Do not hand-edit generated files under `ansible_collections/zeqk/databasus/plugins/modules/`, `ansible_collections/zeqk/databasus/README.md`, or `ansible_collections/zeqk/databasus/galaxy.yml`.
- Regenerate outputs after changing the generator.

## Source of truth
- API schema source: `openapi.json` (Swagger 2.0).
- Generator source: `scripts/generate_collection.py`.
- Docs template for ansible-doc-extractor: `module_doc.md.j2`.

## Expected workflow
1. Edit `scripts/generate_collection.py`.
2. Regenerate collection:
   - `uv run python3 scripts/generate_collection.py --spec openapi.json --output ansible_collections/zeqk/databasus`
3. Regenerate module docs:
   - `uv run ansible-doc-extractor docs $PWD/ansible_collections/zeqk/databasus/plugins/modules/*.py --markdown --template module_doc.md.j2`
4. Run sanity tests:
   - `cd ansible_collections/zeqk/databasus && uv run ansible-test sanity`
5. Run integration tests when behavior changed:
   - `docker compose up -d`
   - `cd ansible_collections/zeqk/databasus && uv run ansible-test integration workspace -v`
   - `docker compose down`

For command details and environment variables, see `README.md`.

## Module conventions to preserve in generator output
- Standard Ansible docs blocks: `DOCUMENTATION`, `EXAMPLES`, `RETURN`.
- Auth inputs: `api_url` and `api_token` (`no_log=True` for token-like fields).
- State handling:
  - Writable resources use `state: present|absent`.
  - Read-only resources avoid state mutation logic.
- HTTP handling uses bearer auth and strict status validation.
- `check_mode` support must remain correct.
- Idempotency must be preserved (detect desired-state equivalence before update).

## Key paths
- Generator: `scripts/generate_collection.py`
- Generated modules: `ansible_collections/zeqk/databasus/plugins/modules/`
- Integration tests: `ansible_collections/zeqk/databasus/tests/integration/`
- Extracted docs: `docs/`
- Collection README generated output: `ansible_collections/zeqk/databasus/README.md`

## Pitfalls
- Direct edits to generated modules will be overwritten on the next generation run.
- If endpoint behavior changes are needed, adjust generator classification/mapping logic, then regenerate and test.
- Keep instruction updates concise: link to existing docs instead of duplicating long explanations.
