from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>CI/CD app</title>
        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                background: linear-gradient(135deg, #ff5fa2, #b86bff);
            }

            .card {
                background: white;
                padding: 40px;
                border-radius: 20px;
                width: 100%;
                max-width: 420px;
                text-align: center;
                box-shadow: 0 20px 50px rgba(0,0,0,0.25);
            }

            h1 {
                margin-top: 0;
                color: #b4005f;
            }

            p {
                color: #555;
                font-size: 18px;
            }

            button {
                margin-top: 25px;
                padding: 12px 24px;
                font-size: 16px;
                border: none;
                border-radius: 999px;
                cursor: pointer;
                background: linear-gradient(135deg, #ff5fa2, #ff86c8);
                color: white;
                font-weight: 600;
                transition: transform 0.15s ease, box-shadow 0.15s ease;
            }

            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(255,95,162,0.5);
            }

            .status {
                margin-top: 20px;
                font-size: 16px;
                font-weight: 600;
            }

            .ok {
                color: #2ecc71;
            }

            .fail {
                color: #e74c3c;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>CI/CD app</h1>
            <p>It works 🎯</p>

            <button onclick="checkHealth()">Check health</button>

            <div id="status" class="status"></div>
        </div>

        <script>
            function checkHealth() {
                const statusEl = document.getElementById("status");
                statusEl.textContent = "Checking...";
                statusEl.className = "status";

                fetch("/cicd/health")
                    .then(res => res.json())
                    .then(data => {
                        statusEl.textContent = "Status: " + data.status;
                        statusEl.classList.add("ok");
                    })
                    .catch(() => {
                        statusEl.textContent = "Health check failed";
                        statusEl.classList.add("fail");
                    });
            }
        </script>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return jsonify(status="ok")
