# Step13 – Resume App with i18n and Dynamic Settings

This step introduces **internationalization (i18n)** support with dynamic language switching and a visual settings page for customizing the resume's CSS.

## 🔧 Features Implemented

### ✅ 1. i18n Setup
- Integrated Flask-Babel with support for:
  - `ar` (Arabic)
  - `en` (English)
  - `de` (German)
- Language detection based on `?lang=` query param or default fallback (`ar`).
- Custom `get_locale()` function using `request.args.get("lang")`.

### ✅ 2. Translations
- All template text wrapped with `_()` or `gettext`.
- `.po` and `.mo` files generated inside:
  ```
  step13/translations/ar/LC_MESSAGES/messages.po
  step13/translations/en/LC_MESSAGES/messages.po
  step13/translations/de/LC_MESSAGES/messages.po
  ```

### ✅ 3. Dynamic CSS Settings Page (`/admin/settings`)
- Admin can visually update:
  - Section title font size, color, weight
  - Paragraph font size, color
  - Additional settings (textarea per key)
- Live Preview box updates on-the-fly using JavaScript.
- Settings stored in database (`Setting` table).
- Two buttons:
  - **Save Changes**
  - **Save & Show Preview** → redirects to `/resume`

### ✅ 4. Initial DB Seeding
- On first run: auto-creates `lebenslauf.db` and inserts default sections (Summary, Objective, Skills…).

## 🗂 Project Structure Highlights

```
step13/
├── templates/
│   ├── admin/
│   │   └── settings.html.j2
├── routes/
│   ├── admin_routes.py
│   ├── public_routes.py
│   └── main_routes.py
├── models/
│   └── models.py  # Section, Setting
├── i18n_runtime.py  # get_locale() + init_i18n()
├── extensions.py  # babel instance
├── __init__.py  # create_app()
├── translations/
│   └── ar, en, de
```

## 🌍 Language Switching

- Add `?lang=ar`, `?lang=en`, or `?lang=de` to any URL:
  ```
  http://localhost:5000/resume?lang=ar
  ```

## 🧩 Next Step (step14)

- Replace query string language control with `session`-based language memory.

---

✅ **Status**: Completed and tested

🧪 Tip: Use `pybabel compile` to regenerate `.mo` files after editing translations.