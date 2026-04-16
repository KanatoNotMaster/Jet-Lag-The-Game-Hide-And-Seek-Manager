import tkinter as tk
from tkinter import messagebox
import random
import time
import math

# --- STATION DATA ---
STATIONS = sorted([
    {"name": "Shing Mun River", "mc_x": 12534, "mc_z": -1797},
    {"name": "Eastern Industrial District", "mc_x": 12194, "mc_z": -1797},
    {"name": "Factory Street", "mc_x": 11892, "mc_z": -1827},
    {"name": "Northern Industrial District", "mc_x": 11586, "mc_z": -2082},
    {"name": "Green Island", "mc_x": 11887, "mc_z": -1387},
    {"name": "Airport", "mc_x": 12095, "mc_z": -633},
    {"name": "Tin Wah", "mc_x": 10877, "mc_z": -1492},
    {"name": "Lingping", "mc_x": 10719, "mc_z": -1811},
    {"name": "IKEA", "mc_x": 10601, "mc_z": -1327},
    {"name": "Tsun Yip Mall", "mc_x": 10641, "mc_z": -916},
    {"name": "Second Street Park", "mc_x": 10778, "mc_z": -825},
    {"name": "Third Street", "mc_x": 10778, "mc_z": -825},
    {"name": "SKH Lee Wing Him College", "mc_x": 10833, "mc_z": -438},
    {"name": "Tsun Yip Railway", "mc_x": 10595, "mc_z": -737},
    {"name": "Tsun Yip", "mc_x": 10434, "mc_z": -790},
    {"name": "Green Hill", "mc_x": 10203, "mc_z": -623},
    {"name": "Southern Hotel", "mc_x": 10067, "mc_z": -1083},
    {"name": "Southling Stadium", "mc_x": 10202, "mc_z": -1452},
    {"name": "Sai Sha Hospital", "mc_x": 9964, "mc_z": -1495},
    {"name": "Sai Sha", "mc_x": 9789, "mc_z": -1721},
    {"name": "Central Park", "mc_x": 10323, "mc_z": -1930},
    {"name": "Pak Sha", "mc_x": 9873, "mc_z": -2218},
    {"name": "Kamlong Bay", "mc_x": 10340, "mc_z": -2223},
    {"name": "Ting Kau", "mc_x": 10288, "mc_z": -2610},
    {"name": "Sham Tseng", "mc_x": 9875, "mc_z": -2656},
    {"name": "Kwai Chung", "mc_x": 10288, "mc_z": -3119},
    {"name": "Kwai Shing", "mc_x": 9863, "mc_z": -3129},
    {"name": "Man Kam To", "mc_x": 10103, "mc_z": -3332},
    {"name": "Nagashima Resort", "mc_x": 9243, "mc_z": -3165},
    {"name": "Greenfield", "mc_x": 5379, "mc_z": -2033},
    {"name": "Lannex", "mc_x": 4998, "mc_z": -1969},
    {"name": "Thorne", "mc_x": 5023, "mc_z": -3168},
    {"name": "Airport Cargo Centre", "mc_x": 4695, "mc_z": -2237},
    {"name": "LOHAS Town", "mc_x": 4996, "mc_z": -772},
    {"name": "Palma", "mc_x": 4913, "mc_z": 715},
    {"name": "South Palma", "mc_x": 5083, "mc_z": 1058},
    {"name": "Airport Garage", "mc_x": 4102, "mc_z": -1841},
    {"name": "Rio Pueblo", "mc_x": 4253, "mc_z": -1336},
    {"name": "Sumida River", "mc_x": 4213, "mc_z": -792},
    {"name": "Rio Pueblo-Downtown Highway", "mc_x": 4150, "mc_z": -488},
    {"name": "Los Llanos", "mc_x": 4150, "mc_z": -73},
    {"name": "Sonora River", "mc_x": 4165, "mc_z": 565},
    {"name": "Sonora", "mc_x": 4088, "mc_z": 525},
    {"name": "Rockwell Light Rail", "mc_x": 4042, "mc_z": 1453},
    {"name": "Rockwell", "mc_x": 4079, "mc_z": 1575},
    {"name": "Terminal 1", "mc_x": 3682, "mc_z": -1936},
    {"name": "Airport", "mc_x": 3529, "mc_z": -2000},
    {"name": "South Los Llanos", "mc_x": 3544, "mc_z": 525},
    {"name": "Nihonmachi", "mc_x": 3088, "mc_z": -801},
    {"name": "Lennox", "mc_x": 2899, "mc_z": 367},
    {"name": "Longport", "mc_x": 2647, "mc_z": 1345},
    {"name": "Longport Light Rail", "mc_x": 3069, "mc_z": 1288},
    {"name": "Whitestone East", "mc_x": 2413, "mc_z": -792},
    {"name": "Dawson Rail", "mc_x": 1743, "mc_z": 97},
    {"name": "Dawson", "mc_x": 1873, "mc_z": 226},
    {"name": "South Dawson", "mc_x": 1992, "mc_z": 590},
    {"name": "Longport Keys East", "mc_x": 1718, "mc_z": 1357},
    {"name": "Ngong Ping", "mc_x": 1566, "mc_z": -792},
    {"name": "Riverwood", "mc_x": 1288, "mc_z": 226},
    {"name": "Kennedy", "mc_x": 1205, "mc_z": 838},
    {"name": "Eagle-Point", "mc_x": 819, "mc_z": -476},
    {"name": "Georgetown", "mc_x": 886, "mc_z": 226},
    {"name": "Old Georgetown", "mc_x": 600, "mc_z": 229},
    {"name": "Sunnyside", "mc_x": 558, "mc_z": -2061},
    {"name": "Ashfield East Park", "mc_x": 544, "mc_z": -1736},
    {"name": "Ashfield East", "mc_x": 502, "mc_z": -1432},
    {"name": "Ashfield South", "mc_x": 544, "mc_z": -1255},
    {"name": "Downtown", "mc_x": 234, "mc_z": -586},
    {"name": "Southern Park", "mc_x": 275, "mc_z": -457},
    {"name": "Union", "mc_x": 342, "mc_z": -265},
    {"name": "Market Street", "mc_x": 345, "mc_z": -7},
    {"name": "Hunter’s point", "mc_x": 268, "mc_z": -17},
    {"name": "Retail Park", "mc_x": 262, "mc_z": 375},
    {"name": "Longport Keys West", "mc_x": 233, "mc_z": 1120},
    {"name": "Glewview", "mc_x": 58, "mc_z": -1841},
    {"name": "Ashfield Central", "mc_x": 79, "mc_z": -1200},
    {"name": "Ashfield Park", "mc_x": 104, "mc_z": -1034},
    {"name": "Bridge Street", "mc_x": -31, "mc_z": -224},
    {"name": "Hall Street", "mc_x": 53, "mc_z": 63},
    {"name": "Montaro Mall", "mc_x": 53, "mc_z": 365},
    {"name": "Genmar Stadium", "mc_x": -352, "mc_z": -1036},
    {"name": "Fort Franklin", "mc_x": -465, "mc_z": -196},
    {"name": "Wanking", "mc_x": -371, "mc_z": 224},
    {"name": "Olympia", "mc_x": -352, "mc_z": 454},
    {"name": "Clinton Light Rail", "mc_x": -646, "mc_z": -1199},
    {"name": "Clinton", "mc_x": -648, "mc_z": -902},
    {"name": "Franklin", "mc_x": -648, "mc_z": -443},
    {"name": "Deltapier", "mc_x": -839, "mc_z": 505},
    {"name": "Melrose", "mc_x": -1011, "mc_z": -2275},
    {"name": "Northpark", "mc_x": -1121, "mc_z": -1394},
    {"name": "Southpark", "mc_x": -1101, "mc_z": -1087},
    {"name": "Baron’s Bar", "mc_x": -1110, "mc_z": -94},
    {"name": "Melrose West", "mc_x": -1483, "mc_z": -1744},
    {"name": "Zetapier", "mc_x": -1641, "mc_z": 456},
    {"name": "Springfield", "mc_x": -2152, "mc_z": -1934},
    {"name": "Springfield Coliseum", "mc_x": -2488, "mc_z": -1951},
    {"name": "Ashfield West", "mc_x": -2774, "mc_z": -959},
    {"name": "Ashifield Industrial District", "mc_x": -1973, "mc_z": -959},
    {"name": "Westwood", "mc_x": -2181, "mc_z": -102},
    {"name": "Gammapier", "mc_x": -2240, "mc_z": 555},
    {"name": "Eagle Island", "mc_x": 477, "mc_z": -674},
    {"name": "Ralsewell", "mc_x": 714, "mc_z": -674},
    {"name": "Veteran Boulevard", "mc_x": 906, "mc_z": -236}
], key=lambda s: s["name"])

