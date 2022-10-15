Create Table User_Audit(
UserName varchar2(15),
Table_Name varchar2(15),
Column_Name varchar2(15),
Ins Number(4),
Upd Number(4),
del Number(4),
Max_ins Number(4),
Max_upd Number(7),
Max_Del Number(4));
insert into User_Audit(UserName,Table_Name,Column_Name,Ins,Upd,del,Max_ins,Max_upd,Max_Del)
Values('Muneebuit','Teacher','TeacherName',null,1,null,null,5,null);

CREATE OR REPLACE TRIGGER audit_Teacher
AFTER DELETE OR INSERT OR UPDATE ON Teacher
FOR EACH ROW
BEGIN
IF DELETING THEN
UPDATE User_Audit
SET del = del + 1
WHERE user_name = 'Muneebuit'
AND table_name = 'Teacher'
AND column_name ='TeacherName';

ELSIF INSERTING THEN
UPDATE User_Audit
SET ins = ins + 1
WHERE user_name = 'Muneebuit'
AND table_name = 'Teacher'
AND column_name = 'TeacherName';
ELSE
UPDATE User_Audit
SET upd = upd + 1
WHERE user_name = 'Muneebuit'
AND table_name = 'Teacher'
AND column_name = 'TeacherName';
END IF; END;



Create Sequence TeacherSeq
Increment by 1
Start with 12
MaxValue 20;
Insert into Teacher(TeacherID,TeacherName,DepartmentNo,CourseID)
Values(TeacherSeq.Nextval,'Dr Lubaid Ahmed',02,'CS311');



Create Sequence StudentSeq
Increment by 1
Start with 12
MaxValue 20;



INSERT INTO Student(Studentid,fullname,gender, email, address, dob, major, semester, admissionDate, courseID)
VALUES (StudentSeq.Nextval,'Ahmed Raza','Male', 'AhmedRaza1@gmail.com', 'Gulshan','11-JUN-2000','Software','Five','1-JAN-2019','CS312');



Create Sequence DepartmentSeq
Increment by 1
Start with 12
MaxValue 20;



Insert into Department(DepartmentNo,DepartmentName)
Values(DepartmentSeq.Nextval,'Electrical');