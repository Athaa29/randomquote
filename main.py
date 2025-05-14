import customtkinter as ctk
import random
import pygame
import os
import itertools

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

quotes = [
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},
    {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "Everything you can imagine is real.", "author": "Pablo Picasso"},
    {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "It always seems impossible until it's done.", "author": "Nelson Mandela"},
    {"quote": "Dream big and dare to fail.", "author": "Norman Vaughan"},
]

root = ctk.CTk()
root.title("Random Quote Generator")
root.geometry("800x500")
root.resizable(False, False)

FONT_TITLE = ("Segoe UI", 26, "bold")
FONT_QUOTE = ("Segoe UI", 18, "italic")
FONT_AUTHOR = ("Segoe UI", 14)
FONT_BUTTON = ("Segoe UI", 14)

color_cycle = itertools.cycle(["#2193b0", "#6dd5ed", "#ffdde1", "#cc2b5e", "#753a88", "#ee9ca7"])
def animate_background():
    next_color = next(color_cycle)
    root.configure(fg_color=next_color)
    root.after(4000, animate_background)

title_label = ctk.CTkLabel(root, text="✨ Random Quote Generator ✨", font=FONT_TITLE, text_color="black")
title_label.pack(pady=20)

quote_label = ctk.CTkLabel(root, text="", font=FONT_QUOTE, wraplength=700, justify="center", text_color="#222")
quote_label.pack(pady=10)

author_label = ctk.CTkLabel(root, text="", font=FONT_AUTHOR, text_color="#444")
author_label.pack(pady=5)

def typewriter(widget, text, delay=30, index=0):
    if index < len(text):
        widget.configure(text=text[:index+1])
        widget.after(delay, typewriter, widget, text, delay, index + 1)

def show_quote():
    quote = random.choice(quotes)
    quote_label.configure(text="")
    author_label.configure(text="")
    typewriter(quote_label, f"“{quote['quote']}”")
    author_label.after(len(quote['quote']) * 30 + 300, lambda: author_label.configure(text=f"- {quote['author']}"))

generate_button = ctk.CTkButton(root, text="Generate Quote", font=FONT_BUTTON, command=show_quote)
generate_button.pack(pady=20)

pygame.mixer.init()
music_file = "Let down.mp3"
music_playing = True

music_title_label = ctk.CTkLabel(root, text="🎵 Loading...", font=("Segoe UI", 12), text_color="gray20")
music_title_label.pack(pady=5)

def start_music():
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(loops=-1)
        title = os.path.basename(music_file).replace("_", " ").replace(".mp3", "").title()
        music_title_label.configure(text=f"🎵 Now Playing: {title}")
    else:
        music_title_label.configure(text="❌ Music file not found.")

def toggle_music():
    global music_playing
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        music_button.configure(text="▶ Play Music")
        music_playing = False
    else:
        pygame.mixer.music.unpause()
        music_button.configure(text="⏸ Pause Music")
        music_playing = True

music_button = ctk.CTkButton(root, text="⏸ Pause Music", font=FONT_BUTTON, command=toggle_music)
music_button.pack(pady=5)

root.after(500, start_music)
animate_background()
root.mainloop()
