class TicketCreate(BaseModel):
    customer_name: str
    customer_email: str
    description: str
    company_id: int

class TicketResponse(TicketCreate):
    id: int
    category: str
    status: str
    class Config:
        from_attributes = True
