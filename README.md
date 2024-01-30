<h2>ReviewBot<h2>

ReviewBot is a Telegram bot designed to help users submit reviews and feedback in a structured manner. It utilizes the aiogram library for Telegram bot development and incorporates a state machine to guide users through the review submission process.

Features

Structured Review Process: The bot guides users through a step-by-step process to submit reviews, ensuring that all necessary information is collected.
Location Selection: Users can choose a location for their review from a predefined list.
Review Types: Users can select the type of review they want to submit, including template-based answers and custom text.
Image Support: Users can attach photos to their reviews, enhancing the feedback with visual content.
Getting Started

1. Clone the Repository:

```bash

git clone https://github.com/SerhiiL06/ReviewBot.git

```

2. Change work directory:

```bash

cd reviewbot

```

3. Run the bot using docker-compose:

```bash

docker-cumpose up

```

4. Search bot in Telegram:

```bash

@replyreviews_bot

```

<h2>API Service<h2>

Usage

Endpoints
Get a list of reviews:
Method: GET
Path: /reviews/
Parameters:
method: Filter by method (regular expression: optional).
location: Filter by location (regular expression: optional).

```bash

curl -X GET "http://localhost:8000/reviews/?method=GET&location=local"


```
