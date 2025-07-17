# NameFormatter.py
# Streamlit Name Formatter Application for VS Code
# Author: Python Developer

import streamlit as st
import pandas as pd

class NameFormatter:
    """A class to format names in different styles"""
    
    def __init__(self, full_name):
        """
        Initialize the NameFormatter with a full name
        
        Args:
            full_name (str): The full name to format
        """
        self.full_name = full_name.strip()
        self.name_parts = self._parse_name()
    
    def _parse_name(self):
        """Parse the full name into components"""
        if not self.full_name:
            return {'first': '', 'middle': [], 'last': ''}
        
        parts = self.full_name.split()
        
        if len(parts) == 1:
            return {'first': parts[0], 'middle': [], 'last': ''}
        elif len(parts) == 2:
            return {'first': parts[0], 'middle': [], 'last': parts[1]}
        else:
            return {
                'first': parts[0],
                'middle': parts[1:-1],
                'last': parts[-1]
            }
    
    def first_last(self):
        """Format: First Last"""
        if not self.name_parts['last']:
            return self.name_parts['first']
        return f"{self.name_parts['first']} {self.name_parts['last']}"
    
    def last_first(self):
        """Format: Last, First"""
        if not self.name_parts['last']:
            return self.name_parts['first']
        return f"{self.name_parts['last']}, {self.name_parts['first']}"
    
    def last_first_middle(self):
        """Format: Last, First Middle"""
        result = self.last_first()
        if self.name_parts['middle']:
            middle_names = ' '.join(self.name_parts['middle'])
            result += f" {middle_names}"
        return result
    
    def first_middle_last(self):
        """Format: First Middle Last (original order)"""
        return self.full_name
    
    def initials_only(self):
        """Format: F.M.L."""
        initials = []
        if self.name_parts['first']:
            initials.append(self.name_parts['first'][0].upper())
        for middle in self.name_parts['middle']:
            initials.append(middle[0].upper())
        if self.name_parts['last']:
            initials.append(self.name_parts['last'][0].upper())
        return '.'.join(initials) + '.'
    
    def first_initial_last(self):
        """Format: F. Last"""
        if not self.name_parts['first']:
            return self.name_parts['last']
        if not self.name_parts['last']:
            return f"{self.name_parts['first'][0].upper()}."
        return f"{self.name_parts['first'][0].upper()}. {self.name_parts['last']}"
    
    def first_middle_initial_last(self):
        """Format: First M. Last"""
        result = self.name_parts['first']
        if self.name_parts['middle']:
            middle_initials = ' '.join([name[0].upper() + '.' for name in self.name_parts['middle']])
            result += f" {middle_initials}"
        if self.name_parts['last']:
            result += f" {self.name_parts['last']}"
        return result
    
    def uppercase(self):
        """Format: FIRST MIDDLE LAST"""
        return self.full_name.upper()
    
    def lowercase(self):
        """Format: first middle last"""
        return self.full_name.lower()
    
    def title_case(self):
        """Format: First Middle Last (proper title case)"""
        return self.full_name.title()
    
    def formal(self):
        """Format: Last, First Middle Initial(s)"""
        if not self.name_parts['last']:
            return self.name_parts['first']
        
        result = f"{self.name_parts['last']}, {self.name_parts['first']}"
        if self.name_parts['middle']:
            middle_initials = ' '.join([name[0].upper() + '.' for name in self.name_parts['middle']])
            result += f" {middle_initials}"
        return result
    
    def display_all_formats(self):
        """Display all available name formats"""
        formats = {
            "Original": self.full_name,
            "First Last": self.first_last(),
            "Last, First": self.last_first(),
            "Last, First Middle": self.last_first_middle(),
            "First Middle Last": self.first_middle_last(),
            "Initials Only": self.initials_only(),
            "First Initial Last": self.first_initial_last(),
            "First Middle Initial Last": self.first_middle_initial_last(),
            "Uppercase": self.uppercase(),
            "Lowercase": self.lowercase(),
            "Title Case": self.title_case(),
            "Formal": self.formal()
        }
        return formats

