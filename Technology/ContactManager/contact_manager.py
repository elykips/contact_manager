class ContactManager:


	def __init__(self, name, phone_number,email_address,website,birth_day,linkedin_id):

		self.name = name
		self.phone_number = phone_number
		self.email_address = email_address
		self.website = website
		self.birth_day = birth_day
		self.linkedin_id = linkedin_id


	def __repr__(self):
		return """
		Name: {}
		Phone: {}
		Email: {}
		Website: {}
		Birthday: {}
		Linkedin: {}
		""".format(self.name, self.phone_number, self.email_address, self.website, self.birth_day, self.linkedin_id)

name = input("Enter your name")
phone_number = input("Enter phone number")
email_address = input("Enter Email Address")
website = input("Whats your website URL?")
birth_day = input("When is your Birthday?")
linkedin_id = input("Enter your linkedin ID")

ely= ContactManager(name,phone_number,email_address,website,birth_day,linkedin_id)
print(ely)


	
	
