
# All For One

All programs for one execution

### Path Configuration

An `ALL_FOR_ONE_PATH` must be set for the running shell.

```.bashrc
export ALL_FOR_ONE_PATH=~/.config/all-for-one-config.yml
```

### Program Configuration

```programs.yml
rootPath: ~/code
programs:
  ls:
    runtime: /bin/bash
    path: ls
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
