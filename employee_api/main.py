
from fastapi import FastAPI, HTTPException, Query, Response
from pydantic import BaseModel, Field

app = FastAPI(title="Employee Management API", version="1.0.0")


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    department: str = Field(min_length=1, max_length=50)
    salary: float = Field(gt=0)


class Employee(EmployeeCreate):
    id: int


employees: dict[int, Employee] = {}
next_id = 1


@app.get("/employees", response_model=list[Employee])
def list_employees(
    department: str | None = None,
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    results = list(employees.values())

    if department:
        results = [
            employee for employee in results
            if employee.department.lower() == department.lower()
        ]

    return results[offset:offset + limit]


@app.post("/employees", response_model=Employee, status_code=201)
def create_employee(payload: EmployeeCreate):
    global next_id

    employee = Employee(id=next_id, **payload.model_dump())
    employees[next_id] = employee
    next_id += 1

    return employee


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    employee = employees.get(employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@app.put("/employees/{employee_id}", response_model=Employee)
def replace_employee(employee_id: int, payload: EmployeeCreate):
    if employee_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee = Employee(id=employee_id, **payload.model_dump())
    employees[employee_id] = employee

    return employee


@app.patch("/employees/{employee_id}", response_model=Employee)
def update_employee(
    employee_id: int,
    payload: dict,
):
    employee = employees.get(employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    allowed_fields = {"name", "department", "salary"}
    invalid_fields = set(payload) - allowed_fields

    if invalid_fields:
        raise HTTPException(
            status_code=422,
            detail=f"Unsupported fields: {sorted(invalid_fields)}",
        )

    updated_data = employee.model_dump()
    updated_data.update(payload)

    # Validate the complete updated employee.
    updated = Employee.model_validate(updated_data)
    employees[employee_id] = updated

    return updated


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: int):
    if employee_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    del employees[employee_id]
    return Response(status_code=204)
