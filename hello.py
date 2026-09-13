class DataValidator:
    def __init__(self):
        
        self.errors = []
    
    def validate_emails(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid Email:{email}")
            return False
        return True

    def validate_age(self, age):
        if age<0 or age > 150:
            self.errors.append(f"Invalid Age : {age}")
            return False
        return True

    def get_errors(self):
        return self.errors

class IdentityValidator(DataValidator):
    def validate_identity(self, name ):
        if "int" in name:
            self.errors.append(f"Invalid Name : {name}")
            return False    
        return True



invalidator = IdentityValidator()
validator = DataValidator()

validator.validate_emails("testexample.com")
validator.validate_age(-5)
invalidator.validate_identity("Rint")
print(validator.get_errors())