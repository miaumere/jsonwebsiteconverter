# JSON -> website converter

This is a simple python script that converts a JSON to a website.
It is a simple way to create a website without having to write HTML code.
The script uses Flask to create the website. HTML code is generated from the JSON file.
Styles are added using Tailwind CSS.

## How to use

1. Clone the repository
2. Install the required packages

```bash
pip install
```

3. Run the script

```bash
python main.py
```

4. Open the website in your browser

```bash
http://127.0.0.1:5000/
```

## Example JSON

```json
{
  {
    "pageTitle": "Tytuł Strony",
    "pageContent": {
      "header": {
        "elementType": "header",
        "text": "Nagłówek",
        "textColor": "text-red-500",
        "backgroundColor": "bg-blue-200",
      },
      "main": {
        "elementType": "main",
        "articles": [
          {
            "sectionTitle": "Sekcja 1",
            "layout": "flex",
            "sectionContent": [
              {
                "elementType": "div",
                "content": "Treść diva 1",
                "textColor": "text-yellow-800",
                "backgroundColor": "bg-green-200",
              },
              {
                "elementType": "div",
                "content": "Treść diva 2",
                "textColor": "text-blue-800",
                "backgroundColor": "bg-yellow-200",
              },
            ],
          },
          {
            "sectionTitle": "Sekcja 2",
            "layout": "stacked",
            "sectionContent": [
              {
                "elementType": "div",
                "content": "Treść diva 3",
                "textColor": "text-purple-800",
                "backgroundColor": "bg-indigo-200",
              },
              {
                "elementType": "div",
                "content": "Treść diva 4",
                "textColor": "text-gray-800",
                "backgroundColor": "bg-pink-200",
              },
            ],
          },
        ],
      },
      "footer": {
        "elementType": "footer",
        "text": "Stopka",
        "textColor": "text-white",
        "backgroundColor": "bg-gray-900",
      },
    },
  };


```
