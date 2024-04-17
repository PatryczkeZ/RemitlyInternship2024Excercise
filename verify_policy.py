import json

#function to verify the Resource field
def verify_single_asterisk():
    try:
        data = json.loads(file)
        statements = data.get("PolicyDocument").get("Statement")
        for statement in statements:
            resource = statement.get("Resource")
            if resource == "*":
                print("The Resource field contains only single asterisk!")
                return False
            elif resource is not str:
                print("Resource field is not a string!")
                return True
            elif resource == "":
                print("The Resource field is empty!")
                return True
            else:
                print("The Resource field doesn't contain single asterisk. It contains: ", resource)
                return True
    except:
        print("There is a problem with policy file!")

#Loading file
file = open("policy_file.json")
file = file.read()
verify_single_asterisk()

