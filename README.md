# laravel-locale-finder
Finding strings in PHP files that used Laravel's "*Using Translation Strings As Keys*" locale format and make a JSON output file.

## Example of usage
### With no JSON input file
1. Copy the Python file into your Laravel's `resources` folder
2. Run: `laravel_locale_finder.py views`

### With JSON input file
Use this if your JSON locale file already has some data.
1. Copy your JSON locale file into the `resources` folder
2. Copy the Python file into your Laravel's resources folder
3. Run: `laravel_locale_finder.py views YOUR_JSON_LOCALE_FILE.json`
4. The output file will be `YOUR_JSON_LOCALE_FILE.json.output`
5. Now you can beautify the result with online services
6. Copy the result to your original JSON locale file
7. Delete unused files
