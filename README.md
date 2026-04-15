# 🎵 Music Recommendation System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 Description

The **Music Recommendation System** is a web-based application built with Django and machine learning to provide personalized song recommendations.

It uses **content-based filtering** and **cosine similarity** to analyze song features and suggest tracks that match user preferences. The application integrates external APIs and offers a clean, responsive interface.

---

## 🚀 Features

* 🔍 Search for songs and artists
* 🎧 Personalized recommendations
* 🤖 Content-based filtering (Cosine Similarity)
* 🌐 Responsive UI
* ⚡ Fast API integration
* 🎶 Real-time results

---

## 📚 Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Dependencies](#dependencies)
* [Testing](#testing)
* [Contributing](#contributing)
* [License](#license)

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/aaryanadithya/music-recommendation-system.git
cd music-recommendation-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run Server

```bash
python manage.py runserver
```

### 7. Open in Browser

```
http://127.0.0.1:8000/
```

---

## ▶️ Usage

1. Start the server
2. Open the application in your browser
3. Search for a song or artist
4. View recommended songs

---

## ⚙️ Configuration

* Python 3.10+ required
* Update API keys if needed
* Modify `settings.py` for custom configuration

---

## 📦 Dependencies

* Python 3.10+
* Django 4.x
* scikit-learn
* pandas

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧪 Testing

```bash
python manage.py test
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch

```bash
git checkout -b feature/your-feature-name
```

3. Commit changes

```bash
git commit -m "Add feature"
```

4. Push

```bash
git push origin feature/your-feature-name
```

5. Open Pull Request

---

## 📄 License

MIT License
