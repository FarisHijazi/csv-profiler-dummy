"""CSV Profiler - A tool for analyzing and profiling CSV files."""

from csv_profiler.profiler import profile_csv
from csv_profiler.render import generate_json_report, generate_markdown_report

__version__ = "0.1.0"
__all__ = ["profile_csv", "generate_json_report", "generate_markdown_report"]
