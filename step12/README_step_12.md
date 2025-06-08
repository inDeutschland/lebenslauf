
# ✅ Step 12 – Unifying Page Design Using a Base Template

In this step, we implemented a unified design across all project pages by creating:

---

## 📁 Added Files:

- `base.html.j2`: The main base template for all pages.
- `partials/navbar.html.j2`: A unified top navigation bar.
- `partials/footer.html.j2`: A unified footer.

---

## 🧩 Implemented Features:

| Feature                     | Status |
|----------------------------|--------|
| Unified Navbar             | ✅     |
| Unified Footer             | ✅     |
| `.j2` extension for templates | ✅     |
| `home.html.j2` inherits from `base.html.j2` | ✅ |
| Fixed `TemplateNotFound` errors | ✅ |

---

## 🚀 Recommended Way to Run the Server:

```bash
# From the project root directory:
python -m step12.run
```

> Make sure `run.py` contains:
```python
from step12 import create_app
```

---

## ⚠️ Important Note:

If you see the message:
```
sqlalchemy.exc.OperationalError: no such table: section
```

📌 It means the database tables have not been created yet.  
In the next step `step13`, automatic table creation will be implemented inside `create_app()`.

---
