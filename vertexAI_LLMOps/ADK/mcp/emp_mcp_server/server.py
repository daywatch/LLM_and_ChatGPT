from fastmcp import FastMCP

# Create the MCP app instance
mcp = FastMCP("employee_server")

# Simple in-memory employee data
employees = {
    101: {"name": "Alice", "role": "Manager", "salary": 85000},
    102: {"name": "Bob", "role": "Engineer", "salary": 70000},
    103: {"name": "Charlie", "role": "Analyst", "salary": 65000},
}

@mcp.tool
def get_employee_salary(emp_id: int) -> dict:
    """
    Get employee details by ID.
    Returns name, role, and salary.
    """
    emp = employees.get(emp_id)
    if emp:
        return {"emp_id": emp_id, **emp}
    else:
        return {"error": "Employee not found"}

@mcp.tool
def list_employees() -> list:
    """List all employees."""
    return [
        {"emp_id": emp_id, "name": emp["name"], "role": emp["role"]}
        for emp_id, emp in employees.items()
    ]
# -------------------------------------------------
# Run the MCP server
# -------------------------------------------------
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8080)


