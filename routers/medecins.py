from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import ProfilMedecin
from schemas import MedecinCreate

router = APIRouter(prefix="/medecins", tags=["Medecins"])

# CREATE MEDECIN
@router.post("/")
def create_medecin(med: MedecinCreate, session: Session = Depends(get_session)):
    db_med = ProfilMedecin(**med.dict())
    session.add(db_med)
    session.commit()
    session.refresh(db_med)
    return db_med

# GET ALL MEDECINS (VALIDES SEULEMENT)
@router.get("/")
def get_medecins(session: Session = Depends(get_session)):
    statement = select(ProfilMedecin).where(
        ProfilMedecin.statut_validation == "VALIDE"
    )
    return session.exec(statement).all()