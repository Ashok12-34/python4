import matplotlib.pyplot as plt

companies = ["Apple", "Microsoft", "Google", "Amazon", "Facebook"]
market_share = [30, 25, 20, 15, 10]
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
explode = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(8, 8))
plt.pie(
    market_share,
    labels=companies,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    startangle=140,
    shadow=True
)

# Title
plt.title("Market Share of Technology Companies")

# Show plot
plt.show()
