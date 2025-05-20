import pandas as pd
from pathlib import Path

def get_data(registery_path: Path) -> pd.DataFrame:
    return pd.read_excel(registery_path, sheet_name="Acces_Data")

def calculate_score(acces_df: pd.DataFrame) -> pd.DataFrame:
    acces_df["score"] = acces_df["nb_tentative"] / acces_df["nb_acces"]

def concurrence(acces_df: pd.DataFrame) -> dict:
    wanted_slots = []
    dict_slot = {}
    for list_slots in acces_df["date_visee"]:
        wanted_slots.expand(list_slots)
    dates = set(wanted_slots)
    for slot in dates.keys():
        dict_slot[slot] = acces_df.iloc[slot.isin(acces_df)]
    return dict_slot
