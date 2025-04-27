# .gitignore
Why?
- Ignore files we do not want to include in our commit, and/or do not want version controlled

Sensitive Files:
- If at all possible, sensitive info should not exist in your git repo
- If any sensitive info must be included in a git repo (hopefully private one):
  - Needs to be included in .gitignore (others can't access it at all)
  - Control access to repo very carefully
- If any credentials must be included + accessed in a git repo (hopefully a private one):
  - Should be encrypted

If file/folder has already been staged, commited then we add to .gitignore:
- need to run command git rm --cached <file/folder>
Otherwise:
- should no longer exist as part of version control

If something like credentials are pushed to a public repo (our own), quickest way to address:
1. remove the GitHub or remote repo
2. disable/remove credentials wherever it was used (eg. AWS)
3. then we have time locally to decide to either:
   - git reset (to keep some commit history)
   - delete .git (will lose all commit history)