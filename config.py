# config.py

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Application@123',
    'database': 'video_library'
}

# Sliding Window Sizes (in seconds)
WINDOW_SIZES = [30, 60, 120]

# Total number of frames in a video (example: 30 fps for a 1-minute video)
TOTAL_FRAMES = 30 * 60
