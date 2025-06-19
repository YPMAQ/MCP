from mcp.server.fastmcp import FastMCP
import os
app = FastMCP("MathMCP")

@app.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@app.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@app.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@app.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    import asyncio
    port = int(os.environ.get("PORT", 8000))
    asyncio.run(
        mcp.run_sse_async(
            host="0.0.0.0",  # Changed from 127.0.0.1 to allow external connections
            port=port,
            log_level="debug"
        )
    )
