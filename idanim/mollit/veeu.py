from selenium.webdriver.chrome.service import Service

# Create a Service object to specify the path to the ChromeDriver executable
service = Service(executable_path="/path/to/chromedriver")

# Create a Chrome WebDriver instance using the Service object
driver = webdriver.Chrome(service=service)
