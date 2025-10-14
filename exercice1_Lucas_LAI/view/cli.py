class View:
    def displayView(self, message):
        print(message)
    
    def show_task(self, tasks):
        if not tasks:
            print("Il n'y a aucune tâche.")
        else:
            print("\nVoici la liste des tâches :")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
