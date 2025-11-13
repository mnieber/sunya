from app.utils.env import env

NOTION_API_KEY = env("NOTION_API_KEY")
NOTION_ROADMAPS_PAGE_ID = env(
    "NOTION_ROADMAPS_PAGE_ID", "2818bc0a4ead80138a68ef937a33850d"
)
# Bump this version to invalidate cached markdown files
ROADPLAN_MARKDOWN_VERSION = "1.0"
