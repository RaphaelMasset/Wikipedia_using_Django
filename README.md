# Wiki Encyclopedia Web App

A Django-based online encyclopedia where users can view, create, edit, and search entries. Each entry is stored in Markdown and rendered as HTML for display.

## Overview
- View encyclopedia entries by title.
- Search for entries by exact match or substring.
- Create new entries with a title and Markdown content.
- Edit existing entries; Markdown content pre-populated for easy updates.
- Navigate to a random entry.
- Markdown content is converted to HTML before display.

## Getting Started
1. Download and unzip the project distribution code.
2. Open a terminal and navigate to the project directory.
3. Run migrations for the `encyclopedia` app:
   ```bash
   python manage.py makemigrations encyclopedia
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Open your browser and visit `http://127.0.0.1:8000/` to use the encyclopedia.

## Usage
- Click on any entry from the index page to view its content.
- Use the search box to find entries by title or substring.
- Click “Create New Page” to add a new encyclopedia entry.
- Click “Edit” on any entry page to update the Markdown content.
- Click “Random Page” in the sidebar to navigate to a random entry.
- Markdown content supports headings, bold text, lists, links, and paragraphs.

## Project Structure
- `encyclopedia/`: Django app with models, views, URLs, and templates.
- `encyclopedia/util.py`: Provides functions to list, get, and save entries.
- `encyclopedia/templates/encyclopedia/`: HTML templates for layout, index, entry, and edit pages.
- `entries/`: Stores all encyclopedia entries as Markdown files.
- `manage.py`: Django ma
