# Proxy method
class College:
    """Resource-intensive object"""
    def studyingInCollege(self):
        print("Studying In College....")
        
class CollegeProxy:
    """Relatively less resource-intensive proxy acting as middleman. Instantiates a College object only if there is no fee due."""
    def __init__(self):
        self.feeBalance = 1000
        self.college = None
        
    def studyingInCollege(self):
        print("Proxy in action. Checking to see if the balance of student is clear or not...")
        
        if self.feeBalance <= 500:
            # If the balance is less than 500, let him study.
            self.college = College()
            self.college.studyingInCollege()
            
        else:
            # Otherwise, don't instantiate the college object.
            print("Your fee balance is greater than 500, first pay the fee")
            
# Main method
if __name__ == "__main__":
    # Instatiate the Proxy
    collegeProxy = CollegeProxy()
    
    # Client attempting to study in the college at the default balance of 1000.
    # Logically, since he/she study with such balance, 
    # there is no need to make the college object
    collegeProxy.studyingInCollege()
    collegeProxy.feeBalance = 100
    
    # Client attempting to study in college at the balance of 100. Should succeed.
    collegeProxy.studyingInCollege()
    
# Applicability
# Virtual Proxy: Most importantly used in Databases for example there exist certain heavy resource consuming data in the database and we need it frequently. so. here we can use the proxy pattern which would create multiple proxies and point to the object.
# Protective Proxy: It creates a protective layer over the application and can be used in the scenarios of Schools or Colleges where only a few no. of websites are allowed to open with there WiFi.
# Remote Proxy: It is particularly used when the service object is located on a remote server. In such cases, the proxy passes the client request over the network handling all the details.
# Smart proxy: It is used to provide the additional security to the application by intervene specific actions whenever the object would be accessed.
