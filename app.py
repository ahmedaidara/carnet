from flask import Flask, request

app = Flask(__name__)

# PAGE ACCUEIL
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Mon Site Python</title>
            <style>
                body {
                    background-color: #111;
                    color: white;
                    text-align: center;
                    font-family: Arial;
                }
                h1 {
                    color: cyan;
                }
                a {
                    color: orange;
                    text-decoration: none;
                    font-size: 20px;
                }
                .box {
                    margin-top: 50px;
                }
                input {
                    padding: 10px;
                    font-size: 16px;
                }
                button {
                    padding: 10px;
                    background: cyan;
                    border: none;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <h1>Bienvenue sur mon site 100% Python 🚀</h1>
            <div class="box">
                <a href='/about'>À propos</a>
                <br><br>
                <form action='/salut' method='POST'>
                    <input type='text' name='prenom' placeholder='Entre ton prénom'>
                    <button type='submit'>Envoyer</button>
                </form>
            </div>
        </body>
    </html>
    """

# PAGE ABOUT
@app.route("/about")
def about():
    return """
    <h1>Page À propos</h1>
    <p>Ce site est entièrement généré en Python avec Flask.</p>
    <a href="/">Retour accueil</a>
    """

# TRAITEMENT FORMULAIRE
@app.route("/salut", methods=["POST"])
def salut():
    prenom = request.form.get("prenom")
    return f"""
    <h1>Salut {prenom} 😎</h1>
    <p>Ton message a été envoyé avec succès.</p>
    <a href="/">Retour accueil</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
