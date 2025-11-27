from database import fetch_sensitive_frames, fetch_all_videos
from config import TOTAL_FRAMES, WINDOW_SIZES


class DGIM:
    """Implements the DGIM algorithm for approximate counting."""

    def __init__(self, window_size):
        self.window_size = window_size
        self.buckets = []

    def add_bit(self, bit):
        """Add a bit to the stream."""
        if bit == 1:
            self.buckets.append((1, 0))  # (bucket size, timestamp)

        # Increment timestamps and remove expired buckets
        self.buckets = [(size, ts + 1) for size, ts in self.buckets if ts + 1 <= self.window_size]

        # Merge buckets if needed
        self.merge_buckets()

    def merge_buckets(self):
        """Merge buckets when two consecutive buckets have the same size."""
        i = 0
        while i < len(self.buckets) - 1:
            if self.buckets[i][0] == self.buckets[i + 1][0]:
                new_bucket = (self.buckets[i][0] * 2, self.buckets[i + 1][1])
                self.buckets[i] = new_bucket
                del self.buckets[i + 1]
            else:
                i += 1

    def estimate_count(self):
        """Estimate the count of 1s in the current window."""
        if not self.buckets:
            return 0
        total = sum(size for size, ts in self.buckets[:-1])
        total += self.buckets[-1][0] // 2  # Halve the oldest bucket size
        return total


def convert_to_binary_stream(sensitive_timestamps, total_frames):
    """Convert sensitive timestamps to a binary stream."""
    # Convert timestamps to integers and filter out invalid ones
    sensitive_timestamps = [int(round(timestamp)) for timestamp in sensitive_timestamps if timestamp >= 0]

    # Create a binary stream of length total_frames
    stream = [0] * total_frames
    for timestamp in sensitive_timestamps:
        if 0 <= timestamp < total_frames:  # Ensure valid index range
            stream[timestamp] = 1
    return stream


def process_video_with_dgim(video_id, total_frames):
    """Process a single video using DGIM and display results."""
    sensitive_timestamps = fetch_sensitive_frames(video_id)

    print(f"Processing video ID {video_id}: Sensitive timestamps = {sensitive_timestamps}")

    # Convert to binary stream
    stream = convert_to_binary_stream(sensitive_timestamps, total_frames)

    for window_size in WINDOW_SIZES:
        dgim = DGIM(window_size)
        for bit in stream:
            dgim.add_bit(bit)
        estimated_count = dgim.estimate_count()

        print(f"Video ID: {video_id}, Window Size: {window_size}, Estimated Sensitive Frames: {estimated_count}")


def process_all_videos():
    """Process all videos in the database."""
    videos = fetch_all_videos()

    for video in videos:
        video_id = video['id']
        print(f"Processing video ID: {video_id}")
        process_video_with_dgim(video_id, TOTAL_FRAMES)


if __name__ == "__main__":
    process_all_videos()
