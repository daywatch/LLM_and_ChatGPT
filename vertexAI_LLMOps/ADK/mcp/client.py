from fastmcp import Client
import asyncio

client = Client("<YOUR-MCP-URL-DEPLOYED-IN-RUN-OR-GKE>/mcp")

async def call_tool(emp_id: str):
    async with client:
        result = await client.call_tool("get_employee_salary", {"emp_id": emp_id})
        print(result)

async def call_resource():
    async with client:
        result = await client.read_resource("info://employees")
        print(result)

async def call_tool_all_employees():
    async with client:
        result = await client.call_tool("list_employees")
        print(result)

asyncio.run(call_tool(101))
asyncio.run(call_tool_all_employees())


