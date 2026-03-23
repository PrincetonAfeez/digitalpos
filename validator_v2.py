#Validator for all user input
#Adding RegEx

import datetime
import re

def get_name(prompt):
    # Pattern: Allows letters, spaces, hyphens, and apostrophes.
    # Must start and end with a letter.
    name_regex = r"^[A-Za-z][A-Za-z\s\-\']+[A-Za-z]$"
    
    while True:
        # .title() automatically handles "ever flores" -> "Ever Flores"
        name = input(prompt).strip().title()
        
        if re.fullmatch(name_regex, name):
            return name
            
        print("❌ Error: Please enter a valid name (letters, hyphens, and apostrophes only).")
        

def get_email(prompt):
    # Pattern designed for standard email formats
    email_regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    
    while True:
        email = input(prompt).strip().lower()
        
        # re.fullmatch ensures the string follows the pattern from start to finish
        if re.fullmatch(email_regex, email):
            return email
            
        print("❌ Error: Please enter a valid email address (e.g., name@example.com).")

def get_int(prompt, min_val=None, max_val=None, exact_len=None, allow_zero=False):
    while True:
        val_str = input(prompt).strip()
        if not val_str:
            print("Error: This field cannot be empty.")
            continue
        try:
            val = int(val_str)
            if val == 0 and not allow_zero:
                print("Error: Value cannot be zero.")
                continue
            if val < 0:
                print("Error: Negative numbers are not allowed.")
                continue
            if exact_len and len(val_str) != exact_len:
                print(f"Error: Must be exactly {exact_len} digits.")
                continue
            if min_val is not None and val < min_val:
                print(f"Error: Minimum allowed is {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"Error: Maximum allowed is {max_val}.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid whole number.")

def get_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = float(input(prompt))
            if min_val is not None and val < min_val:
                print(f"    ❌ Error: Value must be at least {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"    ❌ Error: Value cannot exceed {max_val}.")
                continue
            return val
        except ValueError:
            print("    ❌ Invalid Input: Please enter a number (e.g., 7.5).")
            
def get_date(prompt):
    while True:
        raw_input = input(prompt).strip().lower() # Work in lowercase for cleaning
        if not raw_input:
            print("Error: Date is required.")
            continue

        # Clean suffixes (1st, 2nd, etc.)
        for suffix in ["st", "nd", "rd", "th"]:
            raw_input = raw_input.replace(suffix, "")

        formats = ["%B %d", "%b %d", "%m/%d", "%Y-%m-%d"]
        today = datetime.date.today()
        
        for fmt in formats:
            try:
                dt_obj = datetime.datetime.strptime(raw_input, fmt).date()
                if dt_obj.year == 1900:
                    dt_obj = dt_obj.replace(year=today.year)
                    if dt_obj < today:
                        dt_obj = dt_obj.replace(year=today.year + 1)
                return dt_obj
            except ValueError:
                continue
        print("Error: Use 'March 1st', '3/1', or 'YYYY-MM-DD'.")

def get_time(prompt, start_hour=None, end_hour=None):
    while True:
        t_str = input(prompt).strip().lower().replace(".", ":")
        if not t_str:
            print("Error: Time is required.")
            continue

        # Better digit handling: if they just type "11", make it "11:00"
        if t_str.isdigit():
            t_str += ":00"

        formats = ["%H:%M", "%I:%M%p", "%I%p", "%I:%M %p", "%I %p"]
        resy_time = None
        for fmt in formats:
            try:
                resy_time = datetime.datetime.strptime(t_str, fmt).time()
                break
            except ValueError:
                continue
        
        if resy_time:
            if start_hour is not None and resy_time.hour < start_hour:
                print(f"Error: We open at {start_hour}:00 AM.")
                continue
            if end_hour is not None and resy_time.hour >= end_hour:
                print(f"Error: Last reservation is at {end_hour}:00 PM.")
                continue
            return resy_time
            
        print("Error: Try '11am', '11:15', or '11.15'.")

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ['y', 'yes']: return True
        if ans in ['n', 'no']: return False
        print("Error: Please answer 'yes' or 'no'.")

def get_tip_logic(prompt, subtotal):
    """
    Special validator for POS systems. 
    Parses inputs like '10%' or '$10' and returns the float dollar amount.
    """
    while True:
        get_tip = input(prompt).strip()
        if not get_tip:
            print("Error: Tip is required. Enter 0 if no tip.")
            continue
        try:
            # Percentage logic
            if "%" in get_tip:
                val = float(get_tip.replace("%", ""))
                if val >= 0:
                    return subtotal * (val / 100)
            
            # Dollar logic
            elif "$" in get_tip:
                val = float(get_tip.replace("$", ""))
                if val >= 0:
                    return val
            
            print("Error: Please include % or $ (e.g., '15%' or '$5').")
        except ValueError:
            print("Error: Please enter a numeric value with % or $.")
