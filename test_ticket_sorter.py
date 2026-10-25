import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest, tempfile
from pathlib import Path
from ticket_sorter import sort_tickets, sort_csv
class T(unittest.TestCase):
    def test_p1_first(self):
        rows = [{"priority": "P3", "created_at": "2026-01-01"}, {"priority": "P1", "created_at": "2026-01-02"}]
        self.assertEqual(sort_tickets(rows)[0]["priority"], "P1")
    def test_csv_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d)/"in.csv"; src.write_text("id,priority,created_at\n2,P2,2026-01-01\n1,P1,2026-01-02\n")
            out = Path(d)/"out.csv"; self.assertEqual(sort_csv(str(src), str(out)), 2)
            self.assertIn("P1", out.read_text().splitlines()[1])
if __name__ == "__main__": unittest.main()
