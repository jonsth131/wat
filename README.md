# wat
Command line application to identify string encodings, hashes and the like

# Usage
`wat.py <string>`

## Examples

`wat eyAi`

```
Checking hashes...Loaded 26 hashes...No match found
Checking encodings...Found 1 match(es)
--------------------------------------------------------------------------------
Base64: { "
--------------------------------------------------------------------------------
```

`wat.py abcdef1234567890`

```
Checking hashes...Loaded 26 hashes...Found 3 match(es)
--------------------------------------------------------------------------------
MySQL323
LM
Half MD5
--------------------------------------------------------------------------------
Checking encodings...No match found
```
