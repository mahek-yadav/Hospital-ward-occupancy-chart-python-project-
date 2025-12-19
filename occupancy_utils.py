import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Decorator for logging every occupancy update
def log_update(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        ward = args[0]
        with open("ward_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {ward.name} updated: {func.__name__}\n")
        return result
    return wrapper


# Load wards from CSV
def load_wards(file_path='wards.csv'):
    return pd.read_csv(file_path)


# Save updated ward info to CSV
def save_wards(df, file_path='wards.csv'):
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")


# Plot ward occupancy bar chart
def plot_occupancy(df):
    plt.bar(df['name'], df['occupied_beds'], color='skyblue')
    plt.xlabel('Ward Name')
    plt.ylabel('Occupied Beds')
    plt.title('Hospital Ward Occupancy Chart')
    plt.show()
