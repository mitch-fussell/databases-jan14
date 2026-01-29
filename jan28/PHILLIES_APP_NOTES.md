# Study Notes: `phillies_app.py` ✅

## Overview 🔎
- File: `jan28/phillies_app.py`
- Purpose: small script that queries a SQLite `baseball.db` to fetch `playerID` values for Phillies (`teamID = 'PHI'`) in year 1976.
- Key function: `fetch_phillies()` — returns a `pandas.DataFrame` of `playerID`s and the script prints the result.

---

## What the code does (step-by-step) 🧭
1. Imports `sqlite3`, `gradio`, and `pandas`.
2. `fetch_phillies()` opens a connection to `baseball.db` using `sqlite3.connect`.
3. Executes a SQL query:

```sql
SELECT playerID
FROM batting
WHERE teamID = 'PHI' AND yearID = 1976
```

4. Fetches all results (`cursor.fetchall()`), closes the connection, converts records into a `pandas.DataFrame`, and returns it.
5. The module prints the DataFrame when run as a script: `print(fetch_phillies())`.

---

## Quick checks / assumptions to confirm ✅
- `baseball.db` exists in the working directory (or provide absolute path).
- `batting` table contains columns `playerID`, `teamID`, and `yearID`.
- `pandas` is available in the environment (it is imported and used).
- `gradio` is imported but not used — decide whether to remove or use it to expose the function.

---

## Improvements & best practices 🔧
- Use a context manager for DB connection to ensure it's closed on exceptions:

```python
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
```

- Parameterize `fetch_phillies()` so it accepts `team` and `year` (or `db_path`) instead of hard-coded values.
- Use parameter substitution to avoid SQL injection (even though this is local):

```python
query = "SELECT playerID FROM batting WHERE teamID = ? AND yearID = ?"
cursor.execute(query, (team, year))
```

- Use proper logging instead of `print()` for library-style modules.
- If the app should be interactive, wire up a `gradio.Interface` that accepts `team` and `year` and displays the DataFrame.
- Add type hints and docstrings:

```python
def fetch_phillies(team: str = 'PHI', year: int = 1976, db_path: str = 'baseball.db') -> pd.DataFrame:
    """Return playerID DataFrame for a given team and year from the specified SQLite DB."""
```

- Add error handling for DB/IO errors and empty results.

---

## Test ideas & exercises 🧪
- Unit test using an in-memory SQLite DB (`sqlite3.connect(':memory:')`) and create a small `batting` table with test rows. Verify returned DataFrame contents.
- Test behavior when DB file is missing (should raise or return empty DataFrame — document desired behavior).
- Add property-based tests for input validation (team codes, year range).

Exercise suggestions:
1. Modify `fetch_phillies()` to accept `team`, `year`, and `db_path` and add a docstring.
2. Replace direct `connect()`/`close()` calls with `with` block and add logging.
3. Create a minimal Gradio app to call the function through a UI and show results.

---

## Suggested next steps 🔜
1. Parameterize function and add docstring + type hints.
2. Add unit tests (create `tests/test_phillies.py`).
3. Decide how and whether to use `gradio` — either implement a simple UI or remove the unused import.

---

## Questions to consider ❓
- Is `baseball.db` created as part of the repo or is it external/large? If external, add instructions in `README.md`.
- Should `fetch_phillies()` be part of a package or kept as a script?
- What are the intended consumers of the function (developer use, demo, or production)?

---

If you want, I can implement any of the suggested changes (parameterize the function, add tests, or add a Gradio UI). 🔁
