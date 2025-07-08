import streamlit as st
from agent_file import code_helper

st.set_page_config(page_title="Code Analyzer", layout="wide")
st.title("🤖 AutoDoc Agent")

st.write("This tool detects the programming language, analyzes the functionality, and generates documentation — all powered by LangGraph + GPT-4o-mini.")

example_codes = {
    "🧮 Fibonacci (Python)": """def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
""",
    "🔁 Factorial (Python)": """def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
""",
    "📚 Class Example (Java)": """public class Book {
    private String title;

    public Book(String t) {
        this.title = t;
    }

    public void printTitle() {
        System.out.println(this.title);
    }
}""",
    "🖨️ Print Loop (C++)": """#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 5; i++) {
        cout << "Hello, world!" << endl;
    }
    return 0;
}""",
}

# Set default input value
code_input = ""

# Code example selector
st.subheader("🧪 Try Example Code")
example_choice = st.selectbox(
    "Choose an example to auto-fill the code area:",
    ["None"] + list(example_codes.keys()),
    index=0,
    help="Test with an example code snippet !"
)

# Prefill textarea if example selected
if example_choice != "None":
    code_input = example_codes[example_choice]


# Input box
code_input = st.text_area("✏️ Paste your code here:",  value=code_input, height=300)


if st.button("Analyze Code") and code_input.strip():
    with st.spinner("Analyzing..."):
        try:
            initial_state = {"code": code_input}
            result = code_helper.invoke(initial_state)

            st.success("✅ Analysis Complete!")

            # Results
            st.subheader("📌 Detected Language")
            st.code(result["language"], language="text")

            st.subheader("🧠 Code Functionality")
            st.write(result["functionality"])

            st.subheader("📄 Generated Documentation")
            st.markdown(result["documentation"], unsafe_allow_html=True)

            st.subheader("📝 Code with Inline Comments")
            st.code(result["commented_code"], language=result["language"].lower())

        
        except Exception as e:
            st.error(f"❌ Error: {e}")
else:
    st.info("💡 Enter some code and click Analyze.")
