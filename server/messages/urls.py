from engine.route import Router
from messages.views import send


router = Router()
router.post('send', send.Route)
