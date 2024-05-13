from flask import json

class HTMLGenerator:
    def __init__(self, json_data):
        self.json_data = json.loads(json_data)
        self.title = self.json_data.get("pageTitle", "Default Title")
        self.html = f'''
        <!DOCTYPE html>
        <html>
        <head>
        <title>{self.title}</title>
        <link href='https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css' rel='stylesheet'>
        <link href='../static/css/template-styles.css' rel='stylesheet'>
        </head>
        <body class='flex flex-col'>
        '''

    def generate_header(self):
        header = self.json_data.get("pageContent", {}).get("header", {})
        if header:
            header_text = header.get("text", "")
            text_color = header.get("textColor", "text-white")
            background_color = header.get("backgroundColor", "bg-gradient-to-r from-white to-black")
            self.html += f"<header class='{background_color} {text_color} text-center py-4'>{header_text}</header>\n"

    def generate_main_content(self):
        main_content = self.json_data.get("pageContent", {}).get("main", {})
        if main_content:
            articles = main_content.get("articles", [])
            for article in articles:
                section_title = article.get("sectionTitle", "")
                self.html += f"<h2 class='text-2xl font-semibold text-gray-800 mt-6'>{section_title}</h2>\n"
                section_content = article.get("sectionContent", [])
                layout = article.get("layout", "stacked")
                if layout == "flex":
                    self.html += "<div class='flex flex-wrap justify-center'>\n"
                for i, div_content in enumerate(section_content):
                    div_element_type = div_content.get("elementType", "")
                    text_color = div_content.get("textColor", "text-gray-800")
                    background_color = div_content.get("backgroundColor", "bg-white")
                    style = f"{text_color} {background_color}"
                    if div_element_type == "div":
                        div_content_text = div_content.get("content", "")
                        self.html += f"<{div_element_type} class='py-2 {style} {'mt-4' if layout == 'stacked' else 'mr-4'}'"
                        self.html += f">{div_content_text}</{div_element_type}>\n"
                    elif div_element_type == "img":
                        img_src = div_content.get("src", "")
                        img_alt = div_content.get("alt", "")
                        self.html += f"<{div_element_type} src='{img_src}' alt='{img_alt}' class='mt-4'>\n"
                if layout == "flex":
                    self.html += "</div>\n"

    def generate_footer(self):
        footer = self.json_data.get("pageContent", {}).get("footer", {})
        if footer:
            footer_text = footer.get("text", "")
            text_color = footer.get("textColor", "text-white")
            background_color = footer.get("backgroundColor", "bg-gray-800")
            self.html += f"<footer class='{background_color} {text_color} text-center py-4 mt-auto'>{footer_text}</footer>\n"

    def generate_html(self):
        self.generate_header()
        self.generate_main_content()
        self.generate_footer()
        self.html += "</body>\n</html>"
        return self.html

# Example usage:
json_data = '''
{
  "pageTitle": "Tytuł Strony",
  "pageContent": {
    "header": {
      "elementType": "header",
      "text": "Nagłówek",
      "textColor": "text-red-500",
      "backgroundColor": "bg-blue-200"
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
              "backgroundColor": "bg-green-200"
            },
            {
              "elementType": "div",
              "content": "Treść diva 2",
              "textColor": "text-blue-800",
              "backgroundColor": "bg-yellow-200"
            }
          ]
        },
        {
          "sectionTitle": "Sekcja 2",
          "layout": "stacked",
          "sectionContent": [
            {
              "elementType": "div",
              "content": "Treść diva 3",
              "textColor": "text-purple-800",
              "backgroundColor": "bg-indigo-200"
            },
            {
              "elementType": "div",
              "content": "Treść diva 4",
              "textColor": "text-gray-800",
              "backgroundColor": "bg-pink-200"
            }
          ]
        }
      ]
    },
    "footer": {
      "elementType": "footer",
      "text": "Stopka",
      "textColor": "text-white",
      "backgroundColor": "bg-gray-900"
    }
  }
}
'''

html_generator = HTMLGenerator(json_data)
print(html_generator.generate_html())
