class RecordCreate(BaseModel):
    machine_name: str
    operation: str
    output_count: int
    defect_count: int
    failure_type: str = None
    notes: str = ""
    company_id: int

class RecordResponse(RecordCreate):
    id: int
    class Config:
        from_attributes = True
