# BI Code Challenge

Code challenge for the Business Intelligence Manager position.

## Data

Within this repository you're given a dataset in the form of a csv file, containing a log of users making route searches. The csv consists of the following columns:

`user_id`: A user's unique id.<br>
`query_time`: The time when the user's route search was issued (when did it hit the server).<br>
`search_time`: The time for which a user asked for a route.<br>
`search_mode`: How the search time is to be interpreted: search by arrival or by departure time.<br>
`search_origin_lat`: Latitude of the searched route origin.<br>
`search_origin_lon`: Longitude of the searched route origin.<br>
`search_destination_lat`: Latitude of the searched route destination.<br>
`search_destination_lon`: Longitude of the searched route destination.

## Task

Given that route searches are a key business metric, your task is to:

   - Extract valuable insights from the data related to said metric (hint: one such insight might be user retention)

   - Convey the gathered insights effortlessly, that is in an easily understandable manner

The language of choice for data analysis at Ally is Python, though we don't mandate the tools for the solution. Choose the tools and language that you think are best to accomplish the task. It's important though that the presented analyses can be reliably reproduced, and that you're able to convey the results of your analysis. You can always choose more than one way to present those insights.

Whenever questions arise during the task please don't hesitate to ask us.

## Developing your solution:

1. Please clone the repository to your local machine via:

    ```
    git clone https://github.com/allyapp/bi-code-challenge.git
    ```

    or download a zip archive of this repository [here](https://github.com/allyapp/bi-code-challenge/archive/master.zip).

2. Fulfill the given task.

3. Submit your solution:

    Please submit your solution in the form of a publicly accessible git repository. Please make sure to submit the full git commit history with the project and please include instructions for running your code where necessary.

    Alternatively, you can submit a zip archive of your project via email.
