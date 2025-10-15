from flask import Flask, jsonify, request
from controllers.task_controller import TaskController
from model.task import Task

# ===============================
# 🌐 Flask : Application principale
# ===============================
app = Flask(__name__)
controller = TaskController()

@app.route("/")
def home():
    return "Bienvenue dans l'API ToDoList 📝"

# ➕ Ajouter une tâche
@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Veuillez fournir un titre de tâche"}), 400
    new_task = Task(data["title"])
    message = controller.add(new_task)
    return jsonify({"message": message})

# 📋 Lister toutes les tâches
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(controller.list_tasks())

# ❌ Supprimer une tâche
@app.route("/delete/<int:index>", methods=["DELETE"])
def delete_task(index):
    message = controller.delete(index)
    return jsonify({"message": message})

# ===============================
# 🚀 Lancer le serveur Flask
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
