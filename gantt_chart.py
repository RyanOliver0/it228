import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Define your tasks and their details
tasks = {
    'Task': ['Requirements Gathering', 'Market Research', 'Technology Stack Selection', 
             'User Interface Design', 'Database Schema Design', 'API Design', 
             'Frontend Development', 'Backend Development', 'Mobile App Development',
             'Database Implementation', 'Payment Gateway Integration', 'Unit Testing',
             'Integration Testing', 'User Acceptance Testing', 'Performance Testing',
             'Documentation', 'Deployment', 'Project Presentation Prep'],
    'Start': ['2024-10-14', '2024-10-14', '2024-10-14', '2024-10-16', '2024-10-16', 
              '2024-10-16', '2024-10-18', '2024-10-18', '2024-10-18', '2024-10-25', 
              '2024-10-25', '2024-10-29', '2024-11-01', '2024-11-01', '2024-11-01', 
              '2024-11-03', '2024-11-04', '2024-11-04'],
    'End': ['2024-10-15', '2024-10-14', '2024-10-14', '2024-10-18', '2024-10-17', 
            '2024-10-17', '2024-10-24', '2024-10-24', '2024-10-24', '2024-10-28', 
            '2024-10-26', '2024-10-31', '2024-11-03', '2024-11-02', '2024-11-02', 
            '2024-11-04', '2024-11-05', '2024-11-05'],
    'Team Member': ['Faris', 'Gale', 'Ryan', 'Faris', 'Gale', 'Ryan', 
                    'Faris', 'Gale', 'Ryan', 'Gale', 'Faris', 'All', 
                    'Gale', 'Faris', 'Ryan', 'All', 'Ryan', 'All']
}

# Create a DataFrame
df = pd.DataFrame(tasks)

# Convert the Start and End date to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Duration'] = (df['End'] - df['Start']).dt.days

# Create a figure and plot the Gantt chart
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the tasks on the Gantt chart
for i, task in df.iterrows():
    ax.barh(task['Task'], task['Duration'], left=task['Start'], color='skyblue')
    ax.text(task['Start'] + datetime.timedelta(days=1), i, f"{task['Team Member']}", 
            va='center', ha='left')

# Format the chart
ax.set_xlabel('Timeline')
ax.set_ylabel('Tasks')
ax.set_title('Project Gantt Chart')
ax.grid(True)

# Format the x-axis as dates
ax.xaxis_date()

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Display the Gantt chart
plt.tight_layout()
plt.show()
