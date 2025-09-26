from mcp.server.fastmcp import FastMCP
import os
import sqlite3
from typing import List, Dict, Any


app = FastMCP("sqlite")


@app.tool()
def execute_query(sql: str) -> List[Dict[str, Any]]:

	"""
	Execute a read-only SQL query against the configured SQLite database.

	Set the environment variable `SQLITE_DB_PATH` to the absolute path of the
	SQLite database file you want to query. This tool enforces read-only access
	by opening the database using the URI mode=ro flag.
	"""

	db_path = os.environ.get("SQLITE_DB_PATH")
	if not db_path:
		raise RuntimeError(
			"SQLITE_DB_PATH environment variable is not set; point it to your .db file"
		)

	# Enforce read-only connection using SQLite URI
	uri = f"file:{db_path}?mode=ro"
	connection = sqlite3.connect(uri, uri=True)
	try:
		connection.row_factory = sqlite3.Row
		cursor = connection.cursor()
		cursor.execute(sql)
		rows = cursor.fetchall()
		return [dict(row) for row in rows]
	finally:
		connection.close()


if __name__ == "__main__":
	# Run the MCP server over stdio (default)
	app.run()


