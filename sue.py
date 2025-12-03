#!/usr/bin/env python3
import json
import os
import time

from core.dispatcher import Dispatcher
from core.cognitive_rebuild import CognitiveRebuilder
from ui.dashboard import Dashboard
from feeds.rss_processor import RSSProcessor

CONFIG_PATH = os.path.join("config", "settings.json")
FEEDS_PATH = os.path.join("config", "feeds.json")


def load_json(path, default=None):
    if not os.path.exists(path):
        return default if default is not None else {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    settings = load_json(CONFIG_PATH, {})
    feeds_cfg = load_json(FEEDS_PATH, {})

    # ensure dirs
    os.makedirs("memory", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    os.makedirs("sandbox", exist_ok=True)
    os.makedirs("models", exist_ok=True)

    dispatcher = Dispatcher(settings=settings)
    dashboard = Dashboard(dispatcher=dispatcher, settings=settings)
    rebuilder = CognitiveRebuilder(settings=settings, dispatcher=dispatcher)
    rss = RSSProcessor(settings=settings, feeds_cfg=feeds_cfg, dispatcher=dispatcher)

    if settings.get("rss", {}).get("digest_on_start", True):
        try:
            rss.refresh_all_feeds()
            rss.generate_digest()
        except Exception as e:
            print(f"[SUE] RSS digest error on startup: {e}")

    dashboard.print_banner()
    input_mode = settings.get("input_mode", "text")

    while True:
        try:
            if input_mode == "text":
                user_input = dashboard.get_user_input()
            else:
                user_input = dashboard.get_user_input(prompt="(voice mode stub) > ")

            if not user_input:
                continue

            low = user_input.lower().strip()

            if low in {"exit", "quit", "bye"}:
                print("[SUE] Shutting down…")
                break

            if "good night" in low or "goodnight" in low:
                print("[SUE] Cognitive Rebuild Mode starting…")
                rebuilder.run_rebuild()
                continue

            if low.startswith("rss "):
                cmd = low.split(" ", 1)[1]
                if cmd == "refresh":
                    rss.refresh_all_feeds()
                    print("[SUE] RSS feeds refreshed.")
                    continue
                elif cmd == "digest":
                    rss.generate_digest()
                    continue

            if low.startswith("dev "):
                response = dispatcher.handle(user_input, channel="dev")
            else:
                response = dispatcher.handle(user_input, channel="user")

            dashboard.display_response(response)

        except KeyboardInterrupt:
            print("\n[SUE] Interrupted. Type 'exit' to quit next time.")
            break
        except Exception as e:
            print(f"[SUE] Error: {e}")
            time.sleep(0.5)


if __name__ == "__main__":
    main()
