name: repo checks
on:
 push:
 workflow_dispatch:

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
     - name: show version
       run: python3 --version
     - name: list files
       run: ls
  
