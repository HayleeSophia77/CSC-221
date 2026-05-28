# Student Enrollment Data Analysis
# 12/11/2025
# M8FinalPro
# Haylee Paredes

"""
Step 1: Load and validate CSV data.
Step 2: Filter out certificate programs.
Step 3: Calculate average credits per program per semester.
Step 4: Create filtering functions for programs and divisions.
Step 5: Create visualization functions using matplotlib.
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# ----------------------------------------------------------------------

def validateCSV(df):
    """
    Parameters:
        df (DataFrame)
    
    Returns:
        bool
    """
    # List of required columns in exact order
    required = ['TermId', 'StudentId', 'StudentTermProgram', 
                'ActiveCredits', 'ProgramDivision', 'StudentName']
    
    if list(df.columns) == required:
        return True
    else:
        return False

# ----------------------------------------------------------------------

def filterPrograms(df):
    """
    Parameters:
        df (DataFrame)
    
    Returns:
        DataFrame
    """
    try:
        programs_df = df[df['StudentTermProgram'].str.startswith('A')].copy()
        return programs_df
    except Exception as e:
        print(f"Error filtering programs: {e}")
        return None

# ----------------------------------------------------------------------

def calculateAverages(df):
    """
    Parameters:
        df (DataFrame)
    
    Returns:
        DataFrame
    """
    try:
        # Group by semester, division, and program, then get mean of credits
        avg_df = df.groupby(['TermId', 'ProgramDivision', 'StudentTermProgram'])['ActiveCredits'].mean().reset_index()
        
        # Rename columns to be more readable for user
        avg_df.columns = ['Semester', 'Division', 'Program', 'Avg_Credits']
        avg_df['Avg_Credits'] = avg_df['Avg_Credits'].round(2)
        avg_df = avg_df.sort_values(['Semester', 'Division', 'Program'])
        
        return avg_df
    except Exception as e:
        print(f"Error calculating averages: {e}")
        return None

# ----------------------------------------------------------------------

def filterBYprogram(df, program):
    """
    Parameters:
        df (DataFrame)
        program (str)
    
    Returns:
        DataFrame
    """
    filtered = df[df['Program'] == program]
    return filtered

# ----------------------------------------------------------------------

def filterBYdivision(df, division):
    """
    Parameters:
        df (DataFrame)
        division (str)
    
    Returns:
        DataFrame
    """
    filtered = df[df['Division'] == division]
    return filtered

# ----------------------------------------------------------------------

def filterBYsemesters(df, semester_list):
    """
    Parameters:
        df (DataFrame)
        semester_list (list)
    
    Returns:
        DataFrame
    """
    # Use .isin() to filter for multiple semesters at once
    filtered = df[df['Semester'].isin(semester_list)]
    return filtered

# ----------------------------------------------------------------------

def plotBar(df, x_col, y_col, title):
    """
    Parameters:
        df (DataFrame)
        x_col (str)
        y_col (str)
        title (str)
    
    Returns:
        matplotlib figure
    """
    try:
        # Calculate avg
        avg_df = df.groupby(x_col)[y_col].mean().reset_index()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(avg_df[x_col], avg_df[y_col], color='steelblue')
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(title)
        # Angles labels so they don't overlap
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return fig
    except Exception as e:
        print(f"Error creating bar chart: {e}")
        return None

# ----------------------------------------------------------------------

def plotLine(df, x_col, y_col, title, group_col=None):
    """
    Parameters:
        df (DataFrame)
        x_col (str)
        y_col (str)
        title (str)
        group_col (str)
    
    Returns:
        matplotlib figure
    """
    try:
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if group_col:
            # Create separate line for each group
            groups = df[group_col].unique()
            for group in groups:
                group_df = df[df[group_col] == group]
                ax.plot(group_df[x_col], group_df[y_col], 
                       marker='o', label=group)
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        else:
            # Single line
            ax.plot(df[x_col], df[y_col], marker='o', color='steelblue')
        
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(title)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return fig
    except Exception as e:
        print(f"Error creating line chart: {e}")
        return None

# ----------------------------------------------------------------------

def toCSV(df):
    """
    Parameters:
        df (DataFrame)
    
    Returns:
        str (CSV data)
    """
    return df.to_csv(index=False)