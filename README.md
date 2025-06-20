## ⚙️ Ejecución local

```bash
git clone https://github.com/Thrumanshow/HormigasAIS-video-intelligence-checker.git
cd HormigasAIS-video-intelligence-checker

# Ejecutar backend
cd backend
pip install -r requirements.txt
uvicorn api.api:app --reload
