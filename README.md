# Daygram2DayOneConverter
## Why
Convert Daygram diary data to format of DayOne diary.
It seems in the diary/journey application market, DayOne is the most popular choice. Many of the competitor apps provide the capability to import DayOne format data into their own repository. 

Daygram was my favorite diary on iOS in past years, but lack of a Desktop app sometimes made it a little inconvenient to use. Because anyway typing on computer's keyboard is way faster.

The purpose of this simple script is to convert exported Daygram to a DayOne JSON format. So diary data can be easily imported to popular diary apps. 


## How-to
1. Use Daygram's export capability to export. An email with exported content will be sent to your inbox. 
2. Open email account, find the Daygram export email. Copy the whole email body and paste to a text file.
3. Download this python script
4. Run command `python convert.py YOUR_DAYGRAM_EXPORT_FILE > dayone_data.json`
    * `dayone_data.json` will be the converted json file of DayOne format
5. Use your zip tool to create a zip file containing the json file
6. Done
