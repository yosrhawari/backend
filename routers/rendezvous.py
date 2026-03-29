from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import RendezVous
from schemas import RendezVousCreate

router = APIRouter(prefix="/rendezvous", tags=["RendezVous"])

# CREATE RDV
@router.post("/")
def create_rdv(rdv: RendezVousCreate, session: Session = Depends(get_session)):
    db_rdv = RendezVous(**rdv.dict())
    session.add(db_rdv)
    session.commit()
    session.refresh(db_rdv)
    return db_rdv

# GET ALL RDV
@router.get("/")
def get_rdv(session: Session = Depends(get_session)):
    return session.exec(select(RendezVous)).all()