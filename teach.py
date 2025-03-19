import pandas as pd
import os
import glob

# Function to generate markdown from multiple Excel files in a directory
def generate_markdown_from_excel(input_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)  # Ensure output directory exists
    
    print(f"Searching for Excel files in: {input_directory}")
    excel_files = glob.glob(os.path.join(input_directory, "*.xlsx"))
    print(f"Found Excel files: {excel_files}")
    
    for file in excel_files:
        print(f"Processing file: {file}")
        df = pd.read_excel(file, sheet_name=None)  # Load all sheets
        
        for sheet_name, sheet_df in df.items():  # Iterate through all sheets
            print(f"Processing sheet: {sheet_name} from file: {file}")
            sheet_df.columns = sheet_df.columns.str.strip()  # Strip whitespace from column names
            print(f"Columns in sheet: {sheet_df.columns}")
            
            markdown_content = f"""
# PMRF - Foundations and Applications of Machine Learning (Bengali)

## Video Lectures ({sheet_name})

Below is a list of video lectures embedded for easy access.
"""
            
            video_count = 0
            
            for index, row in sheet_df.iterrows():
                if 'YouTube link' in row and pd.notna(row['YouTube link']):
                    video_id = row['YouTube link'].split('/')[-1]
                    markdown_content += f"""
### {row.get('Weeks', 'Unknown Week')}

[![Video Link](https://img.youtube.com/vi/{video_id}/0.jpg)]({row['YouTube link']})

<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
"""
                    video_count += 1
            
            if video_count == 0:
                print(f"No valid video links found in sheet: {sheet_name}, skipping markdown generation.")
                continue
            
            # Generate output markdown file name based on Excel file and sheet name
            output_file_name = f"{os.path.splitext(os.path.basename(file))[0]}_{sheet_name}.md"
            output_file_path = os.path.join(output_directory, output_file_name)
            
            with open(output_file_path, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_content)
            
            if os.path.exists(output_file_path):
                print(f"Successfully created: {output_file_path}")
            else:
                print(f"Failed to create: {output_file_path}")


# Example usage
input_directory = r"C:\Users\mainak\Documents\GitHub\Mainak1792.github.io\csv_files"  # Change this to your input CSV directory
output_directory = r"C:\Users\mainak\Documents\GitHub\Mainak1792.github.io\_teaching"  # Target markdown storage directory
generate_markdown_from_excel(input_directory, output_directory)
