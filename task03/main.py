import sys
import re
from typing import Callable, List, Dict

def parse_log_line(line: str) -> Dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> List[Dict]:
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            log = parse_log_line(line.strip())
            logs.append(log)
    return logs

def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python task03/main.py task03/logfile.log error")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(log_file_path)
    except Exception as e:
        print(f"Помилка при читанні файлу логів: {e}")
        sys.exit(1)

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
