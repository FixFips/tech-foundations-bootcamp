# Tech Foundations Bootcamp

This repo tracks a 5-week plan covering core design patterns, SOLID, DDD, and containers.

## Getting Started (Day 1)

### Python
```bash
# from repo root
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

### Java (Maven)
```bash
# from repo root
mvn -q -f week01-02-patterns/java/pom.xml test
```

### Git
```bash
git init
git add .
git commit -m "chore: bootstrap repo (day 1)"
# create a new GitHub repo, then:
# git remote add origin <YOUR_REPO_URL>
# git branch -M main
# git push -u origin main
```
