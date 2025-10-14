from controllers.task_controller import TaskController
from view.cli import View
from model.task import Task


def main():
    controller = TaskController()
    view = View()

    while True:
        print("\n=== ToDo List ===")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")

        choix = input("👉 Choisissez une option (1-4) : ")

        if choix == "1":
            titre = input("Entrez le nom de la tâche : ")
            nouvelle_tache = Task(titre)
            controller.add(nouvelle_tache)
            view.displayView("✅ Tâche ajoutée avec succès !")

        elif choix == "2":
            view.show_task([t.title for t in controller.tasks])

        elif choix == "3":
            view.show_task([t.title for t in controller.tasks])
            try:
                index = int(input("Numéro de la tâche à supprimer : ")) - 1
                controller.delete(index)
            except ValueError:
                print("⚠️ Veuillez entrer un nombre valide.")
            
        elif choix == "4":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()

