import os
from datetime import datetime
import gifos

# Font setup
FONT_FILE_BITMAP = "./gohufont-uni-14.pil"
FONT_FILE_LOGO = "./IosevkaTermNerdFont-Bold.ttf"

def main():
    # REVERTED: Back to original 520px height
    # width=750, height=520 | Solid Dark Background
    t = gifos.Terminal(750, 520, 15, 15, FONT_FILE_BITMAP, 15)
    
    # 1. STARTUP: 1 second delay
    t.gen_text("", 1, count=15) 
    t.toggle_show_cursor(False)
    
    # --- PHASE 1: MODULAR BIOS ---
    year_now = datetime.now().strftime("%Y")
    t.gen_text("SHREYO_OS Modular BIOS v1.0.11", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[31mShreyan Softwares Inc.\x1b[0m", 2)
    t.gen_text("\x1b[94mKrypton(tm) GIFCPU - 500Hz\x1b[0m", 4)
    t.gen_text("Memory Test: 131072KB OK", 6)
    
    for i in range(0, 131073, 32768):
        t.delete_row(7)
        t.gen_text(f"Memory Test: {i} KB", 7, count=1, contin=True)
    t.delete_row(7)
    
    # BIOS PAUSE: 1 Second
    t.gen_text("Memory Test: 131072KB OK", 7, count=15, contin=True)
    t.clear_frame()

    # --- PHASE 2: CENTERED FAST GLITCH ---
    t.gen_text("Initiating Boot Sequence...", 1)
    
    # Original Logo Design
    t.set_font(FONT_FILE_LOGO, 45)
    os_logo_text = "SHREYO OS"
    
    mid_row = (t.num_rows // 2)
    mid_col = (t.num_cols - len(os_logo_text)) // 2
    
    effect_lines = gifos.effects.text_scramble_effect_lines(os_logo_text, 5, include_special=True)
    for line in effect_lines:
        t.delete_row(mid_row)
        t.gen_text(f"\x1b[1;96m{line}\x1b[0m", mid_row, mid_col)

    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()

    # --- PHASE 3: SECURE LOGIN ---
    t.gen_text("\x1b[93mshreyyyan@gifos v1.0.11 (tty1)\x1b[0m", 1, count=2)
    t.gen_text("login: ", 3)
    t.toggle_show_cursor(True)
    
    t.gen_typing_text("shreyyyan", 3, contin=True)
    # LOGIN PAUSE: 1 Second
    t.clone_frame(15) 
    
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4)
    t.toggle_show_cursor(True)
    
    t.gen_typing_text("*********", 4, contin=True)
    # PASSWORD PAUSE: 1 Second
    t.clone_frame(15)
    
    t.clear_frame()

    # --- PHASE 4: NEOFETCH ---
    user_age = gifos.utils.calc_age(5, 11, 2006)
    
    total_stars, total_commits, rank_level = 0, 0, "B"
    try:
        git_stats = gifos.utils.fetch_github_stats("shreyyyan")
        total_stars = git_stats.total_stargazers
        total_commits = git_stats.total_commits_last_year
        rank_level = git_stats.user_rank.level
    except Exception:
        pass

    t.gen_text("shreyyyan@gifos ~> fetch_details.sh -u shreyyyan", 1)
    
    # EXACT ASCII ART PROVIDED (Dashed Version)
    ascii_art = r"""
______________________________________________________________________________________________________________________________
                   ██████████
                  ████████████
                  ██        ██
                  ██▄▄▄▄▄▄▄▄▄█
                  ██▀███ ███▀█
    █             ▀█        █▀
    ██                  █
    ██              ██
    ██            ████ ██  ████
     ████████████████  ██  ██████
        █████████████  ██  █████████
                 ████  ██ █████  ███
                  ███  ██ █████  ███
                  ███     █████████
                  ██      ████████▀
                    ██████████
                    ██████████
                     ████████
                      ██████████▄▄
                        █████████▀
                         ████  ███
                         ████▄  ██
                        ██████   ▀
                        ▀▄▄▄▄▀
    """
    
    info_lines = [
        "",
        f"\x1b[30;101m shreyyyan@GitHub \x1b[0m",
        "------------------",
        f"\x1b[96mOS:         \x1b[0m Windows 11, iOS, Kali Linux",
        f"\x1b[96mLocation:   \x1b[0m Sunsari, Nepal",
        f"\x1b[96mKernel:     \x1b[0m Computer Science & Information Technology",
        f"\x1b[96mUptime:     \x1b[0m {user_age.years} years, {user_age.months} months, {user_age.days} days",
        f"\x1b[96mIDE:        \x1b[0m VS Code, Cursor, Antigravity",
        "",
        f"\x1b[30;101m Contact: \x1b[0m",
        "------------------",
        f"\x1b[96mEmail:      \x1b[0m shreyandahal26@gmail.com",
        f"\x1b[96mInstagram:  \x1b[0m @shreyyyan",
        f"\x1b[96mLinkedIn:   \x1b[0m shreyan-dahal-6a88b2329",
        f"\x1b[96mWebsite:    \x1b[0m shreyandahal.com.np",
        "",
        f"\x1b[30;101m GitHub Stats: \x1b[0m",
        "------------------",
        f"\x1b[96mTotal Stars:\x1b[0m {total_stars}",
        f"\x1b[96mCommits:    \x1b[0m {total_commits}",
        f"\x1b[96mUser Rating:\x1b[0m {rank_level}",
    ]

    art_split = ascii_art.strip().split("\n")
    
    # MOVED UP: Starting at Row 2 to fit everything in 520px height
    start_row = 2
    
    # Loop max lines
    for i in range(max(len(art_split), len(info_lines))):
        current_row = start_row + i
        
        # 1. Draw ASCII Art: TrueType Font (Green)
        # REDUCED SIZE: Set to 11 to fit vertically without crashing
        if i < len(art_split):
            t.set_font(FONT_FILE_LOGO, 11) 
            t.gen_text(f"\x1b[92m{art_split[i]}\x1b[0m", current_row, col_num=1, count=0)
        
        # 2. Draw Text Details: Bitmap Font (Standard Size 15)
        if i < len(info_lines):
            t.set_font(FONT_FILE_BITMAP, 15) 
            t.gen_text(info_lines[i], current_row, col_num=38, count=1, contin=True)
        else:
            t.set_font(FONT_FILE_BITMAP, 15)
            t.gen_text("", current_row, col_num=38, count=1, contin=True)

    t.clone_frame(15)

    # --- PHASE 5: FINAL MESSAGE (Right Side, Bottom) ---
    # Calculated to be exactly 2 rows below the info text
    final_row = start_row + len(info_lines) + 1 # Row 23/24 approx
    
    # Force initialize the row to prevent crash
    t.gen_text(" ", final_row, col_num=38)
    
    # Type message aligned with the text block (col 38)
    t.gen_typing_text("\x1b[92m#Have a great day! Watching you from here \x1b[0m", final_row, col_num=38, contin=True)

    t.clone_frame(120) 
    t.gen_gif()

if __name__ == "__main__":
    main()
