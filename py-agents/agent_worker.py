import sys
import json
import time

def main():
    if len(sys.argv) < 2:
        print("Uso: agent_worker.py <task_json>")
        return

    task = json.loads(sys.argv[1])
    print(f"[Agente] Processing task: {task}")
    time.sleep(2)
    print(f"[Agente] Task {task['id']} finished")

if __name__ == "__main__":
    main()