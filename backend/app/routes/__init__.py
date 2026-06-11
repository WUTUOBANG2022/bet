from .auth import router as auth_router
from .matches import router as matches_router
from .bets import router as bets_router
from .users import router as users_router

__all__ = ["auth_router", "matches_router", "bets_router", "users_router"]
