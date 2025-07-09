name: ChatGPTPRReview

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Get PR diff
        id: diff
        run: |
          git fetch origin ${{ github.event.pull_request.base.ref }}
          git diff origin/${{ github.event.pull_request.base.ref }} > pr.diff

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.*

      - name: Install OpenAI Python SDK
        run: pip install openai

      - name: Run review with ChatGPT
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python review-pr.py < pr.diff

      - name: Comment on PR
        uses: marocchino/sticky-pull-request-comment@v2
        with:
          header: chatgpt-review
          message: |
             **ChatGPT Review Bot**:
            ```
            $(python review-pr.py < pr.diff)
            ```
