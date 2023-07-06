<h1 align="center">Request Sender</h1>

<p align="center">
  <b>Do I have to explain this one?</b>
</p>

[![Maintainability](https://img.shields.io/codeclimate/maintainability/alexlostorto/requests-sender?style=for-the-badge&message=Code+Climate&labelColor=222222&logo=Code+Climate&logoColor=FFFFFF)](https://codeclimate.com/github/alexlostorto/requests-sender/maintainability)

The program sends requests quickly using Python's **Requests** library.

## ⚡ Quick setup

1. Clone the repo

```bash
git clone https://github.com/alexlostorto/requests-sender
```

2. Rename _example.json_ to _request.json_ and input request data.

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run main.py

```bash
python main.py
```

5. Star the repo 😄

## 📋 Example

This is an example of a _request.json_ file which contacts **API Ninja's** counter API and increments the counter by 1.

```json
{
    "url": "https://api.api-ninjas.com/v1/counter?id=<ID>&hit=true",
    "method": "GET",
    "headers": {"X-Api-Key": "<API-KEY>"},
    "data": {}
}
```

## 📜 Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