def main():
    """Main Streamlit application"""
    # Set page configuration
    st.set_page_config(
        page_title="Name Formatter",
        page_icon="👤",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .format-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        border-left: 4px solid #1f77b4;
    }
    .name-analysis {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header
    st.markdown('<h1 class="main-header">👤 Name Formatter Application</h1>', unsafe_allow_html=True)
    st.markdown("**Transform names into various professional formats**")
    
    # Sidebar for input and options
    st.sidebar.header("📝 Input Section")
    
    # Name input
    full_name = st.sidebar.text_input(
        "Enter Full Name:",
        placeholder="e.g., John Michael Smith",
        help="Enter a full name with first, middle (optional), and last names"
    )
    
    # Sample names for quick testing
    st.sidebar.subheader("🎯 Quick Test Names")
    sample_names = [
        "John Doe",
        "Mary Jane Smith", 
        "Alexander Hamilton",
        "Elizabeth Mary Johnson Brown",
        "Madonna",
        "Jean-Claude Van Damme"
    ]
    
    selected_sample = st.sidebar.selectbox(
        "Or select a sample name:",
        [""] + sample_names,
        help="Choose a sample name to test the formatter"
    )
    
    # Use sample name if selected
    if selected_sample:
        full_name = selected_sample
    
    # Display options
    st.sidebar.subheader("🎨 Display Options")
    show_analysis = st.sidebar.checkbox("Show Name Analysis", value=True)
    show_table = st.sidebar.checkbox("Show Results in Table", value=False)
    show_copy_buttons = st.sidebar.checkbox("Show Copy Buttons", value=True)
    
    # Main content area
    if full_name:
        # Create NameFormatter instance
        formatter = NameFormatter(full_name)
        
        # Display name analysis
        if show_analysis:
            st.markdown("## 🔍 Name Analysis")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.info(f"**First Name:** {formatter.name_parts['first'] or 'None'}")
            with col2:
                middle_names = ', '.join(formatter.name_parts['middle']) or 'None'
                st.info(f"**Middle Name(s):** {middle_names}")
            with col3:
                st.info(f"**Last Name:** {formatter.name_parts['last'] or 'None'}")
        
        # Get all formats
        formats = formatter.display_all_formats()
        
        # Display formats
        st.markdown("## 📋 Formatted Names")
        
        if show_table:
            # Display as table
            df = pd.DataFrame(list(formats.items()), columns=['Format', 'Result'])
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            # Display as cards
            col1, col2 = st.columns(2)
            
            format_items = list(formats.items())
            for i, (format_name, formatted_name) in enumerate(format_items):
                with col1 if i % 2 == 0 else col2:
                    st.markdown(f"""
                    <div class="format-card">
                        <strong>{format_name}</strong><br>
                        <code>{formatted_name}</code>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if show_copy_buttons:
                        if st.button(f"📋 Copy", key=f"copy_{i}", help=f"Copy {format_name}"):
                            st.code(formatted_name)
        
        # Statistics
        st.markdown("## 📊 Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Characters", len(full_name))
        with col2:
            st.metric("Word Count", len(full_name.split()))
        with col3:
            st.metric("Format Options", len(formats))
        with col4:
            st.metric("Initials", len(formatter.initials_only()) - formatter.initials_only().count('.'))
        
        # Export options
        st.markdown("## 💾 Export Options")
        col1, col2 = st.columns(2)
        
        with col1:
            # Create CSV data
            csv_data = pd.DataFrame(list(formats.items()), columns=['Format', 'Result'])
            csv_string = csv_data.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv_string,
                file_name=f"name_formats_{full_name.replace(' ', '_')}.csv",
                mime="text/csv"
            )
        
        with col2:
            # Create text summary
            text_summary = f"Name Formatting Results for: {full_name}\n" + "="*50 + "\n"
            for format_name, formatted_name in formats.items():
                text_summary += f"{format_name:.<25} {formatted_name}\n"
            
            st.download_button(
                label="📄 Download as Text",
                data=text_summary,
                file_name=f"name_formats_{full_name.replace(' ', '_')}.txt",
                mime="text/plain"
            )
    
    else:
        # Welcome message when no name is entered
        st.markdown("## 🚀 Welcome to Name Formatter!")
        st.markdown("""
        ### How to use:
        1. **Enter a full name** in the sidebar input field
        2. **Or select a sample name** from the dropdown
        3. **View the formatted results** in various styles
        4. **Copy or download** the results as needed
        
        ### Supported Formats:
        - **Business formats**: Last, First
        - **Formal styles**: Last, First Middle
        - **Initial formats**: F. Last, F.M.L.
        - **Case variations**: UPPERCASE, lowercase, Title Case
        - **And more!**
        """)
        
        # Show example
        st.markdown("### 🎯 Example:")
        st.code("Input: John Michael Smith")
        st.markdown("**Sample outputs:**")
        example_formats = [
            "First Last → John Smith",
            "Last, First → Smith, John",
            "Formal → Smith, John M.",
            "Initials Only → J.M.S."
        ]
        for example in example_formats:
            st.markdown(f"• {example}")
    
    # Footer
    st.markdown("---")
    st.markdown("*Built with ❤️ using Streamlit | Python Developer*")

if __name__ == "__main__":
    main()  