# -------------------------------------------------------------
# Clinical Ward Automation & IV Drip Monitoring System
# Focus: while loops, nested for loops, and range() functions
# -------------------------------------------------------------

def monitor_iv_drip(volume_ml):
    """Simulates an IV fluid drip countdown using a while loop."""
    print(f"--- 🏥 STARTING IV DRIP MONITOR (Target: {volume_ml}ml) ---")
    while volume_ml > 0:
        print(f"[STATUS] IV Fluid remaining: {volume_ml}ml. Patient is stable.")
        volume_ml -= 100  # Fluid drops by 100ml per cycle
    print("[ALERT] IV Drip Empty! Nurse intervention required immediately.\n")

def generate_ward_roster(total_wards, beds_per_ward):
    """Generates a daily doctor round schedule using nested for loops."""
    print("--- 📋 GENERATING DAILY CLINICAL ROSTER ---")
    for ward in range(1, total_wards + 1):
        print(f"\nEntering Ward {ward}...")
        for bed in range(1, beds_per_ward + 1):
            print(f"  -> Checkup Scheduled: Ward {ward} - Bed {bed}")
    print("\n[SUCCESS] Roster Generation Complete!\n")

# --- Execution ---
# 1. Simulate an IV drip of 400ml
monitor_iv_drip(400)

# 2. Generate a roster for 2 Wards, each having 3 Beds
generate_ward_roster(2, 3)