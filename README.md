# covid-api-india

### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/tushxr16/covid-api-india.git
  $ cd covid-api-india
  ```

2. Initialize and activate the virtual env:
  
  I have used virtual-env here to create the env.
  ```
  $ pip install virtualenv
  ```
  If error occurs it must be probably due to the EXECUTION_POLICY. Change it via running as admin PS. 
  ```
  $ SET ExecutionPolicy unrestricted
  ```
  Accept the ExecutionPolicy status.
  ```
  $ .\env\Scripts\activate.ps1
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python .\app.py
  ```

6. Navigate to [http://localhost:8000](http://localhost:800)

7. Create a local Git repository:

  ```
  $ git init
  $ git add .
  $ git commit -am "your commit msg"
  ```

8. Push changes to code on Heroku:

  ```
  $ git push heroku master
  ```
