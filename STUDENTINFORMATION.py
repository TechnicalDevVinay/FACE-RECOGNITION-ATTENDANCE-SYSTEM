import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/SEM 6 PROJECT/")
firebase_admin.initialize_app(cred,{
    'databaseURL':"//"
})

ref = db.reference('STUDENTS')

data = {
    "8791":
    {
    "NAME":"VINAY VIJAY TAWDE",
    "BACHELORS":"ARTIFICIAL INTELLIGENCE",
    "STARTING_YEAR":2023,
    "TOTAL_ATTENDENCE":1,
    "RANKING": "A1",
    "YEAR":1,
    "LAST_ATTENDENCE_TIME": "2023-03-08 00:17:18"
    },

    "8792":
    {
    "NAME":"PEYUSH BANSAL",
    "BACHELORS":"ARTIFICIAL INTELLIGENCE",
    "STARTING_YEAR":2023,
    "TOTAL_ATTENDENCE":1,
    "RANKING": "A1",
    "YEAR":1,
    "LAST_ATTENDENCE_TIME": "2023-03-08 00:17:18"
    },

    "8793":
    {
    "NAME":"SATYA NADELLA",
    "BACHELORS":"ARTIFICIAL INTELLIGENCE",
    "STARTING_YEAR":2023,
    "TOTAL_ATTENDENCE":1,
    "RANKING": "A1",
    "YEAR":1,
    "LAST_ATTENDENCE_TIME": "2023-03-08 00:17:18"
    },

    "8794":
    {
    "NAME":"SUNDAR PICHAI",
    "BACHELORS":"ARTIFICIAL INTELLIGENCE",
    "STARTING_YEAR":2023,
    "TOTAL_ATTENDENCE":1,
    "RANKING": "A1",
    "YEAR":1,
    "LAST_ATTENDENCE_TIME": "2023-03-08 00:17:18"
    },

    "8795":
    {
    "NAME":"TIM COOK",
    "BACHELORS":"ARTIFICIAL INTELLIGENCE",
    "STARTING_YEAR":2023,
    "TOTAL_ATTENDENCE":1,
    "RANKING": "A1",
    "YEAR":1,
    "LAST_ATTENDENCE_TIME": "2023-03-08 00:17:18"
    },
    

}
for key, value in data.items():
    ref.child(key).set(value)
