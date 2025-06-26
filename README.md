# Product Hub 🎩

A Django-based web application to manage and explore products, their sellers, reviews, and authenticity certificates — all powered by Django’s robust ORM and admin panel.

## 🔧 Features

* Custom Django models:

  * `Product` with image support
  * `Seller` (Many-to-Many with products)
  * `Review` (One-to-Many with products)
  * `ProductCertificate` (One-to-One with product)
* Admin panel customization with inline models and horizontal filters
* Dynamic forms using `forms.Form` and `ModelChoiceField`
* Display related sellers based on product selection
* Styled with TailwindCSS

## 📁 Tech Stack

* Python 3.11.2
* Django 5.2.3
* TailwindCSS
* SQLite (default, can be swapped with PostgreSQL/MySQL)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/product-hub.git
cd product-hub
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📷 Screenshots

*(Screenshots of the admin panel, form, and seller list - to be added.)*

---

## 🧑‍💻 Author
Made with ❤️ by [Kshitij Todkar](https://github.com/KshitijTodkar48)
