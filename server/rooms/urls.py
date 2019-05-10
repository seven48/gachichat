from engine.route import Router
from rooms.views import create


router = Router()
router.post('create', create.Route)
