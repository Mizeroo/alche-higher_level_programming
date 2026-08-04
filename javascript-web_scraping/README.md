# javascript-web_scraping

This project covers basic file handling and web scraping/API requests in JavaScript (Node.js).

## Tasks

| File | Description |
|---|---|
| `0-readme.js` | Reads and prints the content of a file (utf-8), prints the error object if reading fails |
| `1-writeme.js` | Writes a string to a file (utf-8), prints the error object if writing fails |
| `2-statuscode.js` | Prints the status code of a GET request to a given URL |
| `3-starwars_title.js` | Prints the title of a Star Wars movie by episode ID, using the SWAPI |
| `4-starwars_count.js` | Prints the number of Star Wars movies featuring the character Wedge Antilles (ID 18) |
| `5-request_store.js` | Fetches a webpage and stores its body content in a file (utf-8) |
| `6-completed_tasks.js` | Prints the number of completed tasks per user ID from a todos API |

## Requirements

- Node.js
- The `request` npm module (for tasks 2-6)

Install dependencies:
```bash
npm init -y
npm install request
```

## Usage

Make the scripts executable:
```bash
chmod +x *.js
```

Run a script:
```bash
./0-readme.js myfile.txt
./1-writeme.js myfile.txt "Some text"
./2-statuscode.js https://example.com
./3-starwars_title.js 1
./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
./5-request_store.js http://loripsum.net/api output.txt
./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
```

## Author

Laetitia Mizero
