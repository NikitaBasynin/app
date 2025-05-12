# 🛡 Secure Pipeline Demo

Pet-проект для демонстрации базовых практик DevSecOps: автоматического сканирования кода, зависимостей, контейнеров и динамического анализа уязвимостей.  
[![DevSecOps Scan](https://github.com/NikitaBasynin/app/actions/workflows/pipeline.yml/badge.svg)](https://github.com/NikitaBasynin/app/actions)

## 🔧 Что внутри

- Уязвимое Flask-приложение
- CI/CD пайплайн на GitHub Actions
- Интеграция:
  - ✅ Semgrep (SAST)
  - ✅ Trivy (SCA + Docker scan)
  - ✅ OWASP ZAP (DAST)

## 🚀 Как запустить вручную

```bash
# Установи зависимости
pip install -r requirements.txt

# Запусти приложение
python app.py


## 🐳 Docker
```bash
docker build -t insecure-app .
docker run -p 5000:5000 insecure-app
