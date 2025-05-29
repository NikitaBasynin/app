# 🛡 Secure Pipeline Demo

Pet-проект для демонстрации базовых практик DevSecOps: автоматического сканирования кода, зависимостей, контейнеров и динамического анализа уязвимостей.  
[![DevSecOps Scan](https://github.com/NikitaBasynin/app/actions/workflows/pipeline.yml/badge.svg)](https://github.com/NikitaBasynin/app/actions)
<p align="left">
    <a href="https://github.com/zricethezav/gitleaks-action">
        <img alt="gitleaks badge" src="https://img.shields.io/badge/protected%20by-gitleaks-blue">
    </a>
</p>  
## 🔧 Что внутри

- Уязвимое Flask-приложение
- CI/CD пайплайн на GitHub Actions
- Интеграция:
  - ✅ Semgrep (SAST)
  - ✅ Trivy (SCA + Docker scan)
  - ✅ OWASP ZAP (DAST)
  - ✅ Gitleaks (Secret scanning)

## 🚀 Как запустить вручную

```bash
# Установи зависимости
pip install -r requirements.txt

# Запусти приложение
python app.py
```

## 🐳 Docker
```bash
docker build -t insecure-app .
docker run -p 5000:5000 insecure-app
```
