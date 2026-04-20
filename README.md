# Atlas — Personal Travel Memory Bot

Send a link, screenshot, or place name to @Atlas_arise_bot on Telegram. Atlas extracts, enriches, and saves it.

## Deploy to Railway (no terminal needed)

### Step 1 — Fork this repo
Click the **Fork** button (top right on GitHub). This copies the code to your account.

### Step 2 — Create a Railway project
1. Go to [railway.app](https://railway.app) and sign in with GitHub
2. Click **New Project**
3. Click **Deploy from GitHub repo**
4. Select your forked `atlas-arise-bot` repo
5. Railway will start deploying automatically

### Step 3 — Add environment variables
In Railway, click your project → **Variables** tab → add these two:

| Variable | Value |
|----------|-------|
| `TELEGRAM_BOT_TOKEN` | Your token from @BotFather |
| `ANTHROPIC_API_KEY` | Your key from console.anthropic.com |

Click **Deploy** after adding variables.

### Step 4 — Open Telegram
Search `@Atlas_arise_bot` and send `/start`. Atlas is live.

## Commands
- `/start` — wake Atlas
- `/list` — all saved places
- `/plan [place]` — trip plan
- `/delete [place]` — remove a place
- `/trek` `/observatory` `/nature` `/culture` `/food` `/place` — filter by type
- `/map` — link to your Wanderlist map

## What you can send
- Instagram reel screenshot
- YouTube link
- Any article or blog URL
- Plain text ("Kedarkantha winter trek")
- Forwarded messages

## Cost
- Telegram bot: free
- Railway hosting: free tier
- Anthropic API: ~$0.01–0.02/day of casual use
