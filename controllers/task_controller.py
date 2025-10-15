class TaskController:
    def __init__(self):
        self.tasks = []

    def add(self, new_task):
        self.tasks.append(new_task)

    def delete(self, index):
        try:
            removed_task = self.tasks.pop(index)
            print(f"Tâche supprimée : {removed_task}")
        except IndexError:
            print("Erreur : index invalide ❌")

    def display(self):
        if not self.tasks:
            print("Aucune tâche pour le moment")
        else:
            print("\n--- Liste des tâches ---")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
