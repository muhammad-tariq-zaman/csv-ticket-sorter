import csv, sys
ORDER = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}
def sort_tickets(rows):
    return sorted(rows, key=lambda r: (ORDER.get(r.get("priority", "P4"), 3), r.get("created_at", "")))
def sort_csv(inp, outp):
    with open(inp, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f)); fields = rows[0].keys() if rows else []
    with open(outp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(fields)); w.writeheader(); w.writerows(sort_tickets(rows))
    return len(rows)
if __name__ == "__main__":
    n = sort_csv(sys.argv[1], sys.argv[2])
    print(f"Sorted {n} tickets by priority, then creation time.")
