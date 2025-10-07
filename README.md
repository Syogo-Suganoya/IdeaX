[日本語版](https://github.com/Syogo-Suganoya/IdeaX/blob/main/README_ja.md)

# Complaint Busters - Idea Generation Tool to Address Complaints from X (Formerly Twitter) Trends

## Overview

**Complaint Busters** is a tool that extracts negative content from X (formerly Twitter) trends and posts, analyzes it with AI, and generates concrete service ideas to address the complaints. The generated ideas are output in the following formats:

- **Summary within 140 characters** (for X posts)
- **Campfire-style project proposal**
- **Qiita-style technical article**

Additionally, the tool can automatically post the generated ideas to X.

## Key Features

1. **Trend Retrieval**
   Fetch trends from X and extract negative trends (mock data can also be used).

2. **Sentiment Analysis**
   Analyze the content of trends and posts using AI to determine whether they are positive or negative.

3. **Idea Generation**
   Generate concrete service ideas to address complaints based on negative trends.

4. **Format Conversion**
   Convert the generated ideas into the following formats:
   - X post within 140 characters
   - Campfire-style project proposal
   - Qiita-style technical article

5. **Automatic Posting**
   Automatically post the generated content to X.

6. **File Output**
   Save the generated ideas to a specified directory.

## Technologies Used

- **Python**
  Used for the overall implementation of the program.
- **Tweepy**
  Utilized for accessing the X API to fetch trends and post updates.
- **Google GenAI**
  Uses the Gemini model for prompt-based generation.
- **dotenv**
  Manages environment variables.

## Requirements

- Python 3
- Python libraries:
  - `tweepy`
  - `google-genai`
  - `python-dotenv`

## Installation

1. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up environment variables. Create a `.env` file with the following content:

    ```env
    X_API_KEY="YOUR_X_API_KEY"
    X_API_KEY_SECRET="YOUR_X_API_KEY_SECRET"
    X_ACCESS_TOKEN="YOUR_X_ACCESS_TOKEN"
    X_ACCESS_TOKEN_SECRET="YOUR_X_ACCESS_TOKEN_SECRET"
    X_BEARER_TOKEN="YOUR_X_BEARER_TOKEN"
    GEMINI_KEY="YOUR_GEMINI_API_KEY"
    ```

## How to Run

1. To run with mock data:

    ```bash
    python src/main.py --mock
    ```

2. To run with the actual X API:

    ```bash
    python src/main.py
    ```

## File Structure

- `src/main.py`
  Main script that performs trend retrieval, sentiment analysis, idea generation, and posting.
- `src/lib/`
  Modules containing APIs and utility functions.
- `mock/`
  Stores mock data (trends and post content).
- `prompt/`
  Stores AI prompt templates.
- `output/`
  Directory for saving generated ideas.

## Notes

- Please comply with the X API terms of service.
- The generated ideas are not guaranteed to be realistic or appropriate. Review carefully before implementation.

## Challenges & Future Plans

- **X API Costs**
Currently, the cost of using the X API is high, making sufficient data collection difficult. This issue will be addressed once funding is secured through crowdfunding.
- **Trend Categorization**
Currently, each tweet is analyzed individually, but aggregating similar tweets could improve trend analysis accuracy.
In the future, prompts will be refined for proper categorization to enhance classification accuracy.
