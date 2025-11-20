# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import threading
app = FastAPI()

# -------------------------------
# Função para iniciar o Streamlit
# -------------------------------
#def run_streamlit():
#    subprocess.run(
#        ["streamlit", "run", "dashboard.py", "--server.port=8501"]
#    )

# Iniciar Streamlit em segundo plano
#threading.Thread(target=run_streamlit, daemon=True).start()

@app.get("/")
def read_root():
    return {"message": "Look Ma, I'm deployed!"}

@app.get("/hello")
def hello():
    return {"message": "Olá! API FastAPI funcionando 🎉"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}


@app.get("/dashboard", response_class=HTMLResponse)
def embedded_dashboard():
    html = """
    <iframe src="http://localhost:8501"
            style="width:100%; height:100vh; border:none;">
    </iframe>
    """
    return html



# Importante pra poder funcionar na porta principal do Vercel 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)