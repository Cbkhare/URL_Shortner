## URL SHORTNER

This is a small project on URL Shortner. '

- #### V1:
  Version 1 of the project provides basic CRUD utilities to:

  - CREATE: Generate a shortned URL string for a given URL string.
  - GET SHORT URL: After a URL is shortened, user can fetch the shortened URL from the original long URL.
  - GET LONG URL: After a URL is shortened, user can fetch the original long URL from the shortened URL.
  - DELETE: Deletes all the details of the LONG Original URL from the system .
  - This version currently uses and in-memory dictionary to maintain the data of the original-long URL and the short-url.
  - User can use this service to generate the short URL and render the long URL.
  - The service is hosted on a flask server with the set of APIs.
  - To shorten the URL, MD5 hash algorithm is used.


  - ##### How to run the app:
    App can be hosted on a docker container or directly on the host.

    - To run on host, execute:
      ```
      /server> python3 flask_app.py
      ```

    - To run in a docker container, execute:

      - Build the image
        ```
        /server> docker build -t test:1 .
        ```
      - Start the container,
        (note:
         1. app is hosted on port 8080
         2. you can replace 8999 with other available port on your machine)
        ```
        /server> docker run --name test -p 8999:8080 test:1
        ```
    - Curl commands to test the execution
      Note: replace port number as per the type of deployment.
      - CREATE

      ```
      curl --header "Content-Type: application/json" --request POST  --data '{"url":"hello.com"}' 0.0.0.0:8999/create
      ```

      - GET SHORT URL

      ```
      curl --header "Content-Type: application/json" --request GET  --data '{"url":"hello.com"}' 0.0.0.0:8999/getShortUrl
      ```

      - GET LONG URL

      ```
      curl --header "Content-Type: application/json" --request GET  --data '{"url":"d123c212edd078f4324f3ca1af755527"}' 0.0.0.0:8999/getLongUrl
      ```

      - DELETE

      ```
      curl --header "Content-Type: application/json" --request POST  --data '{"url":"hello.com"}' 0.0.0.0:8999/delete
      ```

    - Unit test execution

      ```
      /server> python3 -m unittest -v
      ```