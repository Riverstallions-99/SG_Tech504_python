# .gitignore
Why?
- Ignore files we do not want to include in our commit, and/or do not want version controlled

Sensitive Files:
- If at all possible, sensitive info should not exist in your git repo
- If any sensitive info must be included in a git repo (hopefully private one):
  - Needs to be included in .gitignore (others can't access it at all)
  - Control access
- If any credentials must be included + accessed in a git repo (hopefully a private one):
  - Should be encrypted