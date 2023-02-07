# AirBnB_clone
AirBnb clone project

## Description
This project is a clone of the famous airbnb rental booking site on the commandline.


### Installation
Clone this repository: git clone "https://github.com/Abinet508/AirBnB_clone.git"
Access AirBnb directory: cd AirBnB_clone
Run hbnb(interactively): ./console and enter command
Run hbnb(non-interactively): echo "" | ./console.py

This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)


Console and Command Usage
The console is a shell-like command line user interface provided by the python CmdModule.

Command	Example
Display commands help	(hbnb) help
Create object (prints its id)	(hbnb) create )
Destroy object	(hbnb) destroy or (hbnb) .destroy()
Show object	(hbnb) show or (hbnb) .show()
Show "all" objects or instances class	(hbnb) all or (hbnb) all
Run console	./console.py
Quit console	(hbnb)quit
Help command example


## Class Models Used
File	Description	Attributes
- base_model.py	The BaseModel class is inherited by	the other classes
- user.py	User class stores user info such as	email, password, first_name, last_name
- city.py	City class stores city specific information	state_id, name
- state.py	State class stores state information	name
- place.py	Place class stores full detailed outline of rental unit features	city_id, user_id, name, description,number_rooms,number_rooms, number_bathrooms, max_guest,
- price_by_night, latitude, longitude, amenity_ids
- review.py	Review class stores previous customer reviews	place_id, user_id, textand opinions	
- amenity.py	Amenity class stores highlighted amenity	name
information	

## Tests
The test for the classes are in the test_models folder.
