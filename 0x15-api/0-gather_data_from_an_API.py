#!/usr/bin/python3
""" module doc """
import requests
import sys


def main():
    """ def com """
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    done = f'{todos}&completed=true'
    notDone = f'{todos}&completed=false'
    userData = requests.get(f'{url}{users}').json()
    Name = userData[0].get("name")
    todosData = requests.get(f'{url}{todos}').json()
    todosDone = requests.get(f'{url}{done}').json()
    doneN = len(todosDone)
    totalN = len(todosData)
    print(f'Employee {Name} is done with tasks({doneN}/{totalN}):')
    for task in todosDone:
        print("\t "+task.get("title"))


if __name__ == "__main__":
    main()

"""
Employee *NAME* is done with tasks(*DONE*/*TOTAL*):
     *TITLE*
     *TITLE*
     *TITLE*


https://jsonplaceholder.typicode.com/users?id=1
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
https://jsonplaceholder.typicode.com/todos?userId=5
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  },
  ]

https://jsonplaceholder.typicode.com/todos?userId=5&completed=true
https://jsonplaceholder.typicode.com/todos?userId=5&completed=false
"""
