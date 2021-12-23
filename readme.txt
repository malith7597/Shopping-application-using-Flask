A list of file names and brief descriptions of the submitted files

   .venv - virtual enviornment which built to compile the application.
	market- this folder contains all the files of the web application.
	   templates- this file contains all the web interfaces.following files are available under templates.
		base.html- this is the main html layout which is rendered in other pages.
		buy.html- this relates to the purchase products.
		home.html- this relates to the search query of products.
		show_product.html- this relates to display product attributes.
		update.html- this relates to replenish product quantity.
		market.html -this relates to display products which are avaialble in the market.

	__init__.py - this contains the flask app.
	forms.py- handles all the forms of the application.
	models.py- handles all the database tables of the application
	routes.py- handles all the urls which are generated in the application
  run.py- this reliable to run the application and app is imported to this file.	
  test.py- this file is reliable to handle all the unit tests created.


Instructions for setting up and executing the application

	1. Create virtual enviornment in python.can use following command in command prompt to create virtual enviornment.
		py -3 -m venv .venv
	2.select and activate virtual enviornment to compile application .
		ex: .venv/Scripts/Activate.ps1
	3. Import flask
		python -m pip install --upgrade pip 
		after this  command, python -m pip install flask/py -3 -m pip install flask

	4. Import Flask SQLALchemy
		py -3 -m pip install flask-SQLALchemy

	5. to Debug mode on 
		set FLASK_DEBUG=1

	6.to execute application python run.py can use.




Instructions for setting up and executing the unit tests.
	1. Create file called test.py and import following.

		from flask.typing import StatusCode
		from werkzeug.wrappers import response
		import os
		import unittest


	2. To execute the created file python test.py command can be used in command prompt.

JSON formats of the web service requests and responses

	In the application sqlite db stored market database in JSON format as key :value pairs.
		Ex: item=Item(id="1", name="I phone", price="500",quantity=500)
	data in the db can also accessed using its key values.
		Ex: {{item.id}}

Discussion of adopting advanced technologies (discussed below)


Message queue softwares are quite popular in the world , Among them IBM MQ can be identified as one of best message queuing software.The products that are included in the 
MQ family are IBM MQ, IBM MQ Advanced, IBM MQ Appliance, IBM MQ for z/OS, and IBM MQ on IBM Cloud. 
IBM MQ also has containerised deployment options.Apache Kafka, Amazon SQS are another two key message queue software which 
is considered best in the latest technology.Asynchronous messaging facilitates  for decoupling of different programs. 
The key usageof this is that the efficiency of one application will not be reduced down by dependency on 
another program. For example, if one program preprocess data to be analyzed by another program, without a message queue, 
the first program may be slowed down if the second takes long time to analyze the data. Message queue software allows the 
requests from the first program to sit in a queue so that it can continue performing.Some message queue software exists 
as part of a complex application or operating system and is used internally by those programs. In contrast, other message
queue software generates a communication network between multiple applications, sometimes across different end-to-end. 
In either case, message queue software documents messaging activity in case of system failure.
Message queue software options have some different features depending on what software and operating systems they work with, and whether or not they function with multiple programs. 
Despite this, some features that are endemic to message queue software.
Asynchronous Communications Protocol as described above, asynchronous communication protocol helps to keep the performance 
of two programs are executed simulatenously.
Message Encryption is another key area which is considered in the networking. Transferring data in plain text enhance the vulnerability of software.So message queue helps to protect data
form malicious access.Message storage, retrieval, and deletion is also important because destruction of hardware , may cause 
millions to a company. But message storage helps to keep the data.For organizations Permissions for users and software are important to keep the integrity of information.Data error reduction is another important
area in terms of computer science. So software like IBM MQ ensures the error reduction.Azure Scheduler,TIBCO Rendezvous,RabbitMQ.
IBM Cloud Pak for Integration,Google Cloud Pub/Sub are also another important message queing software which are largely used in the world.



