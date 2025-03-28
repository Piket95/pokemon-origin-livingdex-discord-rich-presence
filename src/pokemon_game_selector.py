import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import os

class PokemonGameSelector:
    def __init__(self):
        # Hauptfenster erstellen
        self.root = tk.Tk()
        self.root.title("Game Selector - Pokémon Origin Living Dex")

        # Icon setzen
        try:
            # Lade das webp Bild mit PIL
            icon_path = "assets/Main1.webp"
            icon = Image.open(icon_path)
            # Konvertiere zu PhotoImage
            icon_photo = ImageTk.PhotoImage(icon)
            self.root.iconphoto(True, icon_photo)
        except Exception as e:
            print(f"Fehler beim Laden des Icons: {e}")

        self.pokemon_games = {
            "Pokémon Red": {
                "generation": 1,
                "discord_asset": "pok_mon_rot-edition_icon_png",
                "icon_path": "assets/game_icons/Pokémon_Rot-Edition_Icon.png"
            },
            "Pokémon Blue": {
                "generation": 1,
                "discord_asset": "pok_mon_blau-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Blau-Edition_Icon.png"
            },
            "Pokémon Yellow": {
                "generation": 1,
                "discord_asset": "pok_mon_gelb-edition_icon_png",
                "icon_path": "assets/game_icons/Pokémon_Gelb-Edition_Icon.png"
            },
            "Pokémon Gold": {
                "generation": 2,
                "discord_asset": "pok_mon_gold-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Gold-Edition_Icon.png"
            },
            "Pokémon Silver": {
                "generation": 2,
                "discord_asset": "pok_mon_silber-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Silber-Edition_Icon.png"
            },
            "Pokémon Crystal": {
                "generation": 2,
                "discord_asset": "pok_mon_kristall-edition_icon_png",
                "icon_path": "assets/game_icons/Pokémon_Kristall-Edition_Icon.png"
            },
            "Pokémon Ruby": {
                "generation": 3,
                "discord_asset": "pok_mon_rubin-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Rubin-Edition_Icon.png"
            },
            "Pokémon Sapphire": {
                "generation": 3,
                "discord_asset": "pok_mon_saphir-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Saphir-Edition_Icon.png"
            },
            "Pokémon Emerald": {
                "generation": 3,
                "discord_asset": "pok_mon_smaragd-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Smaragd-Edition_Icon.png"
            },
            "Pokémon Firered": {
                "generation": 3,
                "discord_asset": "pok_mon_feuerrot-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Feuerrot-Edition_Icon.png"
            },
            "Pokémon Leafgreen": {
                "generation": 3,
                "discord_asset": "pok_mon_blattgruen-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Blattgruen-Edition_Icon.png"
            },
            "Pokémon Diamond": {
                "generation": 4,
                "discord_asset": "pok_mon_diamant-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Diamant-Edition_Icon.png"
            },
            "Pokémon Pearl": {
                "generation": 4,
                "discord_asset": "pok_mon_perl-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Perl-Edition_Icon.png"
            },
            "Pokémon Platinum": {
                "generation": 4,
                "discord_asset": "pok_mon_platin-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Platin-Edition_Icon.png"
            },
            "Pokémon HeartGold": {
                "generation": 4,
                "discord_asset": "pok_mon_heartgold-edition_icon_png",
                "icon_path": "assets/game_icons/Pokémon_HeartGold-Edition_Icon.png"
            },
            "Pokémon SoulSilver": {
                "generation": 4,
                "discord_asset": "pok_mon_soulsilver-edition_icon_png",
                "icon_path": "assets/game_icons/Pokémon_SoulSilver-Edition_Icon.png"
            },
            "Pokémon Black": {
                "generation": 5,
                "discord_asset": "pok_mon_schwarz-edition_icon_png",
                "icon_path": "assets/game_icons/Pokémon_Schwarz-Edition_Icon.png"
            },
            "Pokémon White": {
                "generation": 5,
                "discord_asset": "pok_mon_weiss-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Weiss-Edition_Icon.png"
            },
            "Pokémon Black 2": {
                "generation": 5,
                "discord_asset": "pok_mon_schwarz-2-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Schwarz-2-Edition_Icon.png"
            },
            "Pokémon White 2": {
                "generation": 5,
                "discord_asset": "pok_mon_weiss-2-edition_icon",
                "icon_path": "assets/game_icons/Pokémon_Weiss-2-Edition_Icon.png"
            },
            "Pokémon X": {
                "generation": 6,
                "discord_asset": "pok_mon_x_icon",
                "icon_path": "assets/game_icons/Pokémon_X_Icon.png"
            },
            "Pokémon Y": {
                "generation": 6,
                "discord_asset": "pok_mon_y_icon",
                "icon_path": "assets/game_icons/Pokémon_Y_Icon.png"
            },
            "Pokémon Omega Ruby": {
                "generation": 6,
                "discord_asset": "pok_mon_omega_rubin_icon",
                "icon_path": "assets/game_icons/Pokémon_Omega_Rubin_Icon.png"
            },
            "Pokémon Alpha Sapphire": {
                "generation": 6,
                "discord_asset": "pok_mon_alpha_saphir_icon",
                "icon_path": "assets/game_icons/Pokémon_Alpha_Saphir_Icon.png"
            },
            "Pokémon Sun": {
                "generation": 7,
                "discord_asset": "pok_mon_sonne_icon",
                "icon_path": "assets/game_icons/Pokémon_Sonne_Icon.png"
            },
            "Pokémon Moon": {
                "generation": 7,
                "discord_asset": "pok_mon_mond_icon",
                "icon_path": "assets/game_icons/Pokémon_Mond_Icon.png"
            },
            "Pokémon Ultrasun": {
                "generation": 7,
                "discord_asset": "pok_mon_ultrasonne_icon",
                "icon_path": "assets/game_icons/Pokémon_Ultrasonne_Icon.png"
            },
            "Pokémon Ultramoon": {
                "generation": 7,
                "discord_asset": "pok_mon_ultramond_icon",
                "icon_path": "assets/game_icons/Pokémon_Ultramond_Icon.png"
            },
            "Pokémon Sword": {
                "generation": 8,
                "discord_asset": "pok_mon_schwert_icon",
                "icon_path": "assets/game_icons/Pokémon_Schwert_Icon.png"
            },
            "Pokémon Shield": {
                "generation": 8,
                "discord_asset": "pok_mon_schild_icon",
                "icon_path": "assets/game_icons/Pokémon_Schild_Icon.png"
            },
            "Pokémon Scarlet": {
                "generation": 9,
                "discord_asset": "pok_mon_karmesin_icon",
                "icon_path": "assets/game_icons/Pokémon_Karmesin_Icon.png"
            },
            "Pokémon Violet": {
                "generation": 9,
                "discord_asset": "pok_mon_purpur_icon",
                "icon_path": "assets/game_icons/Pokémon_Purpur_Icon.png"
            }
        }

        # Variable für das ausgewählte Spiel
        self.selected_game = tk.StringVar()
        
        # Frame für besseres Layout
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Erstelle Frames für verschiedene Generationen
        frames = {
            "gen1_frame": "Generation 1 (Game Boy)",
            "gen2_frame": "Generation 2 (Game Boy Color)",
            "gen3_frame": "Generation 3 (Game Boy Advance)",
            "gen4_frame": "Generation 4 (Nintendo DS)",
            "gen5_frame": "Generation 5 (Nintendo DS)",
            "gen6_frame": "Generation 6 (Nintendo 3DS)",
            "gen7_frame": "Generation 7 (Nintendo 3DS)",
            "gen8_frame": "Generation 8 (Nintendo Switch)",
            "gen9_frame": "Generation 9 (Nintendo Switch)"
        }

        frame_counter = 0
        for varname, label in frames.items():
            row = frame_counter // 3    # Berechne Zeile (3 Frames pro Zeile)
            col = frame_counter % 3     # Berechne Spalte (0, 1, oder 2)
            
            vars(self)[varname] = ttk.LabelFrame(self.frame, text=label)
            vars(self)[varname].grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            
            # Konfiguriere die Spaltengewichtung für gleichmäßige Verteilung
            self.frame.grid_columnconfigure(col, weight=1)
            
            frame_counter += 1
        
        # Style für den aktiven Button
        self.style = ttk.Style()
        self.style.configure('Selected.TButton', background='blue', relief='sunken')
        
        # Variable für den aktuell ausgewählten Button
        self.current_button = None

        # Ersetze den alten Button-Erstellungscode mit einem einzelnen Aufruf
        self.create_generation_buttons()

        # Label für die Anzeige der aktuellen Auswahl
        self.selection_label = ttk.Label(self.frame, text="Aktuelle Auswahl: Keine")
        self.selection_label.grid(row=row + 1, column=1, padx=5, pady=5)

        self.root.update_idletasks()
        self.root.grid_propagate(True)
        self.root.resizable(False, False)
    
    def select_game(self, game, button):
        """Wird aufgerufen, wenn ein Spiel-Button geklickt wird"""

        # Vorherigen Button zurücksetzen
        if self.current_button:
            self.current_button.configure(style='TButton')  # Standard-Style
        
        # Neuen Button markieren
        button.configure(style='Selected.TButton')  # Ausgewählter Style
        self.current_button = button

        self.selected_game.set(game)
        self.selection_label.config(text=f"Aktuelle Auswahl: {game}")
        game_info = self.pokemon_games.get(game, "nicht gefunden")
        print(f"Ausgewähltes Spiel: {game}")
        print(f"Zugehörige Bilddatei: {game_info['icon_path']}")
        print(f"Zugehöriger Discord Image Key: {game_info['discord_asset']}")

    def getImageKey(self):
        game_info = self.pokemon_games.get(self.selected_game.get(), None)

        if game_info:
            return game_info['discord_asset']
        
        return None
    
    # Erstelle eine Hilfsfunktion für die Button-Erstellung
    def create_game_button(self, frame, game_name, row, col):
        """Erstellt einen Button mit Bild für ein Spiel"""
        try:
            game_info = self.pokemon_games[game_name]
            image_path = game_info["icon_path"]
            
            # Bild laden und in PhotoImage umwandeln
            image = Image.open(image_path)
            image = image.resize((50, 50))
            
            # Speichere das PhotoImage-Objekt
            if not hasattr(self, 'photos'):
                self.photos = {}
            self.photos[game_name] = ImageTk.PhotoImage(image)
            
            # Button mit Bild erstellen
            btn = ttk.Button(
                frame,
                text=game_name.replace("Pokémon ", ""),
                image=self.photos[game_name],
                compound="top"
            )
            btn.configure(command=lambda g=game_name, b=btn: self.select_game(g, b))
            btn.grid(row=row, column=col, padx=2, pady=2)
        except Exception as e:
            print(f"Fehler beim Laden des Bildes für {game_name}: {e}")
            # Fallback Button ohne Bild
            btn = ttk.Button(
                frame,
                text=game_name.replace("Pokémon ", ""),
                command=lambda g=game_name: self.select_game(g)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)

    # Gruppiere Spiele nach Generation
    def create_generation_buttons(self):
        """Erstellt alle Buttons, gruppiert nach Generation"""
        # Dictionary zum Zählen der Positionen pro Generation
        position_counter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

        for game_name, game_info in self.pokemon_games.items():
            gen = game_info["generation"]
            
            # Wähle den richtigen Frame basierend auf der Generation
            frame_name = f"gen{gen}_frame"
            frame = getattr(self, frame_name)
            
            # Berechne Position im Grid
            position = position_counter[gen]
            row = position // 3  # Maximal 3 Buttons pro Zeile
            col = position % 3
            
            # Erstelle den Button
            self.create_game_button(frame, game_name, row, col)
            
            # Erhöhe den Zähler für diese Generation
            position_counter[gen] += 1

    def run(self):
        """Startet die GUI-Anwendung"""
        self.root.mainloop()
