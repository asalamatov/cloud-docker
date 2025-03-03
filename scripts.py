import os
import re
import collections
import socket

# File paths
# data_dir = "/Users/azamat/Desktop/UC/Spring2025/Cloud/docker_hw/data" #
data_dir = "/home/data"
output_file = os.path.join(data_dir, "output/result.txt")
file1_path = os.path.join(data_dir, "IF-1.txt")
file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words = re.findall(r"\b\w+(?:'\w+)?\b", text)  # Handle contractions
        return collections.Counter(words)

# Process files
if os.path.exists(file1_path) and os.path.exists(file2_path):
    counter1 = count_words(file1_path)
    counter2 = count_words(file2_path)
    
    total_words_1 = sum(counter1.values())
    total_words_2 = sum(counter2.values())
    grand_total = total_words_1 + total_words_2

    # Top 3 words
    top3_file1 = counter1.most_common(3)
    top3_file2 = counter2.most_common(3)

    # Get IP Address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Save results
    result_content = f"""Word count in {file1_path}: {total_words_1}
Word count in {file2_path}: {total_words_2}
Grand Total Words: {grand_total}

Top 3 words in {file1_path}:
{top3_file1}

Top 3 words in {file2_path} (handling contractions):
{top3_file2}

Container IP Address: {ip_address}
"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        f.write(result_content)

    # Print results
    print(result_content)
else:
    print("Error: Text files not found.")

