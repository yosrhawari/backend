from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Review, RendezVous
from schemas import ReviewCreate
from utils.dependencies import get_current_user

router = APIRouter(prefix="/reviews", tags=["Reviews"])

# CREATE REVIEW
@router.post("/")
def create_review(review: ReviewCreate, session: Session = Depends(get_session),user=Depends(get_current_user)):
    
    if user["role"] != "patient":
        raise HTTPException(status_code=403, detail="Not allowed")
   
   # vérifier RDV
    rdv = session.get(RendezVous, review.rendezvous_id)
    
    if not rdv:
        raise HTTPException(status_code=404, detail="Rendez-vous introuvable")

    if rdv.statut != "TERMINE":
        raise HTTPException(
            status_code=400,
            detail="Impossible de noter sans consultation terminée"
        )
    

    db_review = Review(**review.dict())
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review

# GET REVIEWS
@router.get("/")
def get_reviews(session: Session = Depends(get_session)):
    return session.exec(select(Review)).all()