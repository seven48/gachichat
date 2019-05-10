from engine.route import Router
from rooms.views import create, info


router = Router()
router.post('create', create.Route)
router.get('info', info.Route)
