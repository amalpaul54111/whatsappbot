This is python program that send a same message either an image with a caption or just a text message to numerous no of people.

## How to run

To run this program  follow the steps below:

Download the repository by clicking the download option In the beginning of the page

then extract the zip file 

open terminal or command line in the extracted folder

run 

```jsx
source venv/bin/activate
```

this will activate the virtual environment included inside the folder

then edit the [message.py](http://message.py) file and add your text message and replace the image.jpeg file with your image to be send.

Now the place the phone numbers inside the phoneno.csv file in the directory make sure to place only one phone number in on line and next one in next line

if you only have a text message to be send edit the [main.py](http://main.py) file in line no 29 replace with the following code

```python
	text(msg)
```

Now running the [main.py](http://main.py) file will open an chrome tab with whatsapp web now login with you phone and press enter key in the terminal to proceed. The bot will start sending the predefined message to the phone numbers specified in the phoneno.csv
