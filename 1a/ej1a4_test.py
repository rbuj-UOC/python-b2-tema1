import pytest
from ej1a4 import create_task, change_task_status, tasks, TaskStatus, list_tasks

@pytest.fixture
def setup_task_system() -> None:
    tasks.clear()

def test_create_task(setup_task_system) -> None:
    task_id = create_task("Test task")
    assert task_id == 1, "The task ID should be 1 for the first created task."
    assert tasks[task_id].title == "Test task", "The task title should match 'Test task'."
    assert tasks[task_id].status == TaskStatus.PENDING, "The initial status should be 'Pending'."

def test_change_task_status(setup_task_system) -> None:
    task_id = create_task("Another test task")
    result = change_task_status(task_id, TaskStatus.COMPLETED)
    assert result is True, "Change task status should succeed."
    assert tasks[task_id].status == TaskStatus.COMPLETED, "The task status should be updated to 'Completed'."

def test_change_task_status_invalid_task(setup_task_system) -> None:
    result = change_task_status(999, TaskStatus.COMPLETED)  
    assert result is False, "Changing status for a non-existent task should fail."

def test_list_tasks(capfd, setup_task_system) -> None:
    create_task("List task")
    create_task("Another list task")
    change_task_status(1, TaskStatus.IN_PROGRESS)
    list_tasks()
    out, _ = capfd.readouterr()
    assert "ID: 1, Title: List task, Status: In Progress" in out, "Task 1 should be listed as 'In Progress'."
    assert "ID: 2, Title: Another list task, Status: Pending" in out, "Task 2 should be listed as 'Pending'."
