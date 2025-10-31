# Task & Time Tracker (FastAPI + SQLite)

4日で作成した個人ポートフォリオ用の簡易Webアプリです。  
デスクトップ開発からWeb開発へのスキル拡張を目的に、REST/API・DB・テンプレートを最小構成で実装しています。

## 技術スタック
- Python 3.14 / FastAPI / Uvicorn
- SQLAlchemy (Async) / SQLite（後日 PostgreSQL 切替）
- Jinja2（最小UI）
- Alembic（後日導入）

## 起動方法
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
