from pathlib import Path
import runpy


if __name__ == "__main__":
	base = Path(__file__).resolve().parent
	runpy.run_path(str(base / "inits" / "init_all.py"))
