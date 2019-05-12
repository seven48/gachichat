from engine.route import Router
from messages.views import send, get


router = Router()
router.post('send', send.Route)
router.get('get', get.Route)
