# accounting_manager


# Technology

* Python 3.9
* Django 3.2
* DRF 3.14

# Endpoint

| Method   | URL                                            | Description                              |
| -------- | ---------------------------------------------- | ---------------------------------------- |
| `POST`   | `/auth/users/`                                 | Registration user.                       |
| `POST`   | `/auth/token/login/`                           | Logn user.                               |
| `GET`    | `/categories/`                                 | CRUD Categories.                         |
| `PATCH`  |   -//-                                         |                                          |
| `UPDATE` |   -//-                                         |                                          |
| `DELETE` |   -//-                                         |                                          |
| `GET`    |`/transactions/?ordering=-amount&ordering=date` | CRUD Categories.(orderby date and amount)|
| `PATCH`  |   -//-                                         |                                          |
| `UPDATE` |   -//-                                         |                                          |
| `DELETE` |   -//-                                         |                                          |
| `GET`    |`/statistics/`                                  | Statistic of user(current balance)       |

Cronjobs - sending messages automatically daily at 23:59(sends user transactions for the current day)
![Sending messages on email ](https://user-images.githubusercontent.com/88445455/200417434-feb66b88-0931-40d2-9f45-f43ed01ad522.PNG)
Transaction, statistics and categories by authorizated user 
![statistics](https://user-images.githubusercontent.com/88445455/200417469-97578453-173b-458b-88f3-feca43bc418d.PNG)


# The second task in the folder "SQL task-2"
