# Top 50 Films Web Scraper

This repository contains a Python script that scrapes film ranking data from an archived web page, stores it in a SQLite database, and exports it to a CSV file using `pandas`. The script focuses on extracting the top 50 most highly ranked films and demonstrates a simple end-to-end data pipeline using `BeautifulSoup`, `requests`, and `sqlite3`.

## 🧩 Features

- Scrapes the top 50 films from an archived webpage
- Extracts data including Average Rank, Film Title, and Year
- Stores scraped data in a Pandas DataFrame
- Saves data to a CSV file (`top_50_films.csv`)
- Stores data into a SQLite database table (`Top_50` in `Movies.db`)

## 📂 Project Structure

```
top-50-films-scraper/
│
├── script.py               # Main Python script
├── top_50_films.csv        # CSV file with scraped data (generated after running)
├── Movies.db               # SQLite database file (generated after running)
└── README.md               # This file
```

## 🛠️ Requirements

- Python 3.x
- pandas
- requests
- beautifulsoup4

Install the required libraries using:

```bash
pip install pandas requests beautifulsoup4
```

## 🚀 How to Run

Simply run the script:

```bash
python script.py
```

The script will:

1. Scrape the film data from the web archive.
2. Print the top 50 films to the console.
3. Save the data to `top_50_films.csv`.
4. Store the data in `Movies.db` under the table name `Top_50`.

## 🌐 Source

Data is scraped from the [Internet Archive version of EverybodyWiki](https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films).

## 📜 License

This project is licensed under the MIT License.
