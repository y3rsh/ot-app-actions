Param(
    [string]$version
)

Invoke-WebRequest "https://chromedriver.storage.googleapis.com/$version/chromedriver_win32.zip" -OutFile chromedriver_win32.zip

Expand-Archive -Path chromedriver_win32.zip -DestinationPath C:\SeleniumWebDrivers\ChromeDriver -Force
Remove-Item chromedriver_win32.zip
