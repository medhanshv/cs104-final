#!/bin/bash

# Root directory where the structure will be created
ROOT_DIR="./bigdirectory"
MAX_DEPTH=2    # Maximum depth of subdirectories
MAX_BREADTH=10     # Maximum number of directories per level
MAX_FILES=5     # Maximum number of files per directory
MAX_LINES=50      # Maximum number of lines of content in a file


# Generate a random timestamp within the given range
generate_random_time() {
    # local start=$(date -d "01 Jan 2025 00:00" +%s)
    local end=$(date +%s)
	local diff=1209600
	# echo "${start} ${end} ${diff}"
    local random_time=$(( end - ((RANDOM*100) % diff) ))
	# echo "${random_time}"
    date -d "@$random_time" "+%Y%m%d%H%M"
}

# Generate random file content with a random number of lines
generate_random_content() {
    local line_count=$((RANDOM % (MAX_LINES + 1)))
    for ((i = 1; i <= line_count; i++)); do
        echo "Random line $i: $RANDOM"
    done
}

# Function to create random directories and files with random timestamps and content
create_structure() {
    local current_dir=$1
    local current_depth=$2

    # Exit if the maximum depth is reached
    if [[ $current_depth -ge $MAX_DEPTH ]]; then
        return
    fi

    # Create a random number of directories at this level
    local dir_count=$((RANDOM % (MAX_BREADTH + 1)))
    for ((i = 1; i <= dir_count; i++)); do
        local dir_name="dir_$RANDOM"
        mkdir -p "$current_dir/$dir_name"
        local random_time=$(generate_random_time)
        touch -t "$random_time" "$current_dir/$dir_name"
        # echo "Created directory: $current_dir/$dir_name with timestamp $random_time"

        # Recursively create subdirectories
        create_structure "$current_dir/$dir_name" $((current_depth + 1))
    done

    # Create a random number of files in this directory
    local file_count=$((RANDOM % (MAX_FILES + 1)))
    for ((i = 1; i <= file_count; i++)); do
        local file_name="file_$RANDOM.txt"
        generate_random_content > "$current_dir/$file_name"
        local random_time=$(generate_random_time)
        touch -t "$random_time" "$current_dir/$file_name"
        # echo "Created file: $current_dir/$file_name with timestamp $random_time"
    done
    local file_count=$((RANDOM % (MAX_FILES + 1)))
    for ((i = 1; i <= file_count; i++)); do
        local file_name="file_$RANDOM.log"
        generate_random_content > "$current_dir/$file_name"
        local random_time=$(generate_random_time)
        touch -t "$random_time" "$current_dir/$file_name"
        # echo "Created file: $current_dir/$file_name with timestamp $random_time"
    done
}

# # Main script execution
# rm -rf "$ROOT_DIR"  # Remove any existing structure
mkdir -p "$ROOT_DIR"
# echo "Created root directory: $ROOT_DIR"

# Start creating the structure
create_structure "$ROOT_DIR" 0

# echo "Random directory structure with timestamps and file content created in $ROOT_DIR"

