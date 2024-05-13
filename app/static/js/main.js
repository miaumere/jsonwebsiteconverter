const exampleJson = `
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

  `;

const isValidJson = (jsonString) => {
  try {
    JSON.parse(jsonString);
    return true;
  } catch (error) {
    return false;
  }
};

const form = document.querySelector("form");
const textArea = document.querySelector("#jsonDataRequest");
textArea.placeholder = exampleJson;

form.addEventListener("submit", (event) => {
  const jsonData = textArea.value;
  const isValid = isValidJson(jsonData);
  if (!isValid) {
    event.preventDefault();
    alert("Invalid JSON data");
  } else {
    form.submit();
  }
});
