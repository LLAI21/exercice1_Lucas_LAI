from flask import Flask, jsonify, request
from controllers.task_controller import TaskController
from model.task import Task

app = Flask(__name__)
controller = TaskController()

@app.route("/", methods=["GET", "POST", "DELETE"])
def home():
    if request.method == "GET":
        return jsonify({"message": "Méthode GET → Bienvenue dans l'API ToDoList"})
    elif request.method == "POST":
        return jsonify({"message": "Méthode POST → Vous avez envoyé une requête POST !"})
    elif request.method == "DELETE":
        return jsonify({"message": "Méthode DELETE → Vous avez supprimé une ressource !"})
    else:
        return jsonify({"error": "Méthode non supportée"}), 405


@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Veuillez fournir un titre de tâche"}), 400
    new_task = Task(data["title"])
    message = controller.add(new_task)
    message= "Success"
    return jsonify({"message": message})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    if not controller.display():
        return jsonify({"message": "Liste vide"})
    taskList = [str(task) for task in controller.display()]
    return jsonify(taskList)


@app.route("/delete/<int:index>", methods=["DELETE"])
def delete_task(index):
    index-=1
    if not controller.display():
        return jsonify({"message": "Liste vide"})
    message = controller.delete(index)
    message="Delete success"
    return jsonify({"message": message})

#Démarrer le FLASK
if __name__ == "__main__":
    app.run(debug=True)
