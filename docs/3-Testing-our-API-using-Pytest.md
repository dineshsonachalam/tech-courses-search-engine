## 3. Testing our API using Pytest

Pytest is a testing framework based on python. It is mainly used to write API based test cases. Here we are going to test our two API's (autocomplete and string-query-search).

**Start Pytest:**
```
dineshsonachalam@macbook tech-courses-search-engine % pytest backend
=========================================== test session starts ===========================================
platform darwin -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/dineshsonachalam/Desktop/tech-courses-search-engine
plugins: cov-2.12.1, metadata-1.11.0
collected 2 items                                                                                         

backend/tests/test_api.py ..                                                                        [100%]

============================================ 2 passed in 0.35s ============================================
dineshsonachalam@macbook tech-courses-search-engine % 
```