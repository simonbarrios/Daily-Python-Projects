import sys
import random
import PyQt6.QtWidgets as QW
import PyQt6.QtCore as QC

# Mock song database organized by mood
SONGS_DB = {
    "Happy": [
        "Don't Stop Believin' - Journey",
        "Happy - Pharrell Williams",
        "Walking on Sunshine - Katrina & The Waves",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Can't Stop the Feeling! - Justin Timberlake"
    ],
    "Sad": [
        "Someone Like You - Adele",
        "Yesterday - The Beatles",
        "All By Myself - Celine Dion",
        "Say Something - A Great Big World",
        "The Sound of Silence - Simon & Garfunkel"
    ],
    "Energetic": [
        "Eye of the Tiger - Survivor",
        "Stronger - Kanye West",
        "Thunderstruck - AC/DC",
        "Can't Hold Us - Macklemore & Ryan Lewis",
        "Shake It Off - Taylor Swift"
    ]
}

class MoodPlaylistGenerator(QW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mood-Based Playlist Generator")
        self.setFixedSize(400, 500)
        
        # Create central widget and layout
        central_widget = QW.QWidget()
        self.setCentralWidget(central_widget)
        layout = QW.QVBoxLayout(central_widget)
        
        # Create and add title label
        title_label = QW.QLabel("How are you feeling today?")
        title_label.setAlignment(QC.Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        layout.addWidget(title_label)
        
        # Create mood selection buttons
        self.create_mood_buttons(layout)
        
        # Create playlist display area
        self.playlist_display = QW.QTextEdit()
        self.playlist_display.setReadOnly(True)
        self.playlist_display.setStyleSheet("font-size: 14px; padding: 10px;")
        layout.addWidget(self.playlist_display)

    def create_mood_buttons(self, layout):
        moods = ["Happy", "Sad", "Energetic"]
        button_colors = {
            "Happy": "#FFD700",  # Gold
            "Sad": "#87CEEB",    # Sky Blue
            "Energetic": "#FF6B6B"  # Coral
        }
        
        for mood in moods:
            btn = QW.QPushButton(mood)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {button_colors[mood]};
                    border-radius: 15px;
                    padding: 10px;
                    font-size: 16px;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: darker({button_colors[mood]}, 110%);
                }}
            """)
            btn.clicked.connect(lambda checked, m=mood: self.generate_playlist(m))
            layout.addWidget(btn)

    def generate_playlist(self, mood):
        playlist = SONGS_DB[mood]
        random.shuffle(playlist)
        
        # Display the playlist
        self.playlist_display.clear()
        self.playlist_display.append(f"🎵 Your {mood} Playlist 🎵\n")
        for i, song in enumerate(playlist, 1):
            self.playlist_display.append(f"{i}. {song}")

def main():
    app = QW.QApplication(sys.argv)
    window = MoodPlaylistGenerator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()





