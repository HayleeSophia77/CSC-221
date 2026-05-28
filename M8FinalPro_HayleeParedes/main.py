# Student Enrollment Data Analysis
# 12/11/2025
# M8FinalPro
# Haylee Paredes

"""
Step 1: Upload CSV file through Streamlit.
Step 2: Validate CSV structure.
Step 3: Filter out certificates (keep programs only).
Step 4: Calculate average credits.
Step 5: Let user choose analysis type (By Program or By Division).
Step 6: Display results with tables and charts.
Step 7: Allow Excel download.
"""

import streamlit as st
import pandas as pd
import functions as fn

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------------------

def main():
    """
    Parameters:
        None
    
    Returns:
        None
    """
    # Custom CSS for styling the app - handles both light and dark mode
    st.markdown("""
        <style>
        /* Keep sidebar always visible */
        section[data-testid="stSidebar"] {
            display: block !important;
        }
        
        /* Make collapse/expand arrow always visible */
        [data-testid="collapsedControl"] {
            opacity: 1 !important;
            visibility: visible !important;
        }
        
        /* Styling for LIGHT MODE */
        @media (prefers-color-scheme: light) {
            section[data-testid="stSidebar"] {
                background-color: #f8f9fa !important;
            }
            
            h1 {
                color: #1f77b4 !important;
                font-weight: 700;
                padding-bottom: 20px;
            }
            
            h2 {
                color: #2c3e50 !important;
                padding-top: 20px;
            }
            
            h3 {
                color: #34495e !important;
            }
            
            .element-container:has(.stSuccess) {
                background-color: #d4edda !important;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #28a745;
            }
            
            .stDownloadButton button {
                background-color: #1f77b4 !important;
                color: white !important;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: 600;
            }
            
            .stDownloadButton button:hover {
                background-color: #155a8a !important;
            }
            
            .dataframe {
                border: 1px solid #e1e4e8;
                border-radius: 5px;
            }
        }
        
        /* Styling for DARK MODE */
        @media (prefers-color-scheme: dark) {
            section[data-testid="stSidebar"] {
                background-color: #1e1e1e !important;
                border-right: 1px solid #3a3a3a;
            }
            
            h1 {
                color: #58a6ff !important;
                font-weight: 700;
                padding-bottom: 20px;
            }
            
            h2 {
                color: #79c0ff !important;
                padding-top: 20px;
            }
            
            h3 {
                color: #a5d6ff !important;
            }
            
            .element-container:has(.stSuccess) {
                background-color: #1e4620 !important;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #3fb950;
            }
            
            .stDownloadButton button {
                background-color: #238636 !important;
                color: white !important;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: 600;
                border: 1px solid #2ea043;
            }
            
            .stDownloadButton button:hover {
                background-color: #2ea043 !important;
            }
            
            .dataframe {
                border: 1px solid #3a3a3a;
                border-radius: 5px;
            }
        }
        
        /* Universal styling (applies to both modes) */
        .block-container {
            padding: 2rem 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Student Enrollment Data Analysis")
    st.write("Analyze average credit hours by program or division")
    
    # Sidebar file uploader(lets user select CSV file)
    st.sidebar.header("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # Read uploaded CSV file
            df = pd.read_csv(uploaded_file)
            
            # Validate that CSV has correct structure
            if fn.validateCSV(df):
                st.sidebar.success("CSV validated successfully!")
                
                st.sidebar.write(f"Total records: {len(df)}")
                
                # Filter out certificates(only want degree programs)
                df_programs = fn.filterPrograms(df)
                
                if df_programs is not None:
                    st.sidebar.write(f"Program records: {len(df_programs)}")
                    st.sidebar.write(f"Certificates filtered: {len(df) - len(df_programs)}")
                    
                    # Calculate avg credits for each program in each semester
                    avg_df = fn.calculateAverages(df_programs)
                    
                    if avg_df is not None:
                        # Get programs & divisions for filtering
                        programs = sorted(avg_df['Program'].unique())
                        divisions = sorted(avg_df['Division'].unique())
                        
                        # Let user choose between program or division analysis
                        st.sidebar.header("Analysis Type")
                        analysis_type = st.sidebar.radio("Select:", ["By Program", "By Division"])
                        
                        # Correct analysis view based on user selection
                        if analysis_type == "By Program":
                            programAnalysis(avg_df, programs)
                        else:
                            divisionAnalysis(avg_df, divisions)
                    else:
                        st.error("Error calculating averages")
                else:
                    st.error("Error filtering programs")
            else:
                st.error("CSV file structure is incorrect!")
                st.write("Required columns:")
                st.write("TermId, StudentId, StudentTermProgram, ActiveCredits, ProgramDivision, StudentName")
        
        except Exception as e:
            st.error(f"Error loading file: {e}")
    
    else:
        # Show instructions when no file is uploaded yet
        st.info("Please upload a CSV file to begin")
        
        st.write("### Instructions:")
        st.write("1. Upload your student data CSV file using the sidebar")
        st.write("2. Choose analysis type: By Program or By Division")
        st.write("3. Select filters and view results")
        st.write("4. Download data as CSV/Excel file")

# ----------------------------------------------------------------------

def programAnalysis(avg_df, programs):
    """
    Parameters:
        avg_df (DataFrame)
        programs (list)
    
    Returns:
        None
    """
    st.header("Analysis by Program")
    
    # Let user select which program to analyze
    selected_program = st.selectbox("Choose a program:", programs)
    
    # Filter data, only show selected program
    program_df = fn.filterBYprogram(avg_df, selected_program)
    program_semesters = sorted(program_df['Semester'].unique())
    
    # Create checkboxes for semester selection(arranged in 4 columns)
    st.subheader("Select Semesters:")
    selected_semesters = []
    
    cols = st.columns(4)
    for i, semester in enumerate(program_semesters):
        col_index = i % 4
        if cols[col_index].checkbox(semester, value=True, key=f"prog_{semester}"):
            selected_semesters.append(semester)
    
    if len(selected_semesters) > 0:
        # Filter data, only show selected semesters
        filtered_df = fn.filterBYsemesters(program_df, selected_semesters)
        
        st.subheader("Results")
        
        # Display data table
        st.write("**Data Table:**")
        display_df = filtered_df[['Semester', 'Division', 'Program', 'Avg_Credits']]
        st.dataframe(display_df)
        
        # Add download button for CSV export
        csv_file = fn.toCSV(display_df)
        st.download_button(
            label="Download CSV",
            data=csv_file,
            file_name=f"{selected_program}_data.csv",
            mime="text/csv"
        )
        
        # Show bar chart comparing semesters
        st.write("**Bar Chart - Average Credits by Semester:**")
        fig1 = fn.plotBar(
            filtered_df, 
            'Semester', 
            'Avg_Credits',
            f'Average Credits for {selected_program}'
        )
        if fig1:
            st.pyplot(fig1)
        
        # Show line chart visualizing trends over time
        st.write("**Line Chart - Trend Over Time:**")
        fig2 = fn.plotLine(
            filtered_df, 
            'Semester', 
            'Avg_Credits',
            f'Trend for {selected_program}'
        )
        if fig2:
            st.pyplot(fig2)
    else:
        st.warning("Please select at least one semester")

# ----------------------------------------------------------------------

def divisionAnalysis(avg_df, divisions):
    """
    Parameters:
        avg_df (DataFrame)
        divisions (list)
    
    Returns:
        None
    """
    st.header("Analysis by Division")
    
    # Let user select which division to analyze
    selected_division = st.selectbox("Choose a division:", divisions)
    
    # Filter data, only show selected division
    division_df = fn.filterBYdivision(avg_df, selected_division)
    division_semesters = sorted(division_df['Semester'].unique())
    
    # Create checkboxes for semester selection(arranged in 4 columns)
    st.subheader("Select Semesters:")
    selected_semesters = []
    
    cols = st.columns(4)
    for i, semester in enumerate(division_semesters):
        col_index = i % 4
        if cols[col_index].checkbox(semester, value=True, key=f"div_{semester}"):
            selected_semesters.append(semester)
    
    if len(selected_semesters) > 0:
        # Filter only show selected semesters
        filtered_df = fn.filterBYsemesters(division_df, selected_semesters)
        
        st.subheader("Results")
        
        # Display the data table
        st.write("**Data Table:**")
        display_df = filtered_df[['Semester', 'Division', 'Program', 'Avg_Credits']]
        st.dataframe(display_df)
        
        # Add download button for CSV export
        csv_file = fn.toCSV(display_df)
        st.download_button(
            label="Download CSV",
            data=csv_file,
            file_name=f"{selected_division}_data.csv",
            mime="text/csv"
        )
        
        # Show bar chart comparing programs within the division
        st.write("**Bar Chart - Compare Programs in Division:**")
        fig1 = fn.plotBar(
            filtered_df, 
            'Program', 
            'Avg_Credits',
            f'Programs in {selected_division}'
        )
        if fig1:
            st.pyplot(fig1)
        
        # Show line chart with separate lines for each program
        st.write("**Line Chart - Trends by Program:**")
        fig2 = fn.plotLine(
            filtered_df, 
            'Semester', 
            'Avg_Credits',
            f'Trends in {selected_division}',
            group_col='Program'
        )
        if fig2:
            st.pyplot(fig2)
    else:
        st.warning("Please select at least one semester")

if __name__ == "__main__":
    main()