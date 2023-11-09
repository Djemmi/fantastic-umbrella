class schoolDB:
    db = {}
    name = "default-db-name"

    # constructor
    def __init__(self, databasename):
        self.name = databasename

    # getters
    def getName(self) -> str:
        return self.name

    def getStudents(self, classname: str) -> []:
        students = []
        for student_number in range(1, self.db[classname]["count"] + 1):
            students.append(self.db[classname][student_number])
        return students

    def getClassNames(self):
        return list(self.db.keys())

    def getDbData(self):
        total_students = 0
        classes_data = {}
        total_classes = len(self.db.keys())

        for classname in self.db.keys():
            total_students += self.db[classname]["count"]
            classes_data[classname] = self.getStudents(classname)

        print("DataBase data:")
        print("Total students amount:", total_students)
        print("Total classes amount:", total_classes)
        print("Classes lists:")
        for printfclass in classes_data.keys():
            print(printfclass, "|", ", ".join(classes_data[printfclass]))

    # setters

    # methods
    def addClass(self, classname: str, list_of_students: []):
        self.db[classname] = {"count": len(list_of_students)}
        for student in range(1, len(list_of_students) + 1):
            self.db[classname][student] = list_of_students[student - 1]

    def addStudent(self, classname, studentname):
        self.db[classname][self.db[classname]["count"] + 1] = studentname
        self.db[classname]["count"] += 1

    def disband_class(self, classname):
        if len(self.db) < 2:
            print("UNABLE TO DISBAND CLASS")
        disbaned_students = self.getStudents(classname)
        self.db.pop(classname)
        classes_left = self.getClassNames()  # array of other classes
        for student in range(len(disbaned_students)):
            self.addStudent(str(classes_left[student % len(classes_left)]), disbaned_students[student])


myDB = schoolDB("School")
myDB.addClass("1a", ["vasya", "vasya2"])
myDB.addClass("1b", ["max1", "max2", "max3"])
myDB.addClass("1c", ["vanya"])
myDB.getDbData()

"""
DB STRUCTURE JSON-type
{
    "name1: {
        "count" : i_count | static field, createt at init
        "1": "name   
    },
    "name2: {
        "count" i_count
        "1": name
    }

}
"""
