class Task:
    # """Représente une tâche de la ToDoList."""

    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    # def mark_done(self):
    #     # """Marque la tâche comme terminée."""
    #     self.done = True

    # def __str__(self):
    #     # """Affichage lisible de la tâche."""
    #     status = "✅" if self.done else "❌"
    #     return f"{self.title} {status}"
