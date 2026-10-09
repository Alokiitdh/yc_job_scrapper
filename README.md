# YC Job Scrapper

A simple command-line Python tool that scrapes [Hacker News](https://news.ycombinator.com/) (YCombinator's news board) and surfaces the most popular stories — filtered by score and sorted by votes.

## Features

- Scrapes one or more pages of Hacker News front-page stories
- Filters out stories with **fewer than 100 points**
- Returns results **sorted by score** (highest first)
- Displays the title, URL, and score of each qualifying story

## How It Works

1. Prompts the user to enter the number of pages to scrape
2. Iterates through the specified pages of `https://news.ycombinator.com/?p=<N>` using `requests`
3. Parses the HTML with `BeautifulSoup` to extract story titles, links, and vote scores
4. Filters stories with `score > 99` and sorts them in descending order
5. Pretty-prints the final list along with the total count

## Project Structure

```
yc_job_scrapper/
├── main.py          # Core scraping logic and entry point
├── pyproject.toml   # Project metadata and dependencies
├── uv.lock          # Locked dependency versions
└── README.md
```

## Requirements

- Python >= 3.13
- [requests](https://pypi.org/project/requests/) >= 2.34.2
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) >= 4.15.0

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repository
git clone <repo-url>
cd yc_job_scrapper

# Create a virtual environment and install dependencies
uv sync
```

Alternatively, install manually with pip:

```bash
pip install requests beautifulsoup4
```

## Usage

```bash
python main.py
```

You will be prompted to enter the number of pages to scrape:

```
How many pages do you want to scrape? 3
```

### Example Output

```python
[{'Links': 'https://example.com/article',
  'Score': 512,
  'Title': 'Some Viral Tech Article'},
 {'Links': 'https://another.com/post',
  'Score': 234,
  'Title': 'Another Popular Story'},
 ...]

Total stories with >99 points found: 12
```

## Dependencies

| Package         | Version  | Purpose                        |
|-----------------|----------|--------------------------------|
| requests        | ≥ 2.34.2 | HTTP requests to Hacker News   |
| beautifulsoup4  | ≥ 4.15.0 | HTML parsing and data extraction |
