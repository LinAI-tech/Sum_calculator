# SumCalculator.py
# Streamlit app to find sum of all numbers from 1 to n using a loop

import streamlit as st

def calculate_sum(n):
    """
    Calculate the sum of all numbers from 1 to n using a loop.
    
    Args:
        n (int): The upper limit number
    
    Returns:
        int: Sum of numbers from 1 to n
    """
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

def main():
    """Main Streamlit application"""
    # Set page configuration
    st.set_page_config(
        page_title="Sum Calculator",
        page_icon="🧮",
        layout="centered"
    )
    
    # App title and description
    st.title("🧮 Sum Calculator")
    st.markdown("Calculate the sum of all numbers from 1 to n using a loop")
    
    # Create input section
    st.header("Input")
    n = st.number_input(
        "Enter a positive integer (n):",
        min_value=1,
        max_value=10000,
        value=10,
        step=1,
        help="Enter any positive integer between 1 and 10,000"
    )
    
    # Calculate button
    if st.button("Calculate Sum", type="primary"):
        # Calculate sum using loop
        result = calculate_sum(n)
        
        # Display results
        st.header("Results")
        
        # Show the result in a metric
        st.metric(
            label=f"Sum of numbers from 1 to {n}",
            value=f"{result:,}"
        )
        
        # Show formula
        st.info(f"**Formula used:** 1 + 2 + 3 + ... + {n} = {result:,}")
        
        # Show calculation breakdown for small numbers
        if n <= 20:
            st.subheader("Calculation Breakdown")
            numbers = " + ".join(str(i) for i in range(1, n + 1))
            st.code(f"{numbers} = {result:,}")
        
        # Show mathematical verification
        st.subheader("Mathematical Verification")
        mathematical_result = n * (n + 1) // 2
        st.write(f"Using the formula n(n+1)/2 = {n}×{n+1}/2 = {mathematical_result:,}")
        
        if result == mathematical_result:
            st.success("✅ Loop calculation matches mathematical formula!")
        else:
            st.error("❌ Calculation error detected!")
        
        # Show step-by-step loop process for very small numbers
        if n <= 10:
            st.subheader("Step-by-Step Loop Process")
            steps = []
            running_sum = 0
            for i in range(1, n + 1):
                running_sum += i
                steps.append(f"Step {i}: Add {i} → Running sum = {running_sum}")
            
            for step in steps:
                st.text(step)
    
    # Add some additional information
    st.markdown("---")
    st.markdown("### About this Calculator")
    st.markdown("""
    This calculator uses a **for loop** to iterate through all numbers from 1 to n and adds them together.
    
    **Algorithm:**
    1. Initialize sum = 0
    2. For each number i from 1 to n:
       - Add i to sum
    3. Return the final sum
    
    **Time Complexity:** O(n)  
    **Space Complexity:** O(1)
    """)

if __name__ == "__main__":
    main()