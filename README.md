🔥 S.U.E. — Sentient Unified Entity
Local Autonomous AI Assistant (llama.cpp Edition)

by Jedi Security

S.U.E. is a fully local, privacy-first autonomous AI system built to run on llama.cpp, with:

Local LLM responses (GGUF models)

Local vector memory (llama.cpp embeddings)

JSON-based long-term memory

RSS intelligence ingestion

PDF document ingestion + indexing

Dev Mode with secure sandbox execution

Systemd autostart for persistent background operation

No cloud dependencies, no telemetry, no external calls

S.U.E. is engineered to run entirely offline on Ubuntu, Windows, Termux (Android), WSL, and low-power hardware.

🚀 Features
🧠 Local LLM Core (llama.cpp)

Runs any GGUF model you choose

Supports 3B–70B models (CPU or GPU-optional)

No PyTorch or transformers required

Zero CUDA requirement (even works on older GPUs)

📚 Vector Memory (llama.cpp embedding API)

Embeds & stores user interactions

Searches memory using cosine similarity

Fast, simple, structured JSON database

Memory grows over time

📰 RSS Intelligence Ingestion

Auto-refreshes RSS feeds

Summarizes headlines

Stores digests into long-term memory

📄 PDF Knowledge Ingestion

Extracts text from PDFs

Indexes every page as memory entries

Tagging support

💻 Dev Mode

Run shell commands in sandbox

Execute Python snippets safely

Perfect for OSINT, automation, scraping

🎨 Interactive CLI Dashboard

Rich console UI

Emotion-color reactions

Clean Matrix-style look

🔄 Cognitive Rebuild Mode

Cleans memory

Re-indexes logs

Ongoing self-maintenance

🔧 Autostarts at Boot

Full systemd service included

Automatic background operation

Crash recovery & restart

📁 Project Structure
SUE/
 ├── sue.py
 ├── install.sh
 ├── requirements.txt
 ├── config/
 │    ├── settings.json
 │    └── feeds.json
 ├── core/
 │    ├── dispatcher.py
 │    ├── memory_json.py
 │    ├── memory_vector.py
 │    ├── hallucination_filter.py
 │    ├── cognitive_rebuild.py
 ├── feeds/
 │    ├── rss_processor.py
 │    └── pdf_reader.py
 ├── ui/
 │    ├── dashboard.py
 │    └── emotion_engine.py
 ├── devmode/
 │    ├── executor.py
 │    └── sandbox.py
 └── models/
       ├── sue.gguf            (place your chat model here)
       └── embedding.gguf      (place embedding model here)

🛠️ Installation (Ubuntu)

Clone or unzip SUE, then run:

chmod +x install.sh
./install.sh


This installs:

Python dependencies

llama-cpp-python backend

Systemd service

Autostart + autorestart

⚙️ Running SUE
Start manually
python3 sue.py

Start as system service
sudo systemctl start sue

Stop
sudo systemctl stop sue

Restart
sudo systemctl restart sue

View live logs
journalctl -u sue -f

🧩 Model Setup

Place your GGUF models here:

models/sue.gguf
models/embedding.gguf

Recommended Models

Chat model: MythoMax-L2-13B-GGUF

Embedding model: nomic-embed-text-v1-GGUF or any embed-capable GGUF

🗂️ Configuring SUE
config/settings.json

Controls:

model paths

memory paths

RSS settings

TTS provider

DevMode options

Example:

{
  "model_path": "models/sue.gguf",
  "embedding_model": "models/embedding.gguf",
  "input_mode": "text",
  "rss": { "enabled": true, "digest_on_start": true }
}

config/feeds.json

Add or remove RSS feeds:

{
  "default_feeds": [
    "https://feeds.bbci.co.uk/news/rss.xml"
  ]
}

🧪 Dev Mode

Trigger DevMode with:

dev <command>


Shell example:

dev ls -la


Python example:

dev py x = 5; y = x * 10

💤 Cognitive Rebuild Mode

Trigger manually:

good night


SUE will:

compress memory

clean logs

set timestamp

rebuild index

🔒 Privacy & Security

SUE is:

Completely local

Never sends data out

Uses no external APIs

Stores all memory offline

Fully transparent

Open-source and auditable

🧘 Credits

Created by:
🛡️ Jedi Security
Built for autonomy, privacy, and raw capability.

❤️ License

MIT License — free to modify, expand, and redistribute.


