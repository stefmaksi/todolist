from datetime import date

mock_db = [
    {
        "id": 1,
        "name": "Buy Groceris",
        "status": "Active",
        "tags": ["Kitchen", "Food"],
        "creation_date": "2026-02-17",
    }
]


# 1. The Data Class (Only holds task info)
class Task:
    def __init__(self, id, name, status, tags, creation_date):
        self.id = id
        self.name = name
        self.status = status
        self.tags = tags
        self.creation_date = creation_date

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "tags": self.tags,
            "creation_date": str(self.creation_date),
        }


# 2. The Manager Class (Handles the Database operations)
class TaskManager:
    def __init__(self):
        self.db = mock_db

    def add_task(self, task_object):
        self.db.append(task_object.to_dict())

    def view_tasks(self):
        for item in self.db:
            print(item)

    def remove_task(self, task_id):
        for task in self.db:
            if task.get("id") == task_id:
                self.db.remove(task)
                break

    def update_task_name(self, task_id, new_name):
        for task in self.db:
            if task.get("id") == task_id:
                task.update({"name": new_name})

    def update_task_tags(self, task_id, new_tags):
        for task in self.db:
            if task.get("id") == task_id:
                task.update({"tags": new_tags})

    def mark_task(self, task_id):
        for task in self.db:
            if task.get("id") == task_id:
                task.update({"status": "Finished"})
                break


manager = TaskManager()

task2 = Task(
    id=2,  # Integer
    name="Playing soccer with Claire",
    status="Active",
    tags=["sport", "meeting"],
    creation_date=date.today(),
)

task3 = Task(
    id=3,  # Integer
    name="Playing soccer with John",
    status="Active",
    tags=["sport", "meeting"],
    creation_date=date.today(),
)

# add tasks
manager.add_task(task2)
manager.add_task(task3)

# Remove Task 3
manager.remove_task(3)

# mark status task 2 finished
manager.mark_task(2)

# update name task 2 playing pickelball
manager.update_task_name(2, "Playing pickelball")

# update tags task 2 to only sports
manager.update_task_tags(2, ["sport", "meeting", "pickel"])

manager.view_tasks()
