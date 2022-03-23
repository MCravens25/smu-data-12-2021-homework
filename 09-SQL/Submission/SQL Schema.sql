﻿-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "departments" (
    "dept_no" VARCHAR(10) NOT NULL,
    "dept_name" VARCHAR(50) NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "title" (
    "title_ID" VARCHAR(10)   NOT NULL,
    "title" VARCHAR(50),
    "last_updated" timestamp default localtimestamp NOT NULL,
    CONSTRAINT "pk_title" PRIMARY KEY (
        "title_ID"
     )
);

CREATE TABLE "employees" (
    "emp_no" Int NOT NULL,
    "emp_title_ID" VARCHAR(10) NOT NULL,
    "birth_date" date,
    "first_name" VARCHAR(100),
    "last_name" VARCHAR(100),
    "sex" VARCHAR(5),
    "hire_date" date,
    "last_updated" timestamp default localtimestamp Not Null,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "dept_employee" (
    "emp_no" Int NOT NULL,
    "dept_no" VARCHAR(10) NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL
);

CREATE TABLE "dept_manager" (
    "dept_no" VARCHAR(10) NOT NULL,
    "emp_no" Int NOT NULL,
    "last_updated" timestamp default localtimestamp NOT NULL
);

CREATE TABLE "salaries" (
    "emp_no" Int NOT NULL,
    "salary" Int,
    "last_updated" timestamp default localtimestamp  NOT NULL
);

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_ID" FOREIGN KEY("emp_title_ID")
REFERENCES "title" ("title_ID");

ALTER TABLE "dept_employee" ADD CONSTRAINT "fk_dept_employee_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_employee" ADD CONSTRAINT "fk_dept_employee_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