class TimerWindow:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title("LIVE GAME TIMER - SEEKER VIEW")
        self.top.geometry("600x400")
        self.top.configure(bg="black")
        self.top.attributes("-topmost", True)
        
        self.status_label = tk.Label(self.top, text="WAITING FOR HIDER", font=("Helvetica", 28, "bold"), fg="yellow", bg="black")
        self.status_label.pack(pady=30)
        
        self.time_label = tk.Label(self.top, text="00:00", font=("Helvetica", 100, "bold"), fg="white", bg="black")
        self.time_label.pack(pady=20)

        self.curse_frame = tk.Frame(self.top, bg="black")
        self.curse_frame.pack(fill="both", expand=True)
        self.active_curse_widgets = {} # Dict to track labels/timers
        self.top.protocol("WM_DELETE_WINDOW", lambda: None)

    def update_display(self, status, time_str, color="white"):
        self.status_label.config(text=status)
        self.time_label.config(text=time_str, fg=color)

class GreenfieldGame:
    def __init__(self, root):
        self.root = root
        self.root.title("HIDER CONTROL PANEL")
        self.root.geometry("500x700")

        self.game_phase = "IDLE"
        self.start_time = 0
        self.elapsed_time = 0
        self.pause_timestamp = 0
        self.countdown_seconds = 15 * 60
        self.hand = []
        self.max_hand_size = 6
        self.active_subwindow = None
        
        # Buff tracking state
        self.chalice_count = 0
        self.divine_blessing = False
        self.tiny_home_active = False
        
        self.card_data = self.initialize_card_data()
        self.deck = self.initialize_deck()
        self.timer_win = None
        self.timer_win = TimerWindow(self.root)

        self.setup_ui()

        self.root.protocol("WM_DELETE_WINDOW", lambda: None)

    def initialize_card_data(self):
        return {
            "Curse of the Jammed Door": {"desc": "For the next 15 minutes, whenever the Seekers want to pass through a doorway into a building, business, train, or other vehicle, they must first roll 2 dice. If they do not roll a 7 or higher, they cannot enter that space (including through other doorways.) Any given doorway can be re-attempted after 2.5 minutes. This curse cannot be casted in the endgame.", "cost_str": "Discard two cards", "cost_type": "any", "cost_val": 2},
            "Curse of the U-Turn": {"desc": "The seekers must disembark their current mode of transportation at the next station (as long as that station is serviced by another form of transit in the next 15mins.)", "cost_str": "Seekers must be heading the wrong way. (Their next station is further from you than they are.)", "cost_type": "special"},
            "Curse of the Drained Brain": {"desc": "Choose three questions in different categories. The seekers cannot ask those questions for the rest of your run.", "cost_str": "Discard you hard", "cost_type": "hand_all"},
            "Curse of the Bridge Troll": {"desc": "The seekers must ask their next question from under a bridge.", "cost_str": "Seekers must be at least 800 blocks from your hiding spot", "cost_type": "special"},
            "Curse of the Overflowing Chalice": {"desc": "For the next three questions, you may draw (not keep) an additional card when drawing from the hider deck.", "cost_str": "Discard a card", "cost_type": "any", "cost_val": 1},
            "Curse of The Open Mind": {"desc": "You no longer have a hand size limit.", "cost_str": "Discard your hand", "cost_type": "hand_all"},
            "Curse of the Glided Inquiry": {"desc": "Secretly choose one question. If the seekers ask that question after this curse is played, the question is automatically vetoed and you instantly draw and keep three extra cards.", "cost_str": "The seekers' next question is free", "cost_type": "special"},
            "Curse of the Hide-And-Seek-Ception": {"desc": "All seekers but one must close their eyes. Without discussion, the remaining seeker must go somewhere at least 150 blocks away and not within direct eyeshot in any direction. The other seekers must find them, without asking them for any information, before asking another question.", "cost_str": "The seekers must be off-transit, at least 150 blocks from a transit station.", "cost_type": "special"},
            "Curse of the Divine Blessing": {"desc": "For the rest of the round, keep all cards drawn. Hand size limit still applies.", "cost_str": "Discard 3 curses", "cost_type": "type", "cost_target": "Curse", "cost_val": 3},
            "Curse of the Untethered Spirit": {"desc": "You may move freely within your hiding zone during this round's endgame. The seekers are given a netherite sword and a permanent speed 4 effect and they have to kill you to end the round. You may not fight back. You must stay within your hiding zone in adventure mode once you casted the curse.", "cost_str": "You have to announce your transit station, and will be given a permanent glow effect.", "cost_type": "special"},
            "Curse of the Shark": {"desc": "For the next 15 minutes, the seekers are not allowed to stop walking for any reason.", "cost_str": "Discard a time bonus.", "cost_type": "time_bonus", "cost_val": 1},
            "Curse of the Trickster": {"desc": "You may lie-or provide a false photo- for one of the next three questions that the seekers ask. As always, you must send a photo of this curse when cast.", "cost_str": "Discard a curse.", "cost_type": "type", "cost_target": "Curse", "cost_val": 1},
            "Curse of the Blind Wanderer": {"desc": "Seekers must ask their next question at least 1000 blocks from where they are right now.", "cost_str": "Seekers must be at least 2000 blocks from your hiding spot", "cost_type": "special"},
            "Curse of the Plagued Word": {"desc": "For the next 30 minutes, asking a question creates a 250 blocks radius where questions cannot be asked until this curse expires.", "cost_str": "Seekers must be at least 1000 blocks from your hiding spot", "cost_type": "special"},
            "Curse of the Data Leak": {"desc": "For the rest of the run, seekers must tell you their route and destination every time they board any form of transit. They may not disembark at any other destination unless forced to.", "cost_str": "Discard 2 minutes worth of time bonuses", "cost_type": "time_val", "cost_val": 2},
            "Curse of the Soothsayer": {"desc": "For the rest of the round, you may choose to predict the next question after each question is asked. If you are right, you earn triple rewards. If you are wrong, you earn no reward.", "cost_str": "Discard a curse", "cost_type": "type", "cost_target": "Curse", "cost_val": 1},
            "Curse of the Chasm": {"desc": "For the next three questions that the seekers ask, they must roll a die. If they roll a 1, 2, 3, ог 4, that question is automatically randomized.", "cost_str": "Discard a randomize", "cost_type": "type", "cost_target": "Randomize", "cost_val": 1},
            "Curse of the Impenetrable Fog": {"desc": "For the next 30 minutes, any time the seekers reach a street intersection, they must assign each direction to a number on their die. They may assign a direction to multiple numbers, but each direction must be assigned to at least one. Then, they roll the die to see what direction to go.", "cost_str": "Roll a die. If it's odd, this curse has no effect", "cost_type": "special"},
            "Curse of the Void": {"desc": "For the next three questions that the seekers ask, roll a die. If you roll a 1, 2, 3, or 4, that question is automatically vetoed.", "cost_str": "Discard a veto.", "cost_type": "type", "cost_target": "Veto", "cost_val": 1},
            "Curse of the Freewheeler": {"desc": "The next three questions that the seekers ask must be asked while on a moving form of transit.", "cost_str": "Seekers must be at least 2000 blocks from you.", "cost_type": "special"},
            "Curse of the 1-Minute King": {"desc": "Remove all 1-minute bonuses from the deck for the rest of your run.", "cost_str": "Discard two 1-minute bonus cards.", "cost_type": "type", "cost_target": "1min", "cost_val": 2},
            "Curse of the Mind Meld": {"desc": "Without any discussion, on the count of three, any two seekers place any block on the bedrock at the same time. Assuming they're not the same word, they must wait 15 seconds, and on top of the previous block, both seekers place another block that they believe to be the midpoint between the last two words. You may not place any blocks that have already been placed, or do anything at all to indicate what block you will place next. Seekers may not ask another question until they both say the same word.", "cost_str": "Discard a card", "cost_type": "any", "cost_val": 1},
            "Curse of the Tiny Home": {"desc": "All time bonus cards held at the end of this round are worth 50% extra.", "cost_str": "The radius of your hiding zone is halved. This curse cannot be played during the endgame.", "cost_type": "special"},
            "Curse of the Rewind": {"desc": "Seekers must ask their next question from the exact place they asked their last question.", "cost_str": "The last question must have been asked during the endgame.", "cost_type": "special"},
            "Curse of the Express Route": {"desc": "Seekers cannot disembark any transit for the next 5 minutes, unless they've reached the end of a line.", "cost_str": "Discard at least 5 minutes worth of time bonuses", "cost_type": "time_val", "cost_val": 5},
            "Curse of the Sniper": {"desc": "Send the seekers a photo you've taken of them. Upon receiving this curse, they have 60 seconds to take a photo of you and end your run. If they fail, draw and keep five cards. You no longer have a maximum hand size.", "cost_str": "A photo of the seekers", "cost_type": "special"},
            "Discard 1 Draw 2": {"desc": "Discard one other card from your hand. Then, draw and keep two cards from the hider deck.", "cost_str": "Discard 1 card", "cost_type": "any", "cost_val": 1, "auto_draw": 2},
            "Discard 2 Draw 3": {"desc": "Discard two other cards from your hand. Then, draw and keep three cards from the hider deck.", "cost_str": "Discard 2 cards", "cost_type": "any", "cost_val": 2, "auto_draw": 3},
            "Draw 1 Expand 1": {"desc": "Draw one card from the hider deck. For the rest of the round, you can hold one additional card in your hand.", "cost_str": "None", "cost_type": "none", "auto_draw": 1, "expand": 1},
            "Draw 2 Expand 2": {"desc": "Draw two cards from the hider deck. For the rest of the round, you can hold two additional cards in your hand.", "cost_str": "None", "cost_type": "none", "auto_draw": 2, "expand": 2},
            "Duplicate": {"desc": "Play this card as a copy of any other card in your hand. This may be used to duplicate a time bonus at the end of your round.", "cost_str": "None", "cost_type": "duplicate"},
            "Randomize": {"desc": "Play instead of answering a question. A new unasked question from the same category is chosen, at random, which you answer instead.", "cost_str": "None", "cost_type": "none"},
            "Veto": {"desc": "Play instead of answering a question. No answer is given, and no reward is earned.", "cost_str": "None", "cost_type": "none"},
            "Discard Me": {"desc": "You can choose to discard this card to pay for the entirety of a curse's casting cost, so long as that card's casting cost involves discarding cards.", "cost_str": "None", "cost_type": "none"},
            "Move": {"desc": "Discard your hand and send the hiders the location of your transit station. This card grants a 5 minute period to establish a new hiding zone somewhere else on the game map. The seekers are frozen and your hiding timer is paused until this new hiding period has concluded. This card cannot be played during the endgame.", "cost_str": "Discard hand", "cost_type": "hand_all"},
        }

    def initialize_deck(self):
        curses = list(self.card_data.keys())[:26]
        power_ups = (["Discard 1 Draw 2"] * 4 + ["Discard 2 Draw 3"] * 4 + ["Draw 1 Expand 1"] * 2 + ["Draw 2 Expand 2"] * 1 +
                     ["Duplicate"] * 2 + ["Randomize"] * 4 + ["Veto"] * 4 + ["Discard Me"] * 2 + ["Move"] * 1)
        time_bonuses = (["1min"] * 25 + ["2min"] * 14 + ["3min"] * 11 + ["4min"] * 4 + ["6min"] * 2 + ["Total * 5%"] * 4)
        deck = curses + power_ups + time_bonuses
        random.shuffle(deck)
        return deck

    def setup_ui(self):
        self.local_status = tk.Label(self.root, text="SYSTEM READY", font=("Helvetica", 16, "bold"))
        self.local_status.pack(pady=20)
        self.start_btn = tk.Button(self.root, text="START HIDING (15m)", command=self.begin_hiding, bg="blue", fg="white", font=("bold", 12), height=3, width=30)
        self.start_btn.pack(pady=30)
        self.control_frame = tk.Frame(self.root)
        tk.Button(self.control_frame, text="DRAW CARDS", command=self.draw_menu, font=("bold", 11), width=25, height=2).pack(pady=10)
        tk.Button(self.control_frame, text="INSPECT HAND", command=self.inspect_hand, font=("bold", 11), width=25, height=2).pack(pady=10)
        tk.Button(self.control_frame, text="DISTANCE CALCULATOR", command=self.dist_cal, font=("bold", 11), width=25, height=2).pack(pady=10)
        tk.Button(self.control_frame, text="END GAME", command=self.confirm_end, bg="#8b0000", fg="white", font=("bold", 11), width=25, height=2).pack(pady=40)

    def manage_win(self, new_win):
        if self.active_subwindow and self.active_subwindow.winfo_exists():
            self.active_subwindow.destroy()
        self.active_subwindow = new_win

    def begin_hiding(self):
        self.game_phase = "HIDING"
        self.start_btn.destroy()
        self.skip_btn = tk.Button(self.root, text="SKIP HIDING PHASE", command=self.start_main_game, bg="orange", font=("bold", 10))
        self.skip_btn.pack(pady=10)
        self.update_loop()

    def start_main_game(self):
        if hasattr(self, 'skip_btn'): self.skip_btn.destroy()
        if hasattr(self, 'move_skip_btn'): self.move_skip_btn.destroy()
        if hasattr(self, 'move_btn'): self.move_btn.destroy()
        
        # New Pause/Resume Logic
        if self.game_phase == "PAUSED" or self.game_phase == "HIDING":
            if self.start_time == 0:
                self.start_time = time.time()
            else:
                # Adjust start_time to account for the time spent paused
                pause_duration = time.time() - self.pause_timestamp
                self.start_time += pause_duration
                
        self.game_phase = "RUNNING"
        self.control_frame.pack()

    def update_loop(self):
        if self.game_phase == "HIDING":
            self.countdown_seconds -= 1
            m, s = divmod(self.countdown_seconds, 60)
            self.timer_win.update_display("HIDER IS HIDING...", f"{m:02d}:{s:02d}", "yellow")
            self.local_status.config(text=f"HIDING TIME LEFT: {m:02d}:{s:02d}")
            if self.countdown_seconds <= 0: self.start_main_game()
        elif self.game_phase == "RUNNING":
            self.elapsed_time = time.time() - self.start_time
            hrs, rem = divmod(int(self.elapsed_time), 3600)
            m, s = divmod(rem, 60)
            time_display = f"{hrs:02d}:{m:02d}:{s:02d}" if hrs > 0 else f"{m:02d}:{s:02d}"
            self.timer_win.update_display("SEEKERS RELEASED!", time_display, "#ff4500")
            self.local_status.config(text=f"SURVIVAL TIMER: {time_display}")
        elif self.game_phase == "PAUSED":
            self.timer_win.update_display("TIMER PAUSED", "MOVE PHASE", "cyan")
            self.local_status.config(text="PAUSED: HIDER IS MOVING")
        self.root.after(1000, self.update_loop)

    def add_active_curse(self, name, type_mode, value=None):
        if not self.timer_win: return
        
        row = tk.Frame(self.timer_win.curse_frame, bg="black")
        row.pack(fill="x", padx=20)
        
        label = tk.Label(row, text=name, font=("Helvetica", 14), fg="red", bg="black")
        label.pack(side="left")

        if type_mode == "time":
            timer_label = tk.Label(row, text="", font=("Helvetica", 14, "bold"), fg="yellow", bg="black")
            timer_label.pack(side="right")
            self.run_curse_timer(name, value, timer_label, row)
        elif type_mode == "question":
            q_label = tk.Label(row, text=f"{value} left", font=("Helvetica", 14), fg="cyan", bg="black")
            q_label.pack(side="right")
            self.timer_win.active_curse_widgets[name] = {"label": q_label, "frame": row, "val": value}
        elif type_mode == "button":
            btn = tk.Button(row, text="CLEAR", command=row.destroy, bg="grey", fg="white", font=("Helvetica", 10))
            btn.pack(side="right")
        elif type_mode == "forever":
            pass # Name is already shown

    def run_curse_timer(self, name, seconds, label, frame):
        if seconds <= 0:
            frame.destroy()
            return
        m, s = divmod(seconds, 60)
        label.config(text=f"{m:02d}:{s:02d}")
        self.root.after(1000, lambda: self.run_curse_timer(name, seconds-1, label, frame))
 
    def draw_menu(self):
        win = tk.Toplevel(self.root); self.manage_win(win)
        tk.Label(win, text="Choose Draw Amount:", font=("bold", 12)).pack(pady=15)
        for i in [3, 2, 1]:
            tk.Button(win, text=f"DRAW {i} PICK 1", command=lambda n=i: self.perform_draw(n), width=20).pack(pady=5, padx=30)

    def perform_draw(self, count):
        if self.timer_win:
            # We use list() to create a copy of items so we can safely delete from the dict during the loop
            for c_name, data in list(self.timer_win.active_curse_widgets.items()):
                data["val"] -= 1  # Reduce the count
                
                if data["val"] <= 0:
                    # If it hits 0, remove the visual row from the seeker's screen
                    data["frame"].destroy()
                    del self.timer_win.active_curse_widgets[c_name]
                else:
                    # Otherwise, update the text to show the new count
                    data["label"].config(text=f"{data['val']} left")
        
        # 2. Specific mechanical buff for the Hider (drawing the extra card)
        if self.chalice_count > 0:
            count += 1
            self.chalice_count -= 1
            messagebox.showinfo("Chalice Active", f"Drawing an additional card! {self.chalice_count} uses remaining.")
        drawn = [self.deck.pop() for _ in range(count) if self.deck]
        
        # 3) Divine Blessing logic
        if self.divine_blessing:
            self.hand.extend(drawn)
            messagebox.showinfo("Divine Blessing", f"Kept all {len(drawn)} cards drawn!")
            self.check_limit()
        else:
            self.pick_screen(drawn)

    def pick_screen(self, pool):
        win = tk.Toplevel(self.root); self.manage_win(win)
        tk.Label(win, text="Select a Card to Inspect:", font=("bold", 11)).pack(pady=10)
        for card in pool:
            tk.Button(win, text=card, command=lambda c=card: self.inspect_card(c, pool)).pack(fill='x', padx=20, pady=2)

    def inspect_card(self, card_name, pool):
        win = tk.Toplevel(self.root); self.manage_win(win)
        data = self.card_data.get(card_name, {"desc": "Time Bonus", "cost_str": "None"})
        tk.Label(win, text=card_name, font=("bold", 15), fg="blue").pack(pady=10)
        tk.Label(win, text=f"CASTING COST: {data.get('cost_str', 'None')}", font=("bold", 10), fg="red").pack()
        tk.Label(win, text=f"INSTRUCTION:\n{data['desc']}", wraplength=450, justify="left").pack(pady=15, padx=20)
        
        def pick():
            pool.remove(card_name)
            self.deck.extend(pool); random.shuffle(self.deck)
            self.hand.append(card_name)
            win.destroy()
            if self.active_subwindow and self.active_subwindow.winfo_exists():
                self.active_subwindow.destroy()
            self.check_limit()
            
        tk.Button(win, text="CONFIRM PICK & KEEP", bg="green", fg="white", font=("bold", 11), command=pick).pack(pady=15)
        if len(pool) > 1:
            tk.Button(win, text="BACK TO CHOICES", command=lambda: self.pick_screen(pool)).pack()

    def check_limit(self):
        while len(self.hand) > self.max_hand_size:
            win = tk.Toplevel(self.root)
            tk.Label(win, text=f"HAND LIMIT ({len(self.hand)}/{self.max_hand_size}) - DISCARD ONE:").pack(pady=10)
            for i, c in enumerate(self.hand):
                tk.Button(win, text=c, command=lambda idx=i: [self.hand.pop(idx), win.destroy()]).pack(fill='x', padx=30, pady=2)
            self.root.wait_window(win)

    def inspect_hand(self):
        win = tk.Toplevel(self.root); self.manage_win(win)
        tk.Label(win, text=f"Your Hand ({len(self.hand)}/{self.max_hand_size if self.max_hand_size < 999 else '∞'})", font=("bold", 14), fg="green").pack(pady=10)
        if not self.hand: tk.Label(win, text="Hand is Empty").pack(pady=10)
        for i, card in enumerate(self.hand):
            tk.Button(win, text=card, command=lambda c=card, idx=i: self.detail_view(c, idx)).pack(fill='x', pady=2, padx=30)

    def update_station_menu(self, menu, variable, filter_text, station_names):
        menu['menu'].delete(0, 'end')
        filtered = [name for name in station_names if filter_text.lower() in name.lower()]
        if not filtered:
            filtered = ["No matches"]
        variable.set(filtered[0])
        for name in filtered:
            menu['menu'].add_command(label=name, command=tk._setit(variable, name))

    def dist_cal(self):
        win = tk.Toplevel(self.root)
        self.manage_win(win)
        win.title("Station Distance Calculator")

        station_names = [station["name"] for station in STATIONS]
        if len(station_names) < 2:
            tk.Label(win, text="Not enough station data available.").pack(pady=20)
            return

        start_search_var = tk.StringVar()
        end_search_var = tk.StringVar()
        start_var = tk.StringVar(value=station_names[0])
        end_var = tk.StringVar(value=station_names[1])

        tk.Label(win, text="Start station:", font=("bold", 12)).pack(pady=(15, 5))
        tk.Entry(win, textvariable=start_search_var).pack(padx=20, pady=(0, 5), fill='x')
        start_menu = tk.OptionMenu(win, start_var, *station_names)
        start_menu.pack(padx=20, pady=5, fill='x')

        tk.Label(win, text="End station:", font=("bold", 12)).pack(pady=(15, 5))
        tk.Entry(win, textvariable=end_search_var).pack(padx=20, pady=(0, 5), fill='x')
        end_menu = tk.OptionMenu(win, end_var, *station_names)
        end_menu.pack(padx=20, pady=5, fill='x')

        def refresh_start(*args):
            self.update_station_menu(start_menu, start_var, start_search_var.get(), station_names)

        def refresh_end(*args):
            self.update_station_menu(end_menu, end_var, end_search_var.get(), station_names)

        start_search_var.trace_add('write', refresh_start)
        end_search_var.trace_add('write', refresh_end)

        result_label = tk.Label(win, text="", font=("Helvetica", 12, "bold"), fg="white", bg="black")
        result_label.pack(pady=10, fill='x', padx=20)

        def calculate_distance():
            start_station = next((s for s in STATIONS if s["name"] == start_var.get()), None)
            end_station = next((s for s in STATIONS if s["name"] == end_var.get()), None)
            if not start_station or not end_station or start_var.get() == "No matches" or end_var.get() == "No matches":
                result_label.config(text="Please select two valid stations.", fg="orange")
                return
            dx = start_station["mc_x"] - end_station["mc_x"]
            dz = start_station["mc_z"] - end_station["mc_z"]
            dist = math.sqrt(dx * dx + dz * dz)
            if dist < 1000:
                color = "green"
            elif dist < 2000:
                color = "yellow"
            else:
                color = "red"
            result_label.config(text=f"{start_station['name']} → {end_station['name']}: {dist:.1f} blocks", fg=color)

        tk.Button(win, text="CALCULATE", command=calculate_distance, bg="blue", fg="white", font=("bold", 11)).pack(pady=10)
        tk.Button(win, text="CLOSE", command=win.destroy).pack(pady=(0, 20))

    def detail_view(self, card_name, index):
        win = tk.Toplevel(self.root); self.manage_win(win)
        data = self.card_data.get(card_name, {"desc": "Time Bonus", "cost_str": "None"})
        tk.Label(win, text=card_name, font=("bold", 15), fg="blue").pack(pady=10)
        tk.Label(win, text=f"CASTING COST: {data.get('cost_str', 'None')}", fg="red", font=("bold", 11)).pack()
        tk.Label(win, text=data['desc'], wraplength=450, justify="left").pack(pady=20, padx=20)
        
        if card_name in self.card_data:
            btn_text = "ACTIVATE DUPLICATE" if card_name == "Duplicate" else "CAST THIS CARD"
            tk.Button(win, text=btn_text, bg="orange", font=("bold", 11), command=lambda: self.handle_cast(card_name, index, win)).pack(pady=10)
        tk.Button(win, text="BACK", command=self.inspect_hand).pack()

    def handle_cast(self, card_name, index, win):
        data = self.card_data[card_name]
        cost_type = data.get("cost_type")
        items_to_remove = [index] 
        
        if cost_type == "hand_all":
            if messagebox.askyesno("Confirm", "Discard entire hand to cast?"):
                self.hand = []
                self.process_effect(card_name, data)
                win.destroy()
            return
        elif cost_type == "duplicate":
            selected_idx = self.duplicate_selector(index)
            if selected_idx is not None:
                self.hand[index] = self.hand[selected_idx]
                messagebox.showinfo("Duplicated", f"Duplicate card became: {self.hand[index]}")
                win.destroy()
                self.inspect_hand()
            return
        elif cost_type in ["any", "type", "time_bonus", "time_val"]:
            selected = self.discard_selector(card_name, index, cost_type, data)
            if selected is not None: items_to_remove.extend(selected)
            else: return 

        for i in sorted(list(set(items_to_remove)), reverse=True):
            self.hand.pop(i)
        
        self.process_effect(card_name, data)
        win.destroy()
        self.inspect_hand()

    def duplicate_selector(self, dup_idx):
        valid_indices = [i for i in range(len(self.hand)) if i != dup_idx]
        if not valid_indices:
            messagebox.showerror("Error", "No other cards in hand to duplicate!")
            return None
        sel_win = tk.Toplevel(self.root)
        tk.Label(sel_win, text="CHOOSE A CARD TO DUPLICATE:").pack(pady=10)
        selection = tk.IntVar(value=-1)
        def select(idx):
            selection.set(idx)
            sel_win.destroy()
        for i in valid_indices:
            tk.Button(sel_win, text=self.hand[i], command=lambda idx=i: select(idx)).pack(fill='x', padx=20, pady=2)
        self.root.wait_window(sel_win)
        return selection.get() if selection.get() != -1 else None

    def discard_selector(self, card_name, card_idx, cost_type, data):
        required = data.get("cost_val", 1)
        dm_idx = next((i for i, c in enumerate(self.hand) if c == "Discard Me"), None)
        if dm_idx is not None and dm_idx != card_idx and cost_type != "time_val":
            if messagebox.askyesno("Discard Me", "Use 'Discard Me' to pay the cost?"): return [dm_idx]
        chosen = []
        current_sum = 0
        while (current_sum < required if cost_type == "time_val" else len(chosen) < required):
            valid_indices = [i for i in range(len(self.hand)) if i != card_idx and i not in chosen]
            if cost_type == "type": valid_indices = [i for i in valid_indices if data["cost_target"] in self.hand[i]]
            elif cost_type == "time_bonus": valid_indices = [i for i in valid_indices if "min" in self.hand[i]]
            elif cost_type == "time_val": valid_indices = [i for i in valid_indices if "min" in self.hand[i]]
            if not valid_indices:
                messagebox.showerror("Error", "No more valid cards to discard!")
                return None
            sel_win = tk.Toplevel(self.root)
            needed = f"{required - current_sum} more mins" if cost_type == "time_val" else f"{required - len(chosen)} more cards"
            tk.Label(sel_win, text=f"SELECT ONE CARD TO DISCARD ({needed}):").pack(pady=10)
            selection_made = tk.BooleanVar(value=False)
            def select(idx):
                nonlocal current_sum
                chosen.append(idx)
                if cost_type == "time_val":
                    val = self.hand[idx].replace("min","").strip()
                    current_sum += int(val) if val.isdigit() else 0
                selection_made.set(True)
                sel_win.destroy()
            for i in valid_indices:
                tk.Button(sel_win, text=self.hand[i], command=lambda idx=i: select(idx)).pack(fill='x', padx=20, pady=2)
            self.root.wait_window(sel_win)
            if not selection_made.get(): return None
        return chosen

    def process_effect(self, card_name, data):
        # 1) 1-Minute King Logic
        if card_name == "Curse of the 1-Minute King":
            self.deck = [c for c in self.deck if c != "1min"]
            messagebox.showinfo("1-Minute King", "All 1min cards have been removed from the deck!")

        # 2) Overflowing Chalice logic (Sets counter for 3 draws)
        if card_name == "Curse of the Overflowing Chalice":
            self.chalice_count = 3

        # 3) Divine Blessing logic
        if card_name == "Curse of the Divine Blessing":
            self.divine_blessing = True

        # 4) Tiny Home logic
        if card_name == "Curse of the Tiny Home":
            self.tiny_home_active = True

        # 5) Sniper logic
        if card_name == "Curse of the Sniper":
            messagebox.showinfo("SNIPER", "Seekers have 60 seconds! If you survive, you get infinite hand size and 5 cards.")
            self.root.after(60000, self.apply_sniper_reward)

        if card_name == "Curse of The Open Mind":
            self.max_hand_size = 999
            messagebox.showinfo("Limit Removed", "Your hand size limit has been removed!")

        if "auto_draw" in data:
            for _ in range(data["auto_draw"]):
                if self.deck: self.hand.append(self.deck.pop())
            messagebox.showinfo("Auto Draw", f"{data['auto_draw']} cards added directly to your hand.")
            self.check_limit()
        
        if "expand" in data: self.max_hand_size += data["expand"]
        
        if card_name == "Move":
            self.game_phase = "PAUSED"
            self.pause_timestamp = time.time()
            self.control_frame.pack_forget()
            self.move_btn = tk.Button(self.root, text="START 5m RELOCATION", bg="cyan", command=self.start_move_timer)
            self.move_btn.pack(pady=40)
            self.move_skip_btn = tk.Button(self.root, text="SKIP MOVE RELOCATION", bg="orange", command=self.start_main_game)
            self.move_skip_btn.pack(pady=5)

        curse_mapping = {
            # Category A: Time
            "Curse of the Jammed Door": ("time", 15*60), "Curse of the Shark": ("time", 15*60),
            "Curse of the Plagued Word": ("time", 30*60), "Curse of the Impenetrable Fog": ("time", 30*60),
            "Curse of the Express Route": ("time", 5*60), "Curse of the Sniper": ("time", 60),
            # Category B: Question
            "Curse of the Overflowing Chalice": ("question", 3), "Curse of the Trickster": ("question", 3),
            "Curse of the Blind Wanderer": ("question", 1), "Curse of the Chasm": ("question", 3),
            "Curse of the Void": ("question", 3), "Curse of the Freewheeler": ("question", 3),
            "Curse of the Rewind": ("question", 1),
            # Category C: Button
            "Curse of the U-Turn": ("button", None), "Curse of the Bridge Troll": ("button", None),
            "Curse of the Glided Inquiry": ("button", None), "Curse of the Hide-And-Seek-Ception": ("button", None),
            "Curse of the Mind Meld": ("button", None),
            # Category D: Forever
            "Curse of the Drained Brain": ("forever", None), "Curse of The Open Mind": ("forever", None),
            "Curse of the Divine Blessing": ("forever", None), "Curse of the Untethered Spirit": ("forever", None),
            "Curse of the Data Leak": ("forever", None), "Curse of the Soothsayer": ("forever", None),
            "Curse of the 1-Minute King": ("forever", None), "Curse of the Tiny Home": ("forever", None)
        }
        
        if card_name in curse_mapping:
            mode, val = curse_mapping[card_name]
            self.add_active_curse(card_name.replace("Curse of the ", ""), mode, val)

        messagebox.showinfo("Casted", f"{card_name} activated!")

    def apply_sniper_reward(self):
        # Only reward if the game is still running
        if self.game_phase == "RUNNING":
            self.max_hand_size = 999
            for _ in range(5):
                if self.deck: self.hand.append(self.deck.pop())
            messagebox.showinfo("Sniper Survival", "You survived! Hand size is now infinite and 5 cards were added.")
            self.check_limit()

    def start_move_timer(self):
        self.move_btn.destroy()
        self.countdown_seconds = 5 * 60
        self.game_phase = "HIDING"

    def confirm_end(self):
        if messagebox.askyesno("END GAME", "Confirm and calculate final survival time?"):
            self.game_phase = "IDLE"
            bonus_mins = sum([int(c.replace("min","")) for c in self.hand if "min" in c and c.replace("min","").isdigit()])
            
            # 4) Tiny Home bonus calculation
            if self.tiny_home_active:
                bonus_mins *= 1.5
                
            mult = sum([0.05 for c in self.hand if "5%" in c])
            base_total = self.elapsed_time + (bonus_mins * 60)
            final_time = base_total * (1 + mult)
            def fmt(seconds):
                h, r = divmod(int(seconds), 3600)
                m, s = divmod(r, 60)
                if h > 0:
                    return f"{h}h {m}m {s}s"
                else:
                    return f"{m}m {s}s"

            results = (f"--- GAME OVER ---\n\n"
                      f"Original Hiding Time: {fmt(self.elapsed_time)}\n"
                      f"Total Bonus Time: {fmt(bonus_mins * 60)}\n"
                      f"Percentage Multiplier: +{int(mult*100)}%\n\n"
                      f"FINAL SURVIVAL TIME: {fmt(final_time)}")
            messagebox.showinfo("FINAL RESULTS", results)
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    GreenfieldGame(root)
    root.mainloop()