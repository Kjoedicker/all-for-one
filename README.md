
# All For One

All programs for one execution

### Configuration

```programs.yml
rootPath: ~/code
programs:
  programA:
    runtime: go run
    path: /programA
  programB:
    runtime: node
    path: /programB/server.js
  programC:
    runtime: /bin/bash
    path: /programC
  programD:
    runtime: python3
    path: /programD
```
### Usage

```
kjnix@arch all-for-one % python3 all-for-one.py ls
README.md       all-for-one
```

## Help