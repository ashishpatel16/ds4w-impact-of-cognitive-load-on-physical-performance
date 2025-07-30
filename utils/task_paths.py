import os
import glob
from pathlib import Path

def get_base_paths():
    """Get the base path for all data files."""
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(workspace_dir, "data")
    return data_dir

def find_all_recording_folders():
    """Find all recording folders across all participant directories."""
    data_dir = get_base_paths()
    participant_dirs = [d for d in os.listdir(data_dir) 
                       if os.path.isdir(os.path.join(data_dir, d))]
    
    recording_folders = []
    for participant in participant_dirs:
        signal_data_path = os.path.join(data_dir, participant, "csv", "Recordings_Signal_Data")
        if os.path.exists(signal_data_path):
            recording_folders.extend([
                os.path.join(signal_data_path, folder) 
                for folder in os.listdir(signal_data_path)
                if os.path.isdir(os.path.join(signal_data_path, folder))
            ])
    
    return recording_folders

def get_task_paths(task_suffix):
    """Get all CSV paths for a specific task."""
    all_folders = find_all_recording_folders()
    task_folders = [folder for folder in all_folders if folder.endswith(task_suffix)]
    
    csv_paths = []
    for folder in task_folders:
        csv_files = glob.glob(os.path.join(folder, "*.csv"))
        csv_paths.extend(csv_files)
    
    return csv_paths

def get_sit_to_stand_paths():
    """Get all sit-to-stand task CSV paths."""
    return get_task_paths("-sit_to_stand")

def get_sit_to_stand_challenge_paths():
    """Get all sit-to-stand challenge task CSV paths."""
    return get_task_paths("-sit_to_stand_challenge")

def get_water_task_paths():
    """Get all water task CSV paths."""
    return get_task_paths("-water_task")

def get_water_task_challenge_paths():
    """Get all water task challenge CSV paths."""
    return get_task_paths("-water_task_challenge")

def get_step_count_paths():
    """Get all step count task CSV paths."""
    return get_task_paths("-step_count")

def get_step_count_challenge_paths():
    """Get all step count challenge task CSV paths."""
    return get_task_paths("-step_count_challenge")

# Example usage
if __name__ == "__main__":
    print(f"Sit-to-stand tasks: {len(get_sit_to_stand_paths())}")
    print(f"Sit-to-stand challenge tasks: {len(get_sit_to_stand_challenge_paths())}")
    print(f"Water tasks: {len(get_water_task_paths())}")
    print(f"Water challenge tasks: {len(get_water_task_challenge_paths())}")
    print(f"Step count tasks: {len(get_step_count_paths())}")
    print(f"Step count challenge tasks: {len(get_step_count_challenge_paths())}")
    
    # Print the first path of each type as an example
    print("\nExamples:")
    tasks = [
        ("Sit-to-stand", get_sit_to_stand_paths()),
        ("Sit-to-stand challenge", get_sit_to_stand_challenge_paths()),
        ("Water task", get_water_task_paths()),
        ("Water challenge task", get_water_task_challenge_paths()),
        ("Step count", get_step_count_paths()),
        ("Step count challenge", get_step_count_challenge_paths())
    ]
    
    for name, paths in tasks:
        if paths:
            print(f"{name}: {paths[0]}") 