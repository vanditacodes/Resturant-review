import pandas as pd  #imported pandas
import matplotlib.pyplot as plt   #imported matplotlib
from matplotlib.animation import FuncAnimation   # for animation purpose

# Swiggy data preparation
swiggy_data = {
    'restaurant_name': [
        'S-Cuba', 'The Cake Box', 'Siya Fast Food', 'Masaledar Kitchen',
        'The Parathas King', 'Kerala Cafe', 'Cafebility', 'The Chaat Walk',
        'World Cuisine', 'Sawadam'
    ],
    'rating': [2, 2.4, 2.5, 2.8, 2.9, 4.3, 4.4, 4.5, 4.7, 4.8]
}
df_swiggy = pd.DataFrame(swiggy_data)

# Zomato data preparation
zomato_data = {
    'restaurant_name': [
        'Barbeque Nation', 'Ming Garden Bakery', 'Baati Chokha', 'Holy Chopsticks',
        'Hari Villas', 'Pizza Popular', 'Biryani Blues', 'Pizza King',
        'Momo Squad', 'Kashi Buffet'
    ],
    'rating': [4.9, 4.8, 4.6, 4.5, 4.3, 2.5, 2.4, 2.3, 2.2, 2.1]
}
df_zomato = pd.DataFrame(zomato_data)

# Ensure the data is sorted for animation purposes so the columns will be animated
df_swiggy = df_swiggy.sort_values(by='rating')
df_zomato = df_zomato.sort_values(by='rating')

# Initialize the plot 12X8 inches
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
fig.subplots_adjust(wspace=0.5)  # Increase the width space between subplots

def init():
    # Initialize Swiggy plot
    ax1.clear()
    ax1.set_xlim(0.0, 5.0)
    ax1.set_xlabel('Rating')
    ax1.set_title('Swiggy Restaurant Ratings')
    ax1.barh(df_swiggy['restaurant_name'], [0] * len(df_swiggy), color='orange', height=0.6)

    # Initialize Zomato plot
    ax2.clear()
    ax2.set_xlim(0.0, 5.0)
    ax2.set_xlabel('Rating')
    ax2.set_title('Zomato Restaurant Ratings')
    ax2.barh(df_zomato['restaurant_name'], [0] * len(df_zomato), color='red', height=0.6)

def update(frame):
    # Update Swiggy plot
    ax1.clear()
    ax1.set_xlim(0.0, 5.0)
    ax1.set_xlabel('Rating')
    ax1.set_title('Swiggy Restaurant Ratings')
    ax1.barh(df_swiggy['restaurant_name'], df_swiggy['rating'] * (frame / len(df_swiggy)), color='orange', height=0.6)
    ax1.set_yticklabels(df_swiggy['restaurant_name'], fontsize=10)

    # Update Zomato plot
    ax2.clear()
    ax2.set_xlim(0.0, 5.0)
    ax2.set_xlabel('Rating')
    ax2.set_title('Zomato Restaurant Ratings')
    ax2.barh(df_zomato['restaurant_name'], df_zomato['rating'] * (frame / len(df_zomato)), color='red', height=0.6)
    ax2.set_yticklabels(df_zomato['restaurant_name'], fontsize=10)


# Create the animation
anim = FuncAnimation(fig, update, frames=len(df_swiggy) + 1, init_func=init, interval=200, repeat=False)

# Show the animation
plt.show()