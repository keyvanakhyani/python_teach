# 📊 Price Tracker

A simple yet powerful price tracking tool for Digikala products. Track price changes, get alerts, and visualize price trends over time.

## 🎯 Project Goal

This is a **one-week learning project** designed to practice real-world freelance skills:
- Web scraping
- Database management
- Task scheduling
- API integration
- Data visualization

## ✨ Features

- 🔍 **Price Scraping**: Automatically fetch current product prices from Digikala
- 💾 **Data Storage**: Store price history in SQLite database
- ⏰ **Scheduled Tracking**: Run daily price checks automatically
- 📱 **Telegram Alerts**: Get notified when prices drop
- 📊 **Price Visualization**: Generate charts showing price trends
- 🖥️ **CLI Interface**: Easy-to-use command-line tool

## 🛠️ Tech Stack

- **Python 3.8+**
- **Requests** + **BeautifulSoup4** - Web scraping
- **SQLite** - Data storage
- **APScheduler** - Task scheduling
- **python-telegram-bot** - Telegram notifications
- **pandas** + **matplotlib** - Data analysis and visualization
- **Click** - CLI interface

## 📁 Project Structure

```
price-tracker/
├── scraper/
│   ├── __init__.py
│   └── digikala_scraper.py      # Scraping logic
├── database/
│   ├── __init__.py
│   └── db.py                     # Database operations
├── alerts/
│   ├── __init__.py
│   └── telegram_alert.py         # Telegram notifications
├── reports/
│   ├── __init__.py
│   └── visualizer.py             # Chart generation
├── tracker.py                    # Main tracking logic
├── cli.py                        # CLI interface
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/price-tracker.git
cd price-tracker
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env and add your Telegram bot token and chat ID
```

## 📖 Usage

### Track a Product
```bash
python cli.py track --url "https://www.digikala.com/product/dkp-xxxxx/"
```

### Start Scheduled Tracking
```bash
python cli.py start
```

### Generate Price Report
```bash
python cli.py report --product-id dkp-xxxxx
```

### View Price History
```bash
python cli.py history --product-id dkp-xxxxx
```

## ⚙️ Configuration

Create a `.env` file with the following variables:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
TRACKING_INTERVAL=24  # Hours between checks
PRICE_DROP_THRESHOLD=5  # Minimum % drop to trigger alert
```

## 📊 Example Output

```
Current Price: 12,500,000 Toman
Previous Price: 13,000,000 Toman
Drop: 500,000 Toman (3.8%)

✅ Alert sent to Telegram!
```

## 🗓️ Development Roadmap

- [x] Day 1: Basic scraping functionality
- [ ] Day 2: Database integration
- [ ] Day 3: Task scheduling
- [ ] Day 4: Telegram alerts
- [ ] Day 5: Data visualization
- [ ] Day 6: CLI interface
- [ ] Day 7: Documentation and polish

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by real freelance projects from Upwork and Parscoders
- Built as part of a practical learning journey
- Special thanks to the Python community for amazing libraries

## 📧 Contact


Project Link: [https://github.com/keyvanakhyani/price-tracker](https://github.com/keyvanakhyani/price-tracker)

---

**Note**: This tool is for educational purposes. Please respect Digikala's terms of service and implement appropriate rate limiting.