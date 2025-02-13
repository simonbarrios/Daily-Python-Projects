# Mood-Based Playlist Generator

A simple Python application that generates music playlists based on your current mood using PyQt6 for the graphical user interface.

## Features

- Clean and intuitive GUI interface
- Three mood options: Happy, Sad, and Energetic
- Randomly shuffled playlists for each mood
- Visually appealing color-coded mood buttons
- Instant playlist generation

## How It Works

1. Launch the application
2. Select your current mood from the three available options:
   - Happy (Gold button)
   - Sad (Sky Blue button)
   - Energetic (Coral button)
3. A randomized playlist matching your mood will be generated and displayed

## Technical Implementation

The application is built using:

- PyQt6 for the GUI framework
- Python's random module for playlist shuffling
- Mock song database organized by moods

## Future Enhancement Ideas

### 1. Spotify Integration

- Implement Spotify API integration using `spotipy` library
- Features to add:
  - Real-time playlist creation in user's Spotify account
  - Song recommendations based on audio features (tempo, valence, energy)
  - User authentication and profile management
  - Ability to save and share mood playlists

### 2. YouTube Music Integration

- Integrate YouTube Music API
- Additional features:
  - Direct music playback within the application
  - Music video suggestions
  - Playlist export to YouTube Music
  - Song lyrics display

### 3. Enhanced User Experience

- Add more mood categories (Relaxed, Focused, Romantic, etc.)
- Create custom mood combinations
- Add user profiles and playlist history
- Implement playlist rating system
- Add cross-platform support (mobile apps)

### 4. Social Features

- Share playlists with friends
- Collaborative mood playlists
- Mood-based music recommendations between users
- Integration with social media platforms

## Requirements

- Python 3.x
- PyQt6

## Installation

1. Clone the repository
2. Install dependencies
3. Run the application

## Usage

1. Launch the application
2. Select your current mood from the three available options
3. A randomized playlist matching your mood will be generated and displayed
