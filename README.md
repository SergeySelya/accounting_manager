# accounting_manager


# Technology

* Python 3.9
* Django 3.2
* DRF 3.14

#Endpoint

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

Cronjobs - sending messages automatically daily at 23:59
