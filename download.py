from yt_dlp import YoutubeDL
import os
from typing import Optional
from urllib.parse import urlparse, parse_qs

def is_playlist_url(url: str) -> bool:
    """
    Check if the provided URL is a playlist or a single video.
    
    Args:
        url (str): YouTube URL to check
        
    Returns:
        bool: True if URL is a playlist, False if single video
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return 'list' in query_params

def download_youtube_content(url: str, output_path: Optional[str] = None, audio_only: bool = False) -> None:
    """
    Download YouTube content (single video or playlist) in MP4 format only.
    
    Args:
        url (str): URL of the YouTube video or playlist
        output_path (str, optional): Directory to save the downloads. Defaults to './downloads'
    """
    # Set default output path if none provided
    if output_path is None:
        output_path = os.path.join(os.getcwd(), 'downloads')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Configure yt-dlp options
    if audio_only:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ignoreerrors': True,
            'no_warnings': False,
            'extract_flat': False,
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
    else:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
            'ignoreerrors': True,
            'no_warnings': False,
            'extract_flat': False,
            'writesubtitles': False,
            'writethumbnail': False,
            'writeautomaticsub': False,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'keepvideo': False,
            'clean_infojson': True
        }

    # Set different output templates for playlists and single videos
    if is_playlist_url(url):
        ydl_opts['outtmpl'] = os.path.join(output_path, '%(playlist_title)s', '%(playlist_index)s-%(title)s.%(ext)s')
        print("Detected playlist URL. Downloading entire playlist...")
    else:
        ydl_opts['outtmpl'] = os.path.join(output_path, '%(title)s.%(ext)s')
        print("Detected single video URL. Downloading video...")
  
    try:
        with YoutubeDL(ydl_opts) as ydl:
            # Download content
            ydl.download([url])
            print(f"\nDownload completed successfully! Files saved to: {output_path}")
            # Extract audio to MP3 after video download
            import subprocess
            for root, _, files in os.walk(output_path):
                for file in files:
                    if file.endswith('.mp4'):
                        video_path = os.path.join(root, file)
                        audio_path = os.path.join(root, os.path.splitext(file)[0] + '.mp3')
                        try:
                            subprocess.run([
                                'ffmpeg', '-i', video_path,
                                '-vn', '-acodec', 'libmp3lame',
                                '-q:a', '2',  # High quality MP3
                                audio_path
                            ], check=True)
                            print(f"Audio extracted: {audio_path}")
                        except subprocess.CalledProcessError as e:
                            print(f"Error extracting audio from {file}: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    url = input("Enter the YouTube URL (video or playlist): ")
    output_dir = input("Enter output directory (press Enter for default): ").strip()
    
    if output_dir:
        download_youtube_content(url, output_dir)
    else:
        download_youtube_content(url)