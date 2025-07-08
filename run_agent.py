from agent_file import code_helper  # Import your agent

# Sample code to analyze
python_code = """
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""

# Initial state with the code
initial_state = {"code": python_code}

# Run the agent
result = code_helper.invoke(initial_state)

# Print results
print(f"Language: {result['language']}")
print(f"Functionality: {result['functionality']}")
print("\nDocumentation:")
print(result['documentation'])