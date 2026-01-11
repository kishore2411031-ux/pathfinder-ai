from flask import Flask, render_template, request

app = Flask(__name__)

career_paths = {
    "Data Analyst": ["python", "sql", "excel", "powerbi", "statistics"],
    "Data Scientist": ["python", "sql", "pandas", "numpy", "machine learning", "deep learning"],
    "Web Developer": ["html", "css", "javascript", "python", "flask"],
    "AI Engineer": ["python", "machine learning", "deep learning", "nlp", "tensorflow"]
}

def recommend_role(user_skills):
    if "python" in user_skills and "sql" in user_skills:
        return "Data Analyst"
    if "python" in user_skills and "machine learning" in user_skills:
        return "Data Scientist"
    if "html" in user_skills and "css" in user_skills:
        return "Web Developer"
    return "AI Engineer"

@app.route("/", methods=["GET", "POST"])
def home():
    skills = None
    role = None
    missing = []

    if request.method == "POST":
        skills = request.form.get("skills")
        user_skills = [s.strip().lower() for s in skills.split(",")]

        role = recommend_role(user_skills)
        required = career_paths[role]
        missing = [skill for skill in required if skill not in user_skills]

    return render_template("index.html", skills=skills, role=role, missing=missing)

if __name__ == "__main__":
    app.run(debug=True)
